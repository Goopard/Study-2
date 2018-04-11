class Matrix:
    """This class embodies a matrix. To create a matrix, you can use one of these options:
    1) Matrix(lines), where lines is a list of lines of the matrix (which are lists of ints) i.eg:
        >>>Matrix([[1, 2], [3, 4]])
        [1, 2]
        [3, 4]
        Notice that if lines in lines are not equal in length, the width of matrix will be the length of the longest
        line, and all undefined missing elements of the matrix will be initialized with zeros i.eg:
        >>>Matrix([[1, 2], [3]])
        [1, 2]
        [3, 0]
    2) Matrix(N, M), where N and M are positive integers will create a NxM matrix with random elements with values from
    0 to 9 i.eg.:
        >>>Matrix(2, 2)
        [5, 3]
        [1, 9]
    3) Matrix(N, M, empty=True), where N and M are positive integers will create a NxM zero matrix i.eg:
        >>>Matrix(2, 2, empty=True)
        [0, 0]
        [0, 0]

    To operate with matrices, you can use those operators:
    1) '==' to find out if matrices are equal.
    2) '!=' to find out if matrices are unequal.
    3) '+' to find the sum of two matrices.
    4) '-' to find the difference between two matrices.
    5) '*' to multiply a matrix on an integer number or another matrix i.eg.:
        >>>M = Matrix([[1, 1], [1, 1]])
        >>>M * 2
        [2, 2]
        [2, 2]
        >>>N = Matrix([[2, 2], [2, 2]])
        >>M * N
        [4, 4]
        [4, 4]
    """
    def __init__(self, lines: list, width=None, empty=False):
        """This is a constructor of class Matrix.

        :param lines: Either list of lines of matrix or its height.
        :type lines: list of lists of ints or int.
        :param: width: Either None if lines = list of lines of matrix or width of matrix.
        :type width: int.
        :param empty: If lines contains only height and width of the matrix, this argument will define whether random or
        zero matrix will be created.
        :type empty: bool.
        """

        # First we check if we are given only the size (height and width, both positive ints) of matrix or not.

        if isinstance(lines, int) and width is not None:
            self.height = lines
            self.width = width
            import random
            random.seed()
            self.__lines = [[random.randint(0, 9) if not empty else 0 for i in range(self.width)]
                            for j in range(self.height)]
        elif isinstance(lines, list) and width is None:

            # If not, than we have to check if our lines are correct. If not, we raise some exceptions.

            for line in lines:
                if isinstance(line, list):
                    for elem in line:
                        if not isinstance(elem, int):
                            raise ValueError('Elements of matrix have to be integer numbers!')
                else:
                    raise ValueError('Lines of matrix have to be lists!')

            # If lines are correct, we can go on and initialize our matrix.

            self.height = len(lines)
            self.width = max(len(line) for line in lines)
            self.__lines = lines

            # In the end, we fill the missing elements of the matrix with zeros.

            for line in self.__lines:
                if len(line) < self.width:
                    for i in range(self.width - len(line)):
                        line.append(0)
        else:
            raise ValueError('incorrect initialisation of an instance of class Matrix')

    def __getitem__(self, index: int) -> list:
        """This method allows us to use operator [] for our matrix by accessing its lines.

        :param index: The number of the line we want to access.
        :type index: int.
        :return: list: The line number index.
        """
        if index < self.width:
            return self.__lines[index]
        else:
            raise IndexError('matrix index out of range')

    def __eq__(self, other) -> bool:
        """This method allows us to find out if two matrices are equal

        :param other: Any object.
        :type other: Any.
        :return bool.
        """
        if not isinstance(other, Matrix):
            return False
        if self.height == other.height and self.width == other.width:
            for i in range(self.height):
                if self[i] != other[i]:
                    return False
        else:
            return False
        return True

    def __ne__(self, other):
        """This method allows us to find out if two matrices are not equal

        :param other: Any object.
        :type other: Any.
        :return bool.
        """
        return not self.__eq__(other)

    def __add__(self, other):
        """This method allows us to find the sum of two matrices.

        :param other: Second matrix.
        :type other: Matrix.
        :return: Matrix.
        """
        result = self
        for i in range(self.height):
            for j in range(self.width):
                result[i][j] += other[i][j]
        return result

    def __sub__(self, other):
        """This method allows us to find the difference between two matrices.

        :param other: Second matrix.
        :type other: Matrix.
        :return: Matrix.
        """
        result = self
        for i in range(self.height):
            for j in range(self.width):
                result[i][j] -= other[i][j]
        return result

    def __mul__(self, other):
        """This method allows us to find the multiplication of two matrices or a multiplication of a matrix and int.

        :param other: Second Matrix or an int.
        :type other: Matrix or int.
        :return: Matrix.
        """
        if isinstance(other, int):
            result = self
            for i in range(self.width):
                for j in range(self.height):
                    result[i][j] *= other
        elif self.width == other.height:
            result = Matrix(self.height, other.width, empty=True)
            for i in range(result.height):
                for j in range(result.width):
                    for r in range(self.width):
                        result[i][j] += self[i][r] * other[r][j]
        else:
            raise ValueError('multiplication of matrices with unequal width of the first matrix and height of the '
                             'second matrix is undefined')
        return result

    def __str__(self) -> str:
        """This method allows us to print a matrix.

        :return: str.
        """
        str_matrix = ''
        for line in self.__lines:
            str_matrix += str(line) + '\n'
        return str_matrix

    def is_square(self) -> bool:
        """This method allows us to find out if matrix is squared.

        :return: bool.
        """
        return self.width == self.height

    def is_symmetrical(self) -> bool:
        """This method allows us to find out if matrix is symmetrical.

        :return: bool.
        """
        if self.is_square():
            for i in range(self.height):
                for j in range(self.width):
                    if self[i][j] != self[j][i]:
                        return False
            return True
        else:
            return False

    def transposed(self):
        """This method creates the transposed version of the matrix.

        :return: Matrix.
        """
        transposed_lines = [[lines[i] for lines in self.__lines] for i in range(self.width)]
        return Matrix(transposed_lines)


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m)
n = Matrix([[1, 1, 1], [1, 1, 1]])
print(n)
print(n + m)
print(n * m)
n = Matrix(4, 4)
print(n)
print(n.transposed())
print(n.is_square())
print(n.is_symmetrical())
