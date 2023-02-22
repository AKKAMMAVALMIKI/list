# n=[19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# a=[]
# i=0
# count=0
# l=len(n)
# while i<l:
#     if count(n[i])>0:
#         count=count(n[i])+1
#     i=i+1
# print(a)



a=[19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
c=[]
i=0
while i<len(a):
    d=a.count(a[i])
    if d>1:
      if c.count(a[i])==0:
        c.append(a[i])
    i=i+1
print(c)



# a=[1,2,3]
# b=[3,4,5]
# i=0
# d=[]
# while i<len(a):
#   c=a[i]+b[i]
#   d.append(c)
#   i=i+1
# print(d)  

