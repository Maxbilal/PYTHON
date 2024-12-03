class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity = quantity

    def change_price(self, price):
        self.price = price

    def display(self):
        print("Item=",self.name, "Price =", self.price, "Quantity=", self.quantity)

name = input("Enter the name of the item: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
item = Item(name, price, quantity)
item.display()

newquantity = int(input("Enter new quantity: "))
newprice = float(input("Enter new price: "))
item.update_quantity(newquantity)
item.change_price(newprice)
item.display()
