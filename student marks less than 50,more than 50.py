m= [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
l= len(m)
i= 0
less_than50 = 0
more_than50 = 0
while i< l:
    marks=m[i]
    if marks< 50:
        less_than50 = less_than50 + 1
    else:
        more_than50 = more_than50 + 1
    i=i+1
print("Marks more than 50: " ,(more_than50))
print("Marks less than 50: " ,(less_than50))



# list1=[1, 3, 2] 
# print(list1 * 2)

# list=[9,5,6,3]
# print(list[2])

# list1=[3,2,5,7,3,6]
# list1.pop(3)
# print(list1)

# list1=[2, 33, 222, 14, 25]


# names = ['Amir', 'Bear', 'Charlton', 'Daman']
# print(names[-1][-1])



# n=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# sum=0
# # for element in n:
# #     sum=sum+1
# # print("Number of elements in the list: ", sum)
# while sum<len(n):
#     sum=sum+1
# print(sum)



# list1=[3, 4, 5, 20, 5, 25, 1, 3]
# print(list1.count(25))



