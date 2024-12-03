class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print("Rectangle: Length = ",self.length," Width = ",self.width)
        print("Area =" ,self.area(), "Perimeter =" ,self.perimeter())

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rect = Rectangle(length, width)
rect.display()
