htuple = ('ii','gg','dd')
d =len(htuple)
f=0
for i in range(d):
    if  htuple[i]=='gg':
        print("index is ",i)
        f=1
        break
if f!=1:
    print("-1")