def main():
    n, p, s = map(int, input().split())
    for _ in range(s):
        _, *x = map(int, input().split())
        print("KEEP" if p in x else "REMOVE")

if __name__ == '__main__':
    main()
