print("Enter the dictionary :")
user_input = input()
my_dict = {}

for item in user_input.split(','):
    key, value = item.split(':')
    my_dict[key.strip()] = int(value.strip())

value_counts = {}
for value in my_dict.values():
    value_counts[value] = value_counts.get(value, 0) + 1

print("Value counts:", value_counts)
