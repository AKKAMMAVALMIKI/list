from symbol import lambdef_nocond


l=[30,40,50,15,19,46,90]
i=0
m1=0
m2=0
m3=0
while i<len(l):
    if l[i]>m1:
        m1=l[i]
    i=i+1
j=0
while j<len(l):
    if l[j]>m2 and l[j]!=m1:
        m2=l[j]
    j=j+1
k=0
while k<len(l):
    if l[k]>m3 and l[k]!=m2 and l[k]!=m1:
        m3=l[k]
    k=k+1
print(m1,m2,m3)