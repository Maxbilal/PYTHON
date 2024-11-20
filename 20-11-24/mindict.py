dict1 = {}
n = int(input("Enter the number of items: "))

for _ in range(n):
    key = input("Enter item name: ")
    value = int(input("Enter quantity : "))
    dict1[key] = value
    
if dict1:
    minkey = min(dict1,key= dict1.get)
    print("items with minimum is:",minkey)
else:
    print("empty")