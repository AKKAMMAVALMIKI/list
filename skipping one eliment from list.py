a=[1,5,"ram",6,7]
i=0
b=[]
while i<len(a):
    if a[i]!="ram":
        b.append(a[i])
    i=i+1
print(b)