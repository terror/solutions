import collections
s = input()
c = collections.Counter(s)

minval = min(c.values())
Sum = 0
three = False

if 'T' in c and 'G' in c and 'C' in c:
    three = True

for key, val in c.items():
    Sum += val**2

if(three):
    print(Sum + (7*minval))
else:
    print(Sum)
