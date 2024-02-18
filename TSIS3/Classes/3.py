class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

print("Rectangle:")
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
rectangle = Rectangle(length, width)
print("Area:", rectangle.area())
