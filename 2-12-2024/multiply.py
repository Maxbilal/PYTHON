m = lambda x: x * 2

numbers = list(map(int, input("Enter a list of numbers: ").split()))

d = list(map(m, numbers))

print("List after multiplying each element by 2:" ,d)
