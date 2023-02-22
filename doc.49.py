a=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
i=0
while i<len(a):
    if a[i]=="f":
        b=i
    elif a[i]=="c":
        c=i
    elif a[i]=="k":
        d=i
    elif a[i]=="w":
        e=i
    i=i+1
print("last occarance of f in list is ",b)
print("last occarance of c in list is ",c)
print("last occarance of k in list is ",d)
print("last occarance of w in list is ",e)





