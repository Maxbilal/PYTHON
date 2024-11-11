num=[]

n = int(input("Enter the number of elements:"))

for i in range(n):
    a = int(input("Enter the elements:"))
    num.append(a)
    
target = int(input("The number your searching:"))

if target in num:
    print("{target} is in the list")
else:
    print("{target}is not in the list")