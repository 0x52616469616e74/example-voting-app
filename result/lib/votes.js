'use strict';

function collectVotesFromResult(result) {
  const votes = {a: 0, b: 0};

  result.rows.forEach(function (row) {
    votes[row.vote] = Number.parseInt(row.count, 10);
  });

  return votes;
}

module.exports = { collectVotesFromResult };
