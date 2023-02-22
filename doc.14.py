# a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# a=[1,2,3]
# b=[2,3,5]
# i=0
# c=[]
# while i<len(a):
#     d=a[i],b[i]
#     c.append(list(d))
#     i=i+1
# print(c)


a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
max=a[i]
min=a[i]
while i<len(a):
    if a[i]>max:
        max=a[i]
    if a[i]<min:
        min=a[i]
    i=i+1
print((len(max),max))
print((len(min),min))           



