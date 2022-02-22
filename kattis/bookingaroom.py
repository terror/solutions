r, n = list(map(int, input().split()))
rooms = []

# add all rooms 1 to r
for i in range(1, r + 1):
  rooms.append(i)

# remove booked rooms
for i in range(n):
  rooms.remove(int(input()))

# if there's still rooms left print any one, else too late
if (len(rooms)):
  print(rooms[0])
else:
  print("too late")
