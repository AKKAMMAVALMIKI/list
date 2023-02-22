# n=int(input("enter the number"))
# i=0
# while i<n:
#     k=1
#     while k<=n-i:
#         print(" ",end="")
#         k=k+1
#     j=0
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     i=i+2 
#     print()
# a=[1,67,8,0]
# a.sort(reverse=True)
# print(a)


# a=[1,2,3,4]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# avg=sum/len(a)
# print(avg)


# a=[123,234,135]
# i=0
# b=[]
# while i<len(a):
#     j=a[i]
#     sum=0
#     while j>0:
#         c=j%10
#         sum=sum+c
#         j=j//10
#     i=i+1
#     b.append(sum)
# print(b)

# numb = [2, 3, 5,3, 7, 8,2,2]
# j=0
# sum=0
# for i in numb:
#     j=j+1
#     sum+=i
# mean=sum/j
# print("mean is",mean)
# for i in range(j-1):
#     for k in range(j-1):
#         if numb[k]>numb[k+1]:
#             numb[k],numb[k+1]=numb[k+1],numb[k]
# if j% 2 == 0:
#     median1 = numb[j//2]
#     median2 = numb[j//2 - 1]
#     median = (median1 + median2)/2
# else:
#     median = numb[j//2]
# print("the median of the list is",median)
# count=1
# mode=0
# b=[]
# for i in numb:
#     c=numb.count(i)
#     if i not in b:
#         b.append(i)
#         if c>count:
#             count=c
#             mode=i
#             print(mode)

# print("mode of the list is",mode)
# a=[7,8,4,6,51,5]
# b=[7,8,9,10,11,11,6]
# m=0
# for l in a:
#     m=m+1
# n=0
# for k in b:
#     n=n+1
# for h in range(m-1):
#     for e in range(m-1):
#         if a[e]>a[e+1]:
#             a[e],a[e+1]=a[e+1],a[e]
# for r in range(n-1):
#     for v in range(n-1):
#         if b[v]>b[v+1]:
#             b[v],b[v+1]=b[v+1],b[v]
# union=[]
# inter=[]
# for i in a:
#     for j in b:
#         if j not in union:
#             union.append(j)
#         if i not in union:
#             union.append(i)
#         if i==j:
#             inter.append(i)
# print(union)
# print(inter)

# a=[1,2,3,5,7]
# b=[4,7,9,11,9]
# c=a+b
# j=0
# for i in c:
#     j=j+1
# for k in range(j-1):
#     for l in range(j-1):
#         if c[l]>c[l+1]:
#             c[l],c[l+1]=c[l+1],c[l]
# print(c)
# if j% 2 == 0:
#     median1 = c[j//2]
#     median2 = c[j//2 - 1]
#     median = (median1 + median2)/2
# else:
#     median = c[j//2]
# print("the median of the list is",median)

# a=[2,3,5,6]
# b=a[0:3]
# print(b)

# a=[1,5,"ram",6,7]
# i=0
# b=[]
# while i<len(a):
#     if a[i]!="ram":
#         b.append(a[i])
#     i=i+1
# print(b)

# a=[1234,5432,147]
# i=0
# b=[]
# while i<len(a):
#     j=a[i]
#     sum=0
#     while j>0:
#         c=j%10
#         sum=sum+c
#         j=j//10
#     i=i+1
#     b.append(sum)
# print(b)

# a=[1,2,[4,5],8,[2,5]]
# print(a[0],a[2][0],a[3],a[4][-1])

a=[1,2,[4,5],3,4]
i=0
s=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        sum=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j=j+1
    else:
        s=s+a[i]
    i=i+1
b.append(s)
b.append(sum)
print(b)
# a=int(input("enter the number")) 
i=0
while i<100:
    i=i+1
    if i%7==0:
        print(i)

    

# i=0
# b=[]
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[0]):
#         sum+=a[i]
#         j+=1
#     i+=1
# print(sum)

    # j=0
    # sum=0
    # while j<(a[i]):
    #     if type(a[i][j])==list:
    #         sum=sum+a[i][j]
    #         b.append(sum)
    #     else:
    #         sum=sum+a[i]    
    #     j=j+1
    # i=i+1
    # print(b)

