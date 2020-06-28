import sys

for i in sys.stdin:
	line = i.split()
	print(abs(int(line[0]) - int(line[1])))





