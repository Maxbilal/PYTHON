set1  = set(map(int,input("Enter the first set:").split()))
set2  = set(map(int,input("Enter the second set:").split()))

result = set1.isdisjoint(set2)
print(result)