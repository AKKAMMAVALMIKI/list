a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
i=0
c=[]
while i<3:
    j=i
    k=[]
    while j<len(a):
        k.append(a[j])
        j=j+3
    i=i+1
    c.append(k)
    
print(c)