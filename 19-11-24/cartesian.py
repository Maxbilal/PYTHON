set1  = set(map(int,input("Enter the first set:").split()))
set2  = set(input("Enter the second set:").split())

cartesianproduct = {(a, b) for a in set1 for b in set2}


print(cartesianproduct)
