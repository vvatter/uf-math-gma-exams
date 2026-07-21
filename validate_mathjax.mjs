#!/usr/bin/env node

import readline from 'node:readline';
import {pathToFileURL} from 'node:url';

const failures = [];
const [bundlePath, fontPath] = process.argv.slice(2);

if (!bundlePath || !fontPath) {
  process.stderr.write('usage: node validate_mathjax.mjs BUNDLE_PATH FONT_PATH\n');
  process.exit(2);
}

const bundleUrl = pathToFileURL(`${bundlePath}/`).href.replace(/\/$/, '');
const fontUrl = pathToFileURL(`${fontPath}/`).href.replace(/\/$/, '');

global.MathJax = {
  loader: {
    paths: {mathjax: bundleUrl, 'mathjax-newcm': fontUrl},
    load: ['input/tex', 'output/chtml', 'adaptors/liteDOM'],
    require: (file) => import(file),
  },
  output: {font: fontUrl},
  tex: {
    packages: {'[-]': ['noundefined']},
    formatError(_jax, error) {
      throw error;
    },
  },
  options: {
    compileError(_document, _math, error) {
      throw error;
    },
    typesetError(_document, _math, error) {
      throw error;
    },
  },
};

try {
  await import(`${bundleUrl}/startup.js`);
  await MathJax.startup.promise;

  const input = readline.createInterface({input: process.stdin, crlfDelay: Infinity});
  for await (const line of input) {
    if (!line.trim()) continue;
    const record = JSON.parse(line);
    try {
      await MathJax.tex2chtmlPromise(record.tex, {display: record.display});
    } catch (error) {
      failures.push({...record, message: error.message || String(error)});
    }
  }
  MathJax.done();
} catch (error) {
  const detail = error?.message || String(error);
  process.stderr.write(`MathJax validator failed to start: ${detail}\n`);
  process.exit(2);
}

process.stdout.write(`${JSON.stringify({failures})}\n`);
process.exitCode = failures.length ? 1 : 0;
