import string

def pangram(s, a):
  if set(s.lower()) >= a:
    return "YES"
  else:
    return "NO"

a = set(string.ascii_lowercase)
n = int(input())
s = input()
print(pangram(s, a))
