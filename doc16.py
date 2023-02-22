a=[1,2,3,4,5,6,7,8,9,10]
i=0
b=[]
while i<len(a)-1:
    c=a[i+1]-a[i]
    b.append(c)
    i=i+1
print(b)