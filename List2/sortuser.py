num=[]

n = int(input("Enter the number of elements:"))

for i in range(n):
    a = int(input("The elements:"))
    num.append(a)
num.sort()
print("The numbers in ascending order:",num)