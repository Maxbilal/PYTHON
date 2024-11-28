def stringlist(strings):
    print("Your list of strings:", strings)

strings = []
b = int(input("Enter the range: "))
for i in range(b):
    n = input("Enter a string: ")
    strings.append(n)

stringlist(strings)
