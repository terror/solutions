g = list(map(int, input().split()))
e = list(map(int, input().split()))

if sum(g) > sum(e):
    print("Gunnar")
elif sum(e) > sum(g):
    print("Emma")
else:
    print("Tie")
