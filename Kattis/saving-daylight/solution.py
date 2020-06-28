import sys
# trivial, just convert times and subtract
for i in sys.stdin:
    *date, t1, t2 = i.split()
    h1, m1 = map(int, t1.split(':'))
    h2, m2 = map(int, t2.split(':'))
    T1 = 60 * (((h2 * 60 + m2)) - (h1 * 60 + m1))//3600
    T2 = 60 * (((h2 * 60 + m2)) - (h1 * 60 + m1))//60
    print(*date, "{0} hours {1} minutes".format(T1, (T2 - (T1 * 60))))
