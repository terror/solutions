from collections import Counter

board = [list(input()) for i in range(8)]
R = C = len(board)


def row(r):
    return Counter(board[r])['*'] == 1


def col(c):
    return Counter(list(zip(*board))[c])['*'] == 1


def diag():
    q = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == '*':
                q.append([i, j])

    if len(q) != 8:
        return False

    for i in range(len(q)):
        a, b = q[i]
        for j in range(len(q)):
            if i == j:
                continue
            c, d = q[j]
            if abs(a-c) == abs(b-d):
                return False
    return True


def main():
    if not diag():
        print('invalid')
        exit()

    for i in range(R):
        for j in range(C):
            if board[i][j] == '*':
                if not row(i) or not col(j):
                    print('invalid')
                    exit()
    print('valid')


if __name__ == '__main__':
    main()
