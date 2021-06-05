r = lambda x: {'South': 'East',  'North': 'West',  'West': 'South', 'East': 'North'}[x]
s = lambda x: {'South': 'West',  'North': 'East',  'West': 'North', 'East': 'South'}[x]
t = lambda x: {'South': 'North', 'North': 'South', 'West': 'East',  'East': 'West' }[x]
u = lambda a, b: a == 'North' and b == 'South' or (b == 'North' and a == 'South') or (a == 'East' and b == 'West' or (a == 'West' and b == 'East'))

def main(a, b, c):
    return u(a, b) and c == r(a) or (b == s(a) and (t(a) == c or c == r(a)))

if __name__ == '__main__': print("Yes" if main(*map(str, input().split())) else "No")
