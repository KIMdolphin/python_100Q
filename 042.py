import datetime
month = int(input())
date = int(input())
def findDay(a,b):
    day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return day[datetime.date(2020,a,b).weekday()]
print(findDay(month,date))
