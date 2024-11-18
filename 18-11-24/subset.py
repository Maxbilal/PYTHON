set1  = set(input("Enter the first set:").split())
set2  = set(input("Enter the second set:").split())

if set2.issubset(set1):
    print("Its a subset",set2)
else:
    print("its not a subset",set1)

