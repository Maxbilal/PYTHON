tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

commonelements = tuple(set(tuple1) & set(tuple2))

print("Common elements:", commonelements)
