a=[[1, 2, 4], [2, 4, 4], [1, 2]]
i=0
b=[]
while i<len(a):
    j=0
    s=0
    while j<len(a[i]):
        s=s+a[j][i]
        j=j+1
    b.append(s)
    i=i+1
print(b)


