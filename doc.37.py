a=[1, 2, 3, 4, 5, 6]
i=0
b=[]
while i<len(a)-1:
    c=a[i],a[i+1]
    b.append(list(c))
    i=i+1
print(b)     
