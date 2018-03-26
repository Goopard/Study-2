students_count = int(input('Please enter the number of students: '))
problems_count = int(input('Please enter the number of problems: '))
students_profile = []
for i in range(students_count):
    students_profile.append([input('Please enter the name of student #{}: '.format(i)), []])
for i in range(students_count):
    for j in range(problems_count):
        mark = int(input('Please enter {}\'s result for problem #{}: '.format(students_profile[i][0], j)))
        if (mark >= 0) & (mark <= 10):
            students_profile[i][1].append(mark)
        else:
            print('Incorrect input!')
            exit(0)
for i in range(students_count - 1):
    for j in range(i + 1, students_count):
        if sum(students_profile[i][1]) < sum(students_profile[j][1]):
            temp = students_profile[i]
            students_profile[i] = students_profile[j]
            students_profile[j] = temp
top3 = []
for i in range(min(students_count, 3)):
    top3.append(students_profile[i][0])
print('Top-3 students are:', end=' ')
for name in top3:
    print(name, end=', ')
print()
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
top3 = []
for i in range(min(problems_count, 3)):
    top3.append(problems_rating[i][0])
print('Top-3 hardest problems are:', end=' ')
for problem in top3:
    print(problem, end=', ')
print()


