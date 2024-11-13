string = "Hello, World! 123"

newstring = ''.join(char for char in string if char.isalpha())

print("Cleaned string:", newstring)
