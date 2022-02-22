def compute_success(a, b, n):
  count = 0
  if (a == b and n % 2 == 0):
    return "Deletion succeeded"
  for i in range(len(a)):
    if a[i] != b[i]:
      count += 1
      if (count == len(a) and n % 2 == 1):
        return "Deletion succeeded"
  return "Deletion failed"

n = int(input())
a = input()
b = input()
c = compute_success(a, b, n)
print(c)
