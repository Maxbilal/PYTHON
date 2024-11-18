numbers = input("Enter a list of integers : ").split()

numbers = list(map(int, numbers))  

counts = {num: numbers.count(num) for num in set(numbers)}

print("Count of each unique number:")
for num, count in counts.items():
    print(f"{num}: {count}")
