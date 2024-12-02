numbers = list(map(int, input("Enter a list of numbers s: ").split()))
oddnumbers = []
for x in numbers:
    if (lambda x: x % 2 != 0)(x):
        oddnumbers.append(x)
print(oddnumbers)
