a=[12,67,98,34]
b=[]
i=0
while i<len(a):
    sum=0
    j=0
    n=str(a[i])
    while j<len(n):
        sum+=int(n[j])
        j=j+1
    b.append(sum)
    i=i+1
print(b)