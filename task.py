students_count = int(input('Please enter the number of students: '))
problems_count = int(input('Please enter the number of problems: '))
# Создаем словарь, где будем хранить данные учеников в виде Имя: [список оценок].
students_profile = {}
# Создаем словарь, где будем хранить суммарные баллы для каждой задачи в виде Номер задачи: Суммарный балл,
# инициализируем суммарные баллы нулями.
problems_rating = {i: 0 for i in range(problems_count)}
# Наполняем словарь именами
for i in range(students_count):
    students_profile[input('Please enter the name of student #{}: '.format(i))] = []
# Для каждого студента считываем все его оценки.
for student in students_profile:
    for i in range(problems_count):
        mark = int(input('Please enter {}\'s result for problem #{}: '.format(student, i)))
        # Проверяем корректность оценок, если все в порядке, то обновляем список оценок студента и рейтинг задачи.
        if mark in range(11):
            students_profile[student].append(mark)
            problems_rating[i] += mark
        else:
            print('Incorrect input!')
            exit(0)
# Создаем список, в котором будем хранить 3-ех (или меньше, если students_count < 3) лучших студентов.
top3_students = []
# 3 раза выбираем лучшего студента, добавляя каждого в top3_students.
for i in range(min(3, students_count)):
    max_student = None
    max_sum = -1
    for student in students_profile:
        if sum(students_profile[student]) > max_sum and student not in top3_students:
            max_student = student
            max_sum = sum(students_profile[student])
    top3_students.append(max_student)
# Красиво выводим top3_students.
print('Top-3 students are:', end=' ')
for student in top3_students:
    print(student, end=' ')
print()
# Аналогично тому, что выше, находим три самые сложные задачи и выводим их.
top3_problems = []
for i in range(min(3, problems_count)):
    max_problem = None
    max_rating = -1
    for problem in problems_rating:
        if problems_rating[problem] > max_rating and problem not in top3_problems:
            max_problem = problem
            max_rating = problems_rating[problem]
    top3_problems.append(max_problem)
print('Top-3 hardest problems are:', end=' ')
for problem in top3_problems:
    print(problem, end=' ')
print()

