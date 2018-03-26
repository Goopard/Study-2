students_count = int(input('Please enter the number of students: '))
problems_count = int(input('Please enter the number of problems: '))
students_profile = []
for i in range(students_count):
    students_profile.append([input('Please enter the name of student #{}: '.format(i)), []])
for i in range(students_count):
    for j in range(problems_count):
        students_profile[i][1].append(int(input('Please enter {}\'s result for problem #{}: '.format(students_profile[i][0], j))))
for i in range(students_count - 1):
    for j in range(i + 1, students_count):
        if sum(students_profile[i][1]) < sum(students_profile[j][1]):
            temp = students_profile[i]
            students_profile[i] = students_profile[j]
            students_profile[j] = temp
print('Top-3 students are: {}, {}, {}'.format(students_profile[0][0], students_profile[1][0], students_profile[2][0]))
problems_rating = []
for i in range(problems_count):
    problems_rating.append([i])
    rating = 0
    for j in range(students_count):
        rating += students_profile[j][1][i]
    problems_rating[i].append(rating)
for i in range(problems_count - 1):
    for j in range(i + 1, problems_count):
        if problems_rating[i][1] > problems_rating[j][1]:
            temp = problems_rating[i]
            problems_rating[i] = problems_rating[j]
            problems_rating[j] = temp
print('Top-3 hardest problems are: {}, {}, {}'.format(problems_rating[0][0], problems_rating[1][0], problems_rating[2][0]))

