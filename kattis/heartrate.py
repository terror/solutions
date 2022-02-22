for i in range(int(input())):
  b, p = list(map(float, input().split()))
  t = 60 / p
  tt = t * b
  print("{:.4f} {:.4f} {:.4f}".format(tt - t, tt, tt + t))
