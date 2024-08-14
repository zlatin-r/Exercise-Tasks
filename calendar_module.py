import calendar

month, day, year = map(int, input().split())

result = calendar.weekday(year, month, day)