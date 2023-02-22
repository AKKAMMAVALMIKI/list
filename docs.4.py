a=[6,1,3,5,6,3,1]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
print(b)
j=0
product=1
while j<len(b):
    product=product*b[j]
    j=j+1
print(product)    



