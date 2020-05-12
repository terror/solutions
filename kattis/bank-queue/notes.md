## Bank Queue
The problem can be found [here](https://open.kattis.com/problems/bank).

- Difficulty: 2.7 (Easy)

## The Solution

This problem was a bit tricky as you have to look at it backwards. 

To solve, I sorted everyone by their corresponding time values, then looked through times from longest to shortest and compared which dollar amount is worth serving by pulling out the greatest value and leaving the smaller value for the next round of comparison.

This way, we are only serving clients that have the highest dollar values while staying within the timeframe. 