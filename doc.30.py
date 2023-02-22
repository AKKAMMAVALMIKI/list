a=[2, -7, 5, -64, -14]
i=0
b=[]
cp=0
cn=0
while i<len(a):
    if a[i]<=0:
        cn=cn+1
    else:
        cp=cp+1
        b.append (a[i])
    i=i+1
print("negative",cn)
print("positive",cp)

