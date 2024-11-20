inputdict = {}
n = int(input("Enter the number of items: "))
for _ in range(n):
    key = input("Enter item name: ")
    value = input(f"Enter value : ")
    inputdict[key] = value

letter = input("Enter the letter to search for: ").lower()

matching_keys = [key for key in inputdict if key.lower().startswith(letter)]

print("Keys that start with the letter", letter, ":", matching_keys)
