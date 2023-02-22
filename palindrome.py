# # initializing list
# test_list = ['n','i','t','i','n']
# # Reversing the list
# reverse = test_list[::-1]
# # checking if palindrome
# res = test_list == reverse
# # printing result
# if(res):
#  print("Haan! palindrome hai")
# else:
#  print("Nahi! palindrome nahi h")

a=["n","i","t","i","n"]
b=[]
i=-1
while i>=-len(a):
    b.append(a[i])
    i=i-1
print(b)
if a==b:
    print("palindrome")
else:
    print("not")        