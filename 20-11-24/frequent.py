input_dict = {}
n = int(input("Enter the number of items: "))
for _ in range(n):
    key = input("Enter item name: ")
    value = input("Enter value for : ")
    input_dict[key] = value

values = list(input_dict.values())
mostvalue = max(set(values), key=values.count)
print("Most frequent value:", mostvalue)
