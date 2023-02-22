n=[1,0,0,1,1]
a=len(n)
i=-1
k=0
sum=0
while i>=-a:
    b=n[i]*2**k
    sum=sum+b
    i=i-1
    k=k+1
print(sum)
