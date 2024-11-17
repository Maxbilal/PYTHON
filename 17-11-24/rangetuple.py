my_tuple = tuple(range(1, 11))  

even_numbers = tuple(num for num in my_tuple if num % 2 == 0)

print("Tuple of even numbers:", even_numbers)
