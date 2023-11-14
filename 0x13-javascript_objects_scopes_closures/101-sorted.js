#!/usr/bin/node

const { dict } = require('./101-data');

function computeUserIdsByOccurrence (dict) {
  const userIdsByOccurrence = {};

  // Iterate over the original dictionary
  for (const userId in dict) {
    const occurrences = dict[userId];

    // Check if occurrences is a valid number
    if (Number.isInteger(occurrences)) {
      // Add the user id to the corresponding occurrences in the new dictionary
      if (userIdsByOccurrence[occurrences]) {
        userIdsByOccurrence[occurrences].push(userId);
      } else {
        userIdsByOccurrence[occurrences] = [userId];
      }
    }
  }

  return userIdsByOccurrence;
}

// Compute the new dictionary
const userIdsByOccurrence = computeUserIdsByOccurrence(dict);

// Print the new dictionary
console.log(userIdsByOccurrence);
