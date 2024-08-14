import calendar

month, day, year = map(int, input().split())
week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

print(week[calendar.weekday(year, month, day)])
