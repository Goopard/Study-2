class SchoolMember:
    """This class embodies a member of a school."""

    def __init__(self, name: str, age: int):
        """This is a constructor of the class SchoolMember.

        :param name: Name of the school member.
        :type name: str.
        :param age: Age of the school member.
        :type age: int.
        """
        self.name = name
        self.age = age
        print('SchoolMember created: {}.'.format(name))

    def show(self):
        """This method prints the information about the school member.

        :return: None.
        """
        print('Name: {} Age: {}.'.format(self.name, self.age))


class Teacher(SchoolMember):
    """This is a child class of the class SchoolMember, which embodies a teacher."""

    def __init__(self, name: str, age: int, salary: int):
        """This is a constructor of the class Teacher.

        :param name: Name of the teacher.
        :type name: str.
        :param age: Age of the teacher.
        :type age: int.
        :param salary: Salary of teacher.
        :type salary: int.
        """
        super().__init__(name, age)
        self.salary = salary
        print('Teacher created: {}.'.format(name))

    def show(self):
        """This method prints the information about the teacher.

        :return: None.
        """
        print('Name: {} Age: {} Salary: {}'.format(self.name, self.age, self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        """This is a constructor of the class Student.

        :param name: Name of the Student.
        :type name: str.
        :param age: Age of the Student.
        :type age: int.
        :param marks: Marks of the student.
        :type marks: int.
        """
        super().__init__(name, age)
        self.marks = marks
        print('Student created: {}.'.format(name))

    def show(self):
        """This method prints the information about the student.

        :return: None.
        """
        print('Name: {} Age: {} Marks: {}'.format(self.name, self.age, self.marks))


persons = [Teacher("Mr.Poopybutthole", 40, 3000), Student("Morty", 16, 75)]
for person in persons:
    person.show()
