original_tuple = (1, 2, 3, 4, 5)

swapped_tuple = original_tuple[-1:] + original_tuple[1:-1] + original_tuple[:1]

print("Original tuple:", original_tuple)
print("Tuple after swapping:", swapped_tuple)
