a=[2,7,8,4,5]
i=0
b=[]
e=[]
while i<len(a):
    c=a[i]**2
    e.append(c)
    d=c%10
    b.append(d)
    i=i+1
print(e)
print(b)