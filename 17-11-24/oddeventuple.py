my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)

even_indexed = tuple(my_tuple[i] for i in range(len(my_tuple)) if i % 2 == 0)
odd_indexed = tuple(my_tuple[i] for i in range(len(my_tuple)) if i % 2 != 0)

print("Even-indexed elements:", even_indexed)
print("Odd-indexed elements:", odd_indexed)
