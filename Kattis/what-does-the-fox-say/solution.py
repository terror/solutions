# loop through first input n 
# add first line to list
# for remaining, if len == 3 add line[2] to set
# filter list

n = int(input())

def filterList(lst, sounds):
	return (" ".join(filter(lambda a: a not in sounds, lst)))

for i in range(n):
	lst = input().split()
	sounds = set()
	
	while True:
		line = input().split()
		if(len(line) == 3):
			sounds.add(line[2])
		else:
			 res = filterList(lst, sounds)
			 print(res)
			 break


