// ======================================================PROBLEM STATEMENT==================================================

// You are given a string S consisting of letters 'a' and/or 'b'.
// A block is a consecutive fragment of S composed of the same letters and surrounded by different letters or string endings.

// For example, S = 'abbabbaaa" has five blocks: "a", "bb", "a", "bb" and "aaa".
// What is the minimum number of additional letters needed to obtain a string containing blocks of equal lengths?


// Letters can be added at the beginning, between two existing letters, or at the end of the string.
// Write a function: def solution (5) that, given a string S of length N,
// returns the minimum number of additional letters needed to obtain a string containing blocks of equal lengths.


// Examples: 1. Given S="babaa", the function should return 3. There are four blocks: "b", "a", "b", "aa".
// One letter each should be added to the first, second and third blocks, therefore obtaining a string "bbaabbaa", in which every block is of equal length.
// 2. Given S="bbbab", the function should return 4.
// Two letters each should be added to the second and third blocks, therefore obtaining a string "bbbaaabbb", in which every block is of equal
// 3. Given S="bbbaaabbb", the function should return 0. All blocks are already of equal length.


// Write an efficient algorithm for the following assumptions: N is an integer within the range [1..40,000];
// • string S consists only of the characters "a" and/or "b".

//=========================================================================================================================

function solution(S) {
    let arrayOfNumbers = [];
    let maxCount = 0;
    let count = 0;
    //walk through the string and separate the blocks
    for (let i = 0, j = 0; i < S.length; i++) {
        if (S[i] === S[j]) {
            count++;
            maxCount = Math.max(count, maxCount);
        } else {
            arrayOfNumbers.push(count);
            count = 1;
            j = i;
        }

        if (i === S.length - 1 && count !== 0) arrayOfNumbers.push(count);
    }
    let result = 0;
    // walk through newly created array and compare the numbers with maxCount and add the difference to the result
    for (let num of arrayOfNumbers) {
        if (num < maxCount) result += maxCount - num;
    }
    return result;
}
solution("ababb") // return 3

//=========================================================================================================================