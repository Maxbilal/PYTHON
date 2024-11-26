string = input("Enter a string: ")

uniquevowels = set()

for char in string.lower():
    if char in "aeiou":
        uniquevowels.add(char)

print("Unique vowels found in the string:", uniquevowels)
