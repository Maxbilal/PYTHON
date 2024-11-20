dict1 = {}
n = int(input("Enter the number of items: "))

for _ in range(n):
    key = input("Enter item name: ")
    value = int(input("Enter quantity: "))
    dict1[key] = value
    
dict2 = {}
n = int(input("Enter the number of items: "))

for _ in range(n):
    key = input("Enter item name: ")
    value = int(input("Enter quantity for: "))
    dict2[key] = value
    
combineddict = dict1.copy()
for key, value in dict2.items():
    if key in combineddict:
        combineddict[key] += value  
    else:
        combineddict[key] = value  

print("Combined dictionary:", combineddict)