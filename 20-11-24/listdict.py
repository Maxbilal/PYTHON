keys = input("Enter the list of keys:").split(",")
values = input("Enter the list of values: ").split(",")

valuesint = []
for value in values:
    valuesint.append(int(value))

combined_dict = dict(zip(keys, valuesint))
print("Created dictionary:", combined_dict)
