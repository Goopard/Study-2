"""
This module contains class WeatherUIMainWindow, which is a template user interface for a weather app from the module
weather_app.
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class WeatherUIMainWindow(object):
    """
    Instance of this class will be a template user interface for a weather app.
    """
    def setupUi(self, MainWindow):
        """This method sets up an UI in some window MainWindow.

        :param MainWindow: Window, where UI will be set up.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(823, 594)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Setting some spacers.
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 4, 1, 1)

        # Setting button '5-day forecast'.
        self.button_forecast = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_forecast.sizePolicy().hasHeightForWidth())
        self.button_forecast.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_forecast.setFont(font)
        self.button_forecast.setObjectName("button_forecast")
        self.gridLayout.addWidget(self.button_forecast, 2, 3, 1, 1)

        # Setting button 'Current weather'.
        self.button_weather = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_weather.sizePolicy().hasHeightForWidth())
        self.button_weather.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_weather.setFont(font)
        self.button_weather.setObjectName("button_weather")
        self.gridLayout.addWidget(self.button_weather, 2, 1, 1, 1)

        # Setting table widget, where all the resulting data will be displayed.
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.gridLayout.addWidget(self.table, 3, 0, 1, 5)

        # Setting a panel where the address will be typed in by the user.
        self.address = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.address.setFont(font)
        self.address.setObjectName("address")
        self.gridLayout.addWidget(self.address, 1, 0, 1, 5)

        # Setting a simple label with some explanation text.
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_forecast.setText(_translate("MainWindow", "5-day forecast"))
        self.button_weather.setText(_translate("MainWindow", "Current weather"))
        self.label.setText(_translate("MainWindow", "Please enter the address you wish to get weather for:"))

