set1  = set(map(int,input("Enter the first set:").split()))
set2  = set(map(int,input("Enter the second set:").split()))

target = set(map(int,input("Enter the target set:").split()))

if  set1 | set2:
    print("It is equal")
else:
    print("not equal")