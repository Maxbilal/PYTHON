dict1 = {}
n1 = int(input("Enter the number of items for the first dictionary: "))
for _ in range(n1):
    key = input("Enter item name: ")
    value = input(f"Enter value for {key}: ")
    dict1[key] = value

dict2 = {}
n2 = int(input("Enter the number of items for the second dictionary: "))
for _ in range(n2):
    key = input("Enter item name: ")
    value = input(f"Enter value for {key}: ")
    dict2[key] = value

common_keys = set(dict1.keys()) & set(dict2.keys())
print("Common keys:", common_keys)
