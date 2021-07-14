s, a, A = list(input()), list('abcdefghijklmnopqrstuvwxyz'), 26

s1, s2 = s[0:len(s) // 2], s[len(s) // 2:len(s)]
s1_r, s2_r = sum([a.index(i.lower()) for i in s1]), sum([a.index(i.lower()) for i in s2])

for i in range(len(s1)):
  s1[i] = a[(s1_r + a.index(s1[i].lower())) % A]

for i in range(len(s2)):
  s2[i] = a[(s2_r + a.index(s2[i].lower())) % A]

for i in range(len(s1)):
  s1[i] = a[(a.index(s2[i].lower()) + a.index(s1[i].lower())) % A]

print("".join(s1).upper())
