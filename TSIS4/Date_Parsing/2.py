import datetime


x = datetime.datetime.now()
one = datetime.timedelta(days=1)

yesterday = x - one
tomorow = x + one
print(yesterday)
print(x)
print(tomorow)