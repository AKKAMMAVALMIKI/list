n=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
l=len(n)
count_c=0
count_l=0
count_d=0
i=0
while i<l:
    if n[i]>=10000000:
        count_c=count_c+1
    elif n[i]>=100000:
        count_l=count_l+1
    else:
        count_d=count_d+1
    i=i+1
print(count_c)
print(count_l)
print(count_d)


# a=[1,2,[4,5],3,4]
# i=0
# sum=0
# b=[]
# while i<len(a):
#     sum=sum+a[i]
#     b.append(sum)

#     # j=0
#     # c=[]
#     # c=str(a[i])
#     # while j<len(c):
#     #     k=int(c[j])
#     #     j+=1  
#     i+=1
# print(b)
