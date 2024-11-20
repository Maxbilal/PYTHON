print("Enter the first dictionary :")
dict1 = {}
for item in input().split(','):
    key, value = item.split(':')
    dict1[key.strip()] = int(value.strip())

print("Enter the second dictionary :")
dict2 = {}
for item in input().split(','):
    key, value = item.split(':')
    dict2[key.strip()] = int(value.strip())

merged_dict = dict1.copy()

for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key] = max(merged_dict[key], value)  
    else:
        merged_dict[key] = value  

print("Merged dictionary:", merged_dict)
