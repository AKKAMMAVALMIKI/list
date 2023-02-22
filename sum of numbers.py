a=[1234,5432,147]
i=0
b=[]
while i<len(a):
    j=a[i]
    sum=0
    while j>0:
        c=j%10
        sum=sum+c
        j=j//10
    i=i+1
    b.append(sum)
print(b)