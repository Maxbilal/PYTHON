num = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    a = input("Enter an element: ")
    num.append(a)

print("List of elements:", num)

element_to_find = input("Enter an element to find its index: ")

if element_to_find in num:
    index = num.index(element_to_find)
    print("The element index is :",index)
else:
    print("Element not in the list")
