l1=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
l2=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
i=0
b=[]
while i<len(l1):
    b.append(l1[i]+l2[i])
    i=i+1
print(b)