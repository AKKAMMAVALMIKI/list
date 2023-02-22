a=int(input("enter the number"))
i=0
while i<a:
    l=a%100000
    tent=a%10000
    onet=a%1000
    h=a%100
    t=a%10
    i=i+1
print(a-l,"+",l-tent,"+",tent-onet,"+",onet-h,"+",h-t,"+",t)
    


