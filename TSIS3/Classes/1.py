class to_upper:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print("Uppercase string:", self.string.upper())


manipulator = to_upper()
manipulator.getString()
manipulator.printString()
