#!/usr/bin/env python3
"""Prepare a minimal, verified MathJax cache for archive validation."""

from __future__ import annotations

import argparse
import base64
from dataclasses import dataclass
import hashlib
from io import BytesIO
import json
from pathlib import Path, PurePosixPath
import shutil
import tarfile
import tempfile
from urllib.error import URLError
from urllib.request import urlopen


MATHJAX_VERSION = "4.1.3"
CACHE_ROOT = (
    Path(__file__).resolve().parent
    / ".cache"
    / "mathjax-validator"
    / MATHJAX_VERSION
)


class MathJaxSetupError(RuntimeError):
    """Raised when the lightweight MathJax cache cannot be prepared."""


@dataclass(frozen=True)
class PackageSubset:
    name: str
    url: str
    integrity: str
    destination: str
    exact_members: frozenset[str]
    member_prefixes: tuple[str, ...]

    def includes(self, relative_path: str) -> bool:
        return relative_path in self.exact_members or relative_path.startswith(
            self.member_prefixes
        )


PACKAGES = (
    PackageSubset(
        name="@mathjax/src",
        url="https://registry.npmjs.org/@mathjax/src/-/src-4.1.3.tgz",
        integrity=(
            "sha512-rIrWquuBSoJuoMBdC/1qD+AUHTorlccPicoVy6P2xbUgnuDBpCcpbHtOAsB8L3hd"
            "CHtNBg92lF8e3Fz+pkcQbw=="
        ),
        destination="src",
        exact_members=frozenset(
            {
                "package.json",
                "LICENSE",
                "bundle/core.js",
                "bundle/loader.js",
                "bundle/startup.js",
                "bundle/output/chtml.js",
            }
        ),
        member_prefixes=("bundle/adaptors/", "bundle/input/"),
    ),
    PackageSubset(
        name="@mathjax/mathjax-newcm-font",
        url=(
            "https://registry.npmjs.org/@mathjax/mathjax-newcm-font/-/"
            "mathjax-newcm-font-4.1.3.tgz"
        ),
        integrity=(
            "sha512-gzAB3dFHilHX1l5x2xUqRL+1jDQt3Fyza1DkEMVXWC4E8SvsGdlgEza47HYi2WhV"
            "cgfkvf4zgUGzuhbq3Pjlew=="
        ),
        destination="font",
        exact_members=frozenset({"package.json", "LICENSE", "chtml.js"}),
        member_prefixes=("chtml/dynamic/",),
    ),
)

REQUIRED_FILES = (
    Path("src/bundle/startup.js"),
    Path("src/bundle/input/tex.js"),
    Path("src/bundle/output/chtml.js"),
    Path("src/bundle/adaptors/liteDOM.js"),
    Path("font/chtml.js"),
)


def cache_is_ready(cache_root: Path = CACHE_ROOT) -> bool:
    marker = cache_root / "cache.json"
    try:
        metadata = json.loads(marker.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return False
    return metadata.get("mathjax_version") == MATHJAX_VERSION and all(
        (cache_root / path).is_file() for path in REQUIRED_FILES
    )


def verified_download(package: PackageSubset) -> bytes:
    try:
        with urlopen(package.url, timeout=60) as response:
            archive = response.read()
    except (OSError, URLError) as error:
        raise MathJaxSetupError(f"could not download {package.name}: {error}") from error
    algorithm, encoded_digest = package.integrity.split("-", 1)
    if algorithm != "sha512":
        raise MathJaxSetupError(f"unsupported integrity algorithm: {algorithm}")
    expected = base64.b64decode(encoded_digest)
    actual = hashlib.sha512(archive).digest()
    if actual != expected:
        raise MathJaxSetupError(f"integrity check failed for {package.name}")
    return archive


def extract_subset(package: PackageSubset, archive: bytes, destination: Path) -> int:
    extracted = 0
    with tarfile.open(fileobj=BytesIO(archive), mode="r:gz") as package_tar:
        for member in package_tar.getmembers():
            path = PurePosixPath(member.name)
            if not member.isfile() or not path.parts or path.parts[0] != "package":
                continue
            relative = PurePosixPath(*path.parts[1:]).as_posix()
            if not package.includes(relative):
                continue
            source = package_tar.extractfile(member)
            if source is None:
                continue
            target = destination / package.destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read())
            extracted += 1
    if not extracted:
        raise MathJaxSetupError(f"no files extracted from {package.name}")
    return extracted


def prepare_mathjax(cache_root: Path = CACHE_ROOT, force: bool = False) -> Path:
    if not force and cache_is_ready(cache_root):
        return cache_root
    cache_root.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=f"{MATHJAX_VERSION}-", dir=cache_root.parent
    ) as temporary:
        temporary_root = Path(temporary)
        counts = {}
        for package in PACKAGES:
            counts[package.name] = extract_subset(
                package, verified_download(package), temporary_root
            )
        missing = [path for path in REQUIRED_FILES if not (temporary_root / path).is_file()]
        if missing:
            raise MathJaxSetupError(
                "MathJax package is missing required files: "
                + ", ".join(str(path) for path in missing)
            )
        (temporary_root / "cache.json").write_text(
            json.dumps(
                {
                    "mathjax_version": MATHJAX_VERSION,
                    "packages": {package.name: package.integrity for package in PACKAGES},
                    "files": counts,
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        if cache_root.exists():
            shutil.rmtree(cache_root)
        shutil.copytree(temporary_root, cache_root)
    return cache_root


def directory_size(path: Path) -> int:
    return sum(item.stat().st_size for item in path.rglob("*") if item.is_file())


def main() -> int:
    parser = argparse.ArgumentParser(
        description="download the minimal pinned MathJax files used by archive validation"
    )
    parser.add_argument("--force", action="store_true", help="rebuild an existing cache")
    args = parser.parse_args()
    try:
        cache_root = prepare_mathjax(force=args.force)
    except MathJaxSetupError as error:
        parser.exit(1, f"error: {error}\n")
    size_mib = directory_size(cache_root) / (1024 * 1024)
    print(f"MathJax {MATHJAX_VERSION}: {cache_root} ({size_mib:.1f} MiB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
