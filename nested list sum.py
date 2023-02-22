a=[1,2,[4,5],3,4]
i=0
s=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        sum=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j=j+1
    else:
        s=s+a[i]
    i=i+1
b.append(s)
b.append(sum)
print(b)
        