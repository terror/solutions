n = int(input())
w = input()

for i in range(n, 0, -1):
  if i > 2:
    print("{0} bottles of {1} on the wall, {2} bottles of {3}.".format(i, w, i, w))
    print("Take one down, pass it around, {0} bottles of {1} on the wall.\n".format(i - 1, w))
  elif i == 2:
    print("{0} bottles of {1} on the wall, {2} bottles of {3}.".format(i, w, i, w))
    print("Take one down, pass it around, {0} bottle of {1} on the wall.\n".format(i - 1, w))
  else:
    print("{0} bottle of {1} on the wall, {2} bottle of {3}.".format(i, w, i, w))
    print("Take it down, pass it around, no more bottles of {0}.".format(w))
