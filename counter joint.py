students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# length = len(students) # kyunki dono ki same length hai toh jiski bhi length le sakte ho
marks = [10, 20, 56, 45, 36, 20]
length = len(students)
counter = 0
while counter < length:
    print(students[counter] +str(marks[counter]))
    counter+=1