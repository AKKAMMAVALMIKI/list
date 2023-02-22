a="https://www.w3resource.com/python-exercises/list/"
b=['.com', '.edu', '.tv']
i=0
c=0
while i<len(b):
    if b[i]in a:
        c=c+1
    i=i+1        
if c>=1:
    print("true")
else:
    print("no")
    