"""
This module contains all the functions and classes to create and run a calculator application.
"""

import sys
import functools

from PyQt5 import QtGui, QtWidgets

import supertool.calc as calc


class MainApplication(QtWidgets.QMainWindow):
    """
    Instances of this class will be calculator applications.
    """
    def __init__(self):
        """
        Constructor of class MainApplication, here we initialize all the required attributes of the application, and add
        buttons to the numpad.
        """
        self.waiting_first_arg = True
        self.printing_second_arg = False
        self.first_arg = 0
        self.second_arg = 0
        super(MainApplication, self).__init__()
        self.ui = calc.Ui_MainWindow()
        self.ui.setupUi(self)

        for i in range(10):
            col = i % 3
            row = i // 3
            button = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(30)
            font.setBold(True)
            font.setWeight(75)
            button.setFont(font)
            button.setText(str(i))
            button.setObjectName("button_{}".format(i))
            button.clicked.connect(functools.partial(self.button_pressed, i))
            self.ui.grid_numbers.addWidget(button, row, col, 1, 1)

        self.ui.button_clear.clicked.connect(self.clear_pressed)
        self.ui.button_equal.clicked.connect(self.eq_pressed)
        self.ui.button_sum.clicked.connect(functools.partial(self.op_pressed, lambda x, y: x + y))
        self.ui.button_diff.clicked.connect(functools.partial(self.op_pressed, lambda x, y: x - y))
        self.ui.button_mul.clicked.connect(functools.partial(self.op_pressed, lambda x, y: x * y))
        self.ui.button_div.clicked.connect(functools.partial(self.op_pressed, lambda x, y: x // y if y != 0 else 'ERROR'))
        self.ui.button_pow.clicked.connect(functools.partial(self.op_pressed, lambda x, y: x ** y))

    def button_pressed(self, number):
        """This method is called when some button from the numpad is pressed. It adds the number which was pressed
        (argument number) to the lcd.

        :param number: Number which was pressed.
        :type number: int.
        """
        if not self.printing_second_arg:
            old = str(int(self.ui.lcd.value()))
            new = int(old + str(number))
            self.ui.lcd.display(new)
        else:
            self.ui.lcd.display(number)
            self.printing_second_arg = False
        self.number_string += str(number)

    def clear_pressed(self):
        """
        This method is called when the button AC is pressed. It clears the lcd.
        """
        self.ui.lcd.display(0)

    def op_pressed(self, operation):
        """This method is called when some button from the operations pad is pressed. It stores the operation and the
        first argument and initiates reading of the second argument.

        :param operation: The operation that will be applied later to the arguments.
        :type operation: function.
        """
        if self.waiting_first_arg:
            self.first_arg = int(self.ui.lcd.value())
            self.waiting_first_arg = False
            self.printing_second_arg = True
        self.operation = operation

    def eq_pressed(self):
        """
        This method is called when the button '=' is pressed. It stores the second argument and applies the stored
        before operation to the arguments, and then displays the result on the lcd.
        """
        if not self.waiting_first_arg:
            self.second_arg = int(self.ui.lcd.value())
            self.waiting_first_arg = True
            self.ui.lcd.display(self.operation(self.first_arg, self.second_arg))


def run_calculator():
    """
    This function runs an instance of class MainWindow (the calculator application).
    """
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()
    sys.exit(app.exec_())
