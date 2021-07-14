def main():
  s, k = input().split()
  s = list(s)
  targ = sorted(s)

  if int(k) <= len(s) / 2:
    print("Yes")
  else:
    targ = find_md(targ)
    s = find_md(s)
    if s == targ:
      print("Yes")
    else:
      print("No")

def find_md(lst):
  if lst == sorted(lst):
    s = sorted(lst)
  else:
    s = lst

  index = (len(s) - 1) // 2
  m = []

  if len(s) % 2:
    return s[index]
  else:
    m.append(s[index])
    m.append(s[index + 1])
    return m

main()
