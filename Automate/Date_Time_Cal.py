import datetime
import calendar

x = datetime.datetime.now()

print(x)
print(x.year)
print(x.strftime("%B"))#Month
print(x.strftime("%A")) #Day
print(x.strftime("%C")) #Date


y = datetime.datetime(2020,8,19)

print(y)

cal = calendar.month(2017,2)
print(cal)
