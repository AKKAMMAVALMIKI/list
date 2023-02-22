a=[1, 2, 2, 5, 8, 4, 4, 8]
i=0
b=[]
c=0
while i<len(a):
    if a[i] not in b :
        b.append (a[i])
        c=c+1
    i=i+1
print(c)

