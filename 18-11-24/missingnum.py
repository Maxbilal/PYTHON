n = int(input("Enter the value of n: "))
givennumbers = set(map(int, input("Enter the numbers: ").split()))

missingnumbers = sorted(set(range(1, n + 1)) - givennumbers)

if missingnumbers:
    print("The missing numbers are:",missingnumbers)  
else: 
    print("There are no missing numbers.")
