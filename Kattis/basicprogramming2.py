from collections import Counter

def main():
    n, t = map(int, input().split()); b = sorted(list(map(int, input().split())))
    {1: lambda x: print(one(x)),
     2: lambda x: print("Unique" if len(x) == len(set(x)) else "Contains duplicate"),
     3: lambda x: print(three(x)),
     4: lambda x: print(b[len(x) // 2] if len(x) % 2 == 1 else "{0} {1}".format(x[len(x) // 2 - 1], x[len(x) // 2])),
     5: lambda x: print(*list(filter(lambda x: x >= 100 and x <= 999, b)), sep=" ")}[t](b)

def one(b):
    for i in range(1, 7777):
        if i in b and 7777 - i in b: return "Yes"
    return "No"

def three(b):
    x, y = Counter(b).most_common(1)[0]; return x if y > len(b)/2 else -1

if __name__ == '__main__':
    main()
