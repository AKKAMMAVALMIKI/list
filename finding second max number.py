l=[50,40,23,70,56,12,5,10,7]
i=0
max1=0
max2=0
while i<len(l):
    if l[i]>max1:
        max1=l[i]
    i=i+1
j=0
while j<len(l):
    if l[j]>max2 and l[j]!=max1:
        max2=l[j]
    j=j+1
print(max2)