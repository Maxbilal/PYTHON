num=[]

n = int(input("Enter the number of elements:"))

for i in range(n):
    a = int(input("Enter the elements:"))
    num.append(a)
print("List:",num)
largest_num = max(num)
print("The largest number is:",largest_num)