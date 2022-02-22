from queue import Queue
# use queues to help with ordering

n, m = map(int, input().split())
a, b = Queue(), Queue()
vis = [0] * int(2e5)

for i in range(m):
  x = int(input())
  vis[x] = 1
  a.put(x)

for i in range(1, n + 1):
  if not vis[i]:
    b.put(i)

for _ in range(n):
  if a.empty():
    print(b.get())
  elif b.empty():
    print(a.get())
  elif a.queue[0] < b.queue[0]:
    print(a.get())
  else:
    print(b.get())
