a=['Red', 'Maroon', 'Yellow', 'Olive']
i=0
b=[]
while i<len(a):
    j=0
    d=[]
    while j<len(a[i]):
        d.append(a[i][j])
        j=j+1
    b.append(d)    
    i=i+1
print(b)

