a=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
i=0
b=[]
while i<len(a):
    c=a.count(a[i])
    if c>3:
        if a[i] not in b:
            b.append(a[i])
    i=i+1
print(b)            
