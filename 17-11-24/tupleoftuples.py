ttuples = ((1, 2), (3, 4), (1, 2), (5, 6), (3, 4))

seen = []
utuples = tuple(inner for inner in ttuples if inner not in seen and not seen.append(inner))

print("Original tuple of tuples:", ttuples)
print("Tuple of tuples without duplicates:", utuples)
