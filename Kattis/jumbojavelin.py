def main():
    x = [int(input()) for _ in range(int(input()))]
    return sum(x) - (len(x) - 1)

if __name__ == '__main__':
    print(main())
