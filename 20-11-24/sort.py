input_dict = {}
n = int(input("Enter the number of items: "))
for _ in range(n):
    key = input("Enter item name: ")
    value = int(input(f"Enter value for {key}: "))
    input_dict[key] = value

sorted_items = []
for key, value in input_dict.items():
    sorted_items.append((key, value))

for i in range(len(sorted_items)):
    for j in range(i + 1, len(sorted_items)):
        if sorted_items[i][1] > sorted_items[j][1]:
            sorted_items[i], sorted_items[j] = sorted_items[j], sorted_items[i]

sorted_dict = {}
for key, value in sorted_items:
    sorted_dict[key] = value

print("Dictionary sorted by values:", sorted_dict)
