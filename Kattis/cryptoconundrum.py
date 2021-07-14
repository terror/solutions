s = input()
print(
    sum([(i % 3 == 0 and s[i] != 'P') + (i % 3 == 1 and s[i] != 'E') + (i % 3 == 2 and s[i] != 'R')
         for i in range(len(s))]))
