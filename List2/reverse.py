num = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    a = input("Enter an element: ")
    num.append(a)
    num.reverse()

print("The reversed list is ",num)