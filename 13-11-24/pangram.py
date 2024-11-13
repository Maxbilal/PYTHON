sentence = "The quick brown fox jumps over the lazy dog"

alphabet = "abcdefghijklmnopqrstuvwxyz"

pangram = all(letter in sentence.lower() for letter in alphabet)

if pangram:
    print("The string is a pangram.") 
else:
    ("The string is not a pangram.")
