import time
a = sum(int(x) * 60 ** i for i, x in enumerate(reversed(input().split(":"))))
b = sum(int(x) * 60 ** i for i, x in enumerate(reversed(input().split(":"))))

# the most annoying edge case l0l
if a == b:
    print("24:00:00")
    exit()

ans = 0
if a > b: ans += (24*3600)-a+b
else: ans = b-a

print(time.strftime('%H:%M:%S', time.gmtime(ans)))
