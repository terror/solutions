(lambda l: print(chr(sum(map(lambda x: ord(x), l)) // len(l))))(list(input()))
