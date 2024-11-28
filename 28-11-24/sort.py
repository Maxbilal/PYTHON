def fname(num):
    num.sort()
    print(num)

n=int(input("Enter the range:"))
num=[]
for i in range(n):
    a = int(input("Enter the elements:"))
    num.append(a)
fname(num)