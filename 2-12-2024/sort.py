sort = lambda x: x[1]

tuples = eval(input("Enter a list of tuples: "))

s = sorted(tuples, key=sort)

print("List of tuples sorted by the second element: ",s)
