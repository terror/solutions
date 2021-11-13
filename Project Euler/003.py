# Problem 3: Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

N = 600851475143

i = 2
while i * i <= N:
  if N % i:
    i += 1
  else:
    N //= i

print(N)
