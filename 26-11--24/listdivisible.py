start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number: "))

divisible = []

for num in range(1,51):
    if num % 3 == 0 and num % 5 == 0:
        divisible.append(num)

print("Numbers divisible by both 3 and 5 in the given range:", divisible)
