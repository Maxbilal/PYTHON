strings = input("Enter a list of strings (comma-separated): ").split(",")
grouped_dict = {}
for string in strings:
    length = len(string)
    if length not in grouped_dict:
        grouped_dict[length] = []
    grouped_dict[length].append(string)
print("Grouped strings by their lengths:", grouped_dict)
