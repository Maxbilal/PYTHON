set1  = set(map(int,input("Enter the first set:").split()))
set2  = set(map(int,input("Enter the second set:").split()))

set3 = set1 - set2
print(set3)