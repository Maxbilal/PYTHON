
n = int(input("Enter the no of keyvalue pairs:"))

d ={}


for i in range(n):
    key = input("Enter the no of keys:")
    value = (input("Enter the no of values:"))
    d[key]= value
    
swapp = {value:key for key,value in d.items()}
print(d)
print(swapp)
    