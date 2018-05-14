"""
This module contains class Ui_MainWindow, which is a template user interface for a calculator app from the module
calc_window.
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    """
    Instance of this class will be a template user interface for a calculator app.
    """
    def setupUi(self, MainWindow):
        """This method sets up an UI in some window MainWindow.

        :param MainWindow: Window, where UI will be set up.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 450)

        # Setting central widget and main grid layout, which will contain all other widgets in a MainWindow, allowing
        # user to resize a window properly.
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Setting grid layout for number pad.
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(260, 150, 441, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid_numbers = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid_numbers.setContentsMargins(0, 0, 0, 0)
        self.grid_numbers.setObjectName("grid_numbers")
        self.gridLayout.addWidget(self.gridLayoutWidget, 2, 1, 1, 1)

        # Setting grid layout for operations pad.
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(19, 150, 231, 391))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.gridLayoutWidget_2.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget_2.setSizePolicy(sizePolicy)
        self.grid_ops = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.grid_ops.setContentsMargins(0, 0, 0, 0)
        self.grid_ops.setObjectName("grid_ops")
        self.gridLayout.addWidget(self.gridLayoutWidget_2, 2, 0, 1, 1)

        # Setting an lcd, where the numbers will be displayed.
        self.lcd = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lcd.sizePolicy().hasHeightForWidth())
        self.lcd.setSizePolicy(sizePolicy)
        self.lcd.setFrameShape(QtWidgets.QFrame.Box)
        self.lcd.setObjectName("lcd")
        self.lcd.setDigitCount(12)
        self.lcd.setSmallDecimalPoint(True)
        self.gridLayout.addWidget(self.lcd, 0, 0, 1, 2)

        # Setting button '^'.
        self.button_pow = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pow.sizePolicy().hasHeightForWidth())
        self.button_pow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_pow.setFont(font)
        self.button_pow.setObjectName("button_pow")
        self.grid_ops.addWidget(self.button_pow, 0, 1, 1, 1)

        # Setting button AC.
        self.button_clear = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_clear.sizePolicy().hasHeightForWidth())
        self.button_clear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_clear.setFont(font)
        self.button_clear.setObjectName("button_clear")
        self.grid_ops.addWidget(self.button_clear, 0, 0, 1, 1)

        # Setting button '-'.
        self.button_diff = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_diff.sizePolicy().hasHeightForWidth())
        self.button_diff.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_diff.setFont(font)
        self.button_diff.setObjectName("button_diff")
        self.grid_ops.addWidget(self.button_diff, 1, 1, 1, 1)

        # Setting button '*'.
        self.button_mul = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_mul.sizePolicy().hasHeightForWidth())
        self.button_mul.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_mul.setFont(font)
        self.button_mul.setObjectName("button_mul")
        self.grid_ops.addWidget(self.button_mul, 2, 0, 1, 1)

        # Setting button '+'.
        self.button_sum = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_sum.sizePolicy().hasHeightForWidth())
        self.button_sum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_sum.setFont(font)
        self.button_sum.setObjectName("button_sum")
        self.grid_ops.addWidget(self.button_sum, 1, 0, 1, 1)

        # Setting button '//'.
        self.button_div = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_div.sizePolicy().hasHeightForWidth())
        self.button_div.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_div.setFont(font)
        self.button_div.setObjectName("button_div")
        self.grid_ops.addWidget(self.button_div, 2, 1, 1, 1)

        # Setting button '='.
        self.button_equal = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_equal.sizePolicy().hasHeightForWidth())
        self.button_equal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_equal.setFont(font)
        self.button_equal.setObjectName("button_equal")
        self.grid_ops.addWidget(self.button_equal, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 714, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.button_pow.setText(_translate("MainWindow", "^"))
        self.button_clear.setText(_translate("MainWindow", "AC"))
        self.button_diff.setText(_translate("MainWindow", "-"))
        self.button_mul.setText(_translate("MainWindow", "*"))
        self.button_sum.setText(_translate("MainWindow", "+"))
        self.button_div.setText(_translate("MainWindow", "//"))
        self.button_equal.setText(_translate("MainWindow", "="))
