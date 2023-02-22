n=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
l=len(n)
even_sum=0
odd_sum=0
count_even=0
count_odd=0
i=0
while i<l:
    if n[i]%2==0:
        even_sum=even_sum+n[i]
        count_even=count_even+1
    else:
        odd_sum=odd_sum+n[i]
        count_odd=count_odd+1
    i=i+1
avg_even=even_sum/count_even
avg_odd=odd_sum/count_odd
print(avg_even)
print(avg_odd)
print(count_even)
print(count_odd)
print(even_sum)
print(odd_sum)