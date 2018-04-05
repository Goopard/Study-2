import operator


def top3_for_course(students_list: list, course: str) -> list:
    """This function calculates the top-3 best (with the highest rating) students from students_list for some course.

    :param students_list: The list of the students, should be a list of dicts where each dict represents a student and
    includes elements 'name', 'rate' and 'course'.
    :type students_list: list (of dicts).
    :param course: The course we want to find the best 3 students for.
    :type course: str.
    :return: list: The names (str) of the 3 best students for this course.
    """

    # To find the best 3 students, we create a list of tuples (name, rate) for every student on this course, and sort
    # this list by rate.

    sorted_rating = sorted(
                    [(student['name'], student['rate']) for student in students_list if student['course'] == course],
                    key=operator.itemgetter(1),
                    reverse=True
                    )

    # Since we need only the names of the 3 best students, we return only them.

    return [student[0] for student in sorted_rating][:3]


def set_of_courses(students_list: list) -> set:
    """This function finds out what courses do students from the students_list have and returns them as a set.

    :param students_list: The list of the students, should be a list of dicts where each dict represents a student and
    includes element 'course'.
    :type students_list: list (of dicts).
    :return: set.
    """
    return set(student['course'] for student in students_list)


def top3_for_all_courses(students_list: list) -> dict:
    """This function finds the best 3 students for each course and returns them as a dict of pairs COURSE: [Top-3
    students for the COURSE].

    :param students_list: The list of the students, should be a list of dicts where each dict represents a student and
    includes elements 'name', 'rate' and 'course'.
    :type students_list: list (of dicts).
    :return: dict.
    """
    return {course: top3_for_course(students_list, course) for course in set_of_courses(students_list)}


def print_all_top3(students_list: list):
    """This function is used to print the best 3 students for each course in a beautiful way.

    :param students_list: The list of the students, should be a list of dicts where each dict represents a student and
    includes elements 'name', 'rate' and 'course'.
    :type students_list: list (of dicts).
    :return: None.
    """
    all_top3 = top3_for_all_courses(students_list)

    def print_top3(course: str):
        print('Top-3 students for the course {} are: {}, {}, {}.'.format(course,
                                                                         all_top3[course][0],
                                                                         all_top3[course][1],
                                                                         all_top3[course][2]
                                                                         )
              )

    # We use map to apply function print_top3 to each course in set_of_courses. Since we need it applied,
    # not just stored, we have to cast the result to a list.

    list(map(print_top3, set_of_courses(students_list)))


students = [
            {'name': 'John', 'rate': 8, 'course': 'Python'},
            {'name': 'Andrew', 'rate': 9, 'course': 'Java'},
            {'name': 'Carl', 'rate': 11, 'course': 'Python'},
            {'name': 'Tony', 'rate': 5, 'course': 'Java'},
            {'name': 'Tom', 'rate': 7, 'course': 'Python'},
            {'name': 'Elizabeth', 'rate': 4, 'course': 'Python'},
            {'name': 'Kate', 'rate': 22, 'course': 'Java'},
            {'name': 'Mary', 'rate': 4, 'course': 'Java'},
            ]

print_all_top3(students)
