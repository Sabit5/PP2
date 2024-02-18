import datetime

a = datetime.datetime.now()
print(f"\nNow it is: {a}")

be = input("Enter a date in format: year month(number) day hours(24) min sec: ").split()
    
Y, m, d, H, M, S = map(int, be)
b = datetime.datetime(Y, m, d, H, M, S)
c = a - b

print("difference in seconds: ", int(c.total_seconds()))