a=[12300,1620,105,20,74820]
i=0
b=[]
while i<len(a):
    j=0
    k=""
    c=str(a[i])
    while j<len(c):
        if c[j]!="0":
            k=k+c[j]
        j=j+1
    b.append(k)
    i=i+1
print(b)


        


# while i<len(a):
#     if a[i]<100 or a[i]<1000:
#         c=a[i]//10
#     if a[i]>=1000 or a[i]<10000:
#         c=a[i]//10
#     if  a[i]>=10000 and a[i]<100000:
#         # c=a[i]//100
#         d=str(a[i])
#         if d[-1]==0 and d[-2]==0:
#             m=a[i]//100
#             h=m//10
#             c=int(h)
#         if d[-1]==0:
#             l=a[i]//10
#             c=int(l)
#     b.append(c)
#     i=i+1
# print(b)
            


    

