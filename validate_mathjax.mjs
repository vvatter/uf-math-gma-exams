#!/usr/bin/env node

import readline from 'node:readline';

const failures = [];

global.MathJax = {
  loader: {
    paths: {mathjax: '@mathjax/src/bundle'},
    load: ['adaptors/liteDOM'],
    require: (file) => import(file),
  },
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
  await import('@mathjax/src/bundle/tex-chtml.js');
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
