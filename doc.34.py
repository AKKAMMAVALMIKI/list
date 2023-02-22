a= [34.67, 12, -94.89, 'Python', 0, 'C#']
b=[]
i=0
while i<len(a):
    if type(a[i])==int and a[i]>=0:
            b.append(a[i])
    i+=1
print(b)
