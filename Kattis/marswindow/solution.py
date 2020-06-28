def main():
    yr = int(input())
    print(solve(yr))


def solve(yr):
    curr = 3
    year = 2018
    if yr == 2018:
        return 'yes'
    else:
        while True:
            year += 2
            curr += 2
            if curr >= 12:
                curr %= 12
                year += 1
            if year > yr:
                return 'no'
            if year == yr:
                return 'yes'


main()
