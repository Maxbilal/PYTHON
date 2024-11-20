inputdict = {}
n = int(input("Enter the number of items: "))
for _ in range(n):
    key = input("Enter item name: ")
    value = input(f"Enter value: ")
    inputdict[key] = value.split(',')  

reversed_dict = {}
for key, value in inputdict.items():
    for v in value:
        if v not in reversed_dict:
            reversed_dict[v] = [key]
        else:
            reversed_dict[v].append(key)

print("Reversed dictionary:", reversed_dict)
