# Problem 4: Largest palindrome product
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

print(max(list(filter(lambda x: (s := str(x)) and s == s[::-1], [i * j for i in range(999) for j in range(999)]))))
