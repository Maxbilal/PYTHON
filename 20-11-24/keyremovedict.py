dict1 = {}
n = int(input("Enter the number of items: "))

for _ in range(n):
    key = input("Enter item name: ")
    value = int(input("Enter quantity for: "))
    dict1[key] = value
    
keys_to_remove = []
for key, value in dict1.items():
    if value % 2 == 0:
        keys_to_remove.append(key)

for key in keys_to_remove:
    del dict1[key]

# Display the modified dictionary
print("Modified dictionary:", dict1)