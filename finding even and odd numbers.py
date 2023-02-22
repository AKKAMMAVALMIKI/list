# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# even_count, odd_count = 0, 0
# for num in elements:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print("Even numbers in the list: ", even_count)
# print("Odd numbers in the list: ", odd_count)




n=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
l=len(n)
count_even=0
count_odd=0
i=0
while i<l:
    if n[i]%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
    i=i+1
print(count_even)
print(count_odd)
        