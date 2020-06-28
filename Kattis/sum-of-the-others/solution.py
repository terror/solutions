import sys


def main():
    for i in sys.stdin:
        i = list(map(int, i.split()))
        print(solve(i))


def solve(arr):
    for i in range(len(arr)):
        Sum = 0
        for j in range(len(arr)):
            if i != j:
                Sum += arr[j]
        if Sum == arr[i]:
            return arr[i]


main()
