idict = {}
n = int(input("Enter the number of key-value pairs: "))

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    idict[key] = value

target = input("Enter the value to find keys for: ")

keyvalue = []
for key, value in idict.items():
    if value == target:
        keyvalue.append(key)

if keyvalue:
    print("Keys with value ",target)
    for key in keyvalue:
        print(key)
else:
    print("No keys found with value ",target)
