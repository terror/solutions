def main(a, b, c, d):
    return 1 if a-c >= 2 and b-d >= 2 else 0

if __name__ == '__main__':
    print(main(*map(int, input().split())))
