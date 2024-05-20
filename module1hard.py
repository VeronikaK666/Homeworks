students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
print(sorted(students_list))
grades=[[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
Aaron_grades = grades[0]
print('Aaron_grades =', Aaron_grades)
Aaron_grades_sum = sum(Aaron_grades)
print(sum(Aaron_grades))
Aaron_grades_avg = Aaron_grades_sum/len(Aaron_grades)
print(Aaron_grades_avg)
Bilbo_grades = grades[1]
print('Bilbo_grades =', Bilbo_grades)
Bilbo_grades_sum = sum(Bilbo_grades)
print(sum(Bilbo_grades))
Bilbo_grades_avg = Bilbo_grades_sum/len(Bilbo_grades)
print(Bilbo_grades_avg)
Johnny_grades = grades[2]
print('Johnny_grades =', Johnny_grades)
Johnny_grades_sum = sum(Johnny_grades)
print(sum(Johnny_grades))
Johnny_grades_avg = Johnny_grades_sum/len(Johnny_grades)
print(Johnny_grades_avg)
Khendrik_grades = grades[3]
print('Khendrik_grades =', Khendrik_grades)
Khendrik_grades_sum = sum(Khendrik_grades)
print(sum(Khendrik_grades))
Khendrik_grades_avg = Khendrik_grades_sum/len(Khendrik_grades)
print(Khendrik_grades_avg)
Steve_grades = grades[4]
print('Steve_grades =', Steve_grades)
Steve_grades_sum = sum(Steve_grades)
print(sum(Steve_grades))
Steve_grades_avg = Steve_grades_sum/len(Steve_grades)
print(Steve_grades_avg)
Average_grades = {sorted(students_list)[0]: Aaron_grades_avg, sorted(students_list)[1]: Bilbo_grades_avg,
                  sorted(students_list)[2]: Johnny_grades_avg, sorted(students_list)[3]: Khendrik_grades_avg,
                  sorted(students_list)[4]: Steve_grades_avg}
print(Average_grades)