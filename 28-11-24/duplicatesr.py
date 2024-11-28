def fname(a):
    
     for item in num:
      if item not in seen:
        uniquenum.append(item)
        seen.add(item)
        
     print("Original list:", num)
     print("List without duplicates:", uniquenum)


num = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    a = input("Enter an element: ")
    num.append(a)

uniquenum = []
seen = set()

fname(num)
fname(uniquenum)

