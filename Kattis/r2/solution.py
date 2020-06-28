import sys

for i in sys.stdin:
	ab = i.split()
	print((2 * int(ab[1])) - int(ab[0]))
