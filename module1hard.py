grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_list = list(students)
my_list.sort()
total = 0
for number in grades[0]: total += number
a = (total/len(grades[0]))
total_1 = 0
for number in grades[1]: total_1 += number
a_1 = (total_1/len(grades[1]))
total_2 = 0
for number in grades[2]: total_2 += number
a_2 = (total_2/len(grades[2]))
total_3 = 0
for number in grades[3]: total_3 += number
a_3 = (total_3/len(grades[3]))
total_4 = 0
for number in grades[4]: total_4 += number
a_4 = (total_4/len(grades[4]))
grades[0] = a
grades[1] = a_1
grades[2] = a_2
grades[3] = a_3
grades[4] = a_4
my_dict = dict(zip(my_list, grades))
print(my_dict)
