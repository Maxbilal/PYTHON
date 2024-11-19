names = input("Enter names separated by spaces: ").split()

seen = set()
duplicates = set()

for name in names:
    if name in seen:
        duplicates.add(name)
    else:
        seen.add(name)

if duplicates:
    print(f"Duplicate names: {duplicates}")
else:
    print("No duplicate names found.")
