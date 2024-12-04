import math

list1 = [] 

class Circle:
    def __init__(self):
        self.radius = 0

    def radius1(self):
        self.radius = float(input("Enter the radius of the circle: "))

    def area(self):
        area = math.pi * self.radius**2
        perimeter = 2 * math.pi * self.radius
        print("Radius =", self.radius)
        print("Area =", round(area, 2))
        print("Perimeter =", round(perimeter, 2))


class Person:
    def __init__(self):
        self.name = 0
        self.age = 0
        self.job = 0

    def details(self):
        self.name = input("Enter the name of the person: ")
        self.age = int(input("Enter the age of the person: "))
        self.job = input("Enter the job of the person: ")
        print("Person details added successfully!")

    def display(self):
        print("Name =",self.name,"Age =",self.age,"Job =",self.job)


class Book:
    def __init__(self):
        self.name = 0
        self.author = 0
        self.price = 0
        
    def add(self):
        self.name = input("Enter the name of the book: ")
        self.author = input("Enter the author's name: ")
        self.price = float(input("Enter the price of the book: "))
        print("Book added successfully")

    def display(self):
        print("Name =", self.name,"Author =", self.author,"Price =", self.price)


while True:
    print("1. Calculate area and perimeter of a circle")
    print("2. Input and display details of a person")
    print("3. Input and display details of books")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        c = Circle()
        c.radius1()
        c.area()

    elif choice == 2:
        p = Person()
        p.details()
        p.display()

    elif choice == 3:
        while True:
            print("\nBook Menu:")
            print("1. Add a new book")
            print("2. Display all books")
            print("3. Exit to main menu")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                b = Book()
                b.add()
                list1.append(b)
            elif ch == 2:
                if  list1:
                    for i in list1:
                        i.display()
                else:
                     print("No books to display.")
            elif ch == 3:
                break
            else:
                print("Default")

    elif choice == 4:
        break

    else:
        print("Default")
