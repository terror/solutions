import sys


def check(a):
    for b in range(len(a)):
        if "problem" in a[b].lower():
            return "Yes"
    return "No"


for i in sys.stdin:
    a = list(map(str, i.split()))
    print(check(a))
