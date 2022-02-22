a, b, c = list(map(int, input().split()))
for i in range(1, c + 1):
  if i % a == 0:
    if i % b == 0:
      print("FizzBuzz")
    else:
      print("Fizz")
  elif i % b == 0:
    if i % a == 0:
      print("FizzBuzz")
    else:
      print("Buzz")
  else:
    print(i)
