import datetime

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print(datetime.datetime.now().isoformat(sep = " ", timespec = "seconds"))