a=['1', '2', '3', '4', '5', '6', '7', '8']
# a=["1","2","3"]
i=0
m=[]
while i<len(a)-1:
    b=a[i]+a[i+1]
    m.append(b)
    i=i+2
print(m)
