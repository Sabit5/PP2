from math import tan, pi #regular polygon


sides = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
p_area = int(sides * (length ** 2) / (4 * tan(pi / sides)))


print("The area of the polygon is: ", p_area)
