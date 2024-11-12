num = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    a = input("Enter an element: ")
    num.append(a)

occurrences = {}

for item in num:
    if item in occurrences:
        occurrences[item] += 1
    else:
        occurrences[item] = 1

print("Occurrences of each element:")
for element, count in occurrences.items():
    print(f"{element}: {count}")
