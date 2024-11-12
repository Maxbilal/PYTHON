num = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    a = input("Enter an element: ")
    num.append(a)

unique_num = []
seen = set()

for item in num:
    if item not in seen:
        unique_num.append(item)
        seen.add(item)

print("Original list:", num)
print("List without duplicates:", unique_num)
