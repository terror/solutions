import string

S = string.ascii_lowercase
C = input()
K = input()

ret = ''
for i, v in enumerate(C):
  if i & 1:
    ret += S[(S.index(v.lower()) + S.index(K[i].lower())) % len(S)].upper()
  else:
    ret += S[(S.index(v.lower()) - S.index(K[i].lower())) % len(S)].upper()

print(ret)
