#!/usr/bin/node
// It returns a number of occurrences in the list
exports.nbOccurences = function (list, searchElement) {
    let count = 0;
  
    for (let idx = 0; idx < list.length; idx++) {
      if (list[idx] === searchElement) {
        count++;
      }
    }
    return count;
  };
