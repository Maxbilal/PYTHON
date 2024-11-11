num=[]

n = int(input("Enter the number of elements:"))

for i in range(n):
    a = int(input("The elements:"))
    num.append(a)
total_sum = sum(num)
print("The total sum is:",total_sum)