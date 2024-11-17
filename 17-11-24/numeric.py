my_tuple = (1, 2, 3, 'a', 4, 'b', 5)

total_sum = sum(item for item in my_tuple if isinstance(item, (int, float)))

print("Sum of numeric values in the tuple:", total_sum)
