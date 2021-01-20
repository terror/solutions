from datetime import date
d, m = list(map(int, input().split()))
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
print(days[date(2009, m, d).weekday()])
