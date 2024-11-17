numbers = (3, 1, 4, 1, 5, 9, 2)

max_value = numbers[0]
min_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print("Original tuple:", numbers)
print("Maximum value:", max_value)
print("Minimum value:", min_value)
