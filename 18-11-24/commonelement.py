set1  = set(input("Enter the first set:").split())
set2  = set(input("Enter the second set:").split())
set3  = set(input("Enter the third set:").split())

commonset = set1 & set2 & set3

if commonset:
    print("The common elements among the three sets are :",commonset)
else:
    print("There is no common element")