a=["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
c=[]
i=0
b=[]
while i<len(a):
    d=a.count(a[i])
    if a[i] not in b:
        v=a[i],d
        b.append(a[i])
        c.append(list(v))
    i=i+1
print(c)


