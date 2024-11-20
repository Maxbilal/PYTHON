dict1 = {}
n = int(input("Enter the number of items: "))

for _ in range(n):
    key = input("Enter item name: ")
    value = int(input("Enter quantity for: "))
    dict1[key] = value
    
threshold = int(input("Enter the threshold value: "))

fdict = {}
for key, value in dict1.items():
    if value >= threshold:
        fdict[key] = value

print("Filtered dictionary:", fdict)