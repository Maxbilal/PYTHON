def index():
 num = []

 n = int(input("Enter the number of elements: "))

 for i in range(n):
    a = input("Enter an element: ")
    num.append(a)

 print("List of elements:", num)

 elementfind = input("Enter an element to find its index: ")

 if elementfind in num:
    index = num.index(elementfind)
    print("The element index is :",index)
 else:
    print("Element not in the list")
    
index()