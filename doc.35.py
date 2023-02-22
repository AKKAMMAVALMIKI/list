a=[1234, 122, 1984, 19372, 100]
i=0
v=str(a[0])
m=v[0]
result=True
while i<len(a):
    b=str(a[i])
    if b[0]!=m:
        result=False
        break
    i=i+1
print(result)
    

# l=[1234, 122, 1984, 19372, 100]
# result=True
# d=str(l[0])
# i=0
# while i<len(l):
#     c=str(i)
#     if d[0]!=c[0]:
#         result=False
#         break
#     else:
#         continue
# print(result)
    