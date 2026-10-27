'use strict';

const assert = require('node:assert/strict');
const test = require('node:test');
const { collectVotesFromResult } = require('../lib/votes');

test('starts with zero votes when the database returns no rows', function () {
  assert.deepEqual(collectVotesFromResult({rows: []}), {a: 0, b: 0});
});

test('converts PostgreSQL counts to numbers', function () {
  const result = {rows: [
    {vote: 'a', count: '3'},
    {vote: 'b', count: '7'}
  ]};

  assert.deepEqual(collectVotesFromResult(result), {a: 3, b: 7});
});
