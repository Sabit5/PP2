import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("x =", self.x, " y =", self.y)
    def move(self, x_new, y_new):
        self.x = x_new
        self.y = y_new
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y))

#1   
x1 = float(input("Enter x for point1: "))
y1 = float(input("Enter y for point1: "))
point1 = Point(x1, y1)

x2 = float(input("Enter x for point2: "))
y2 = float(input("Enter y for point2: "))
point2 = Point(x2, y2)

print("Coordinates of the point1:")
point1.show()
print("Coordinates of the point2:")
point2.show()
#3
distance = point1.dist(point2)
print("Distance between 2 points:", distance)

#2
x1 = float(input("Enter new x for point1: "))
y1 = float(input("Enter new y for point1: "))
point1.move(x1, y1)
print("New coordinates of the point1:")
point1.show()