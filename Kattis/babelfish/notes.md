## Babelfish
The problem can be found [here](https://open.kattis.com/problems/babelfish).

- Difficulty: 2.2 (Easy/Trivial)

## The Solution

To solve this problem I made use of a dictionary by adding each non english word as a key with it's corresponding english word as a value. 

I then went and looked through the remaining lines and if the line matched with a key in the dictionary, I printed out it's value or else I printed out "eh" as instructed in the problem. 