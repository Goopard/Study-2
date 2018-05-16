"""
This module contains class SimilarFilesUIMainWindow, which is a template user interface for a similar files finder app
from the module sff_app.
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class SimilarFilesUIMainWindow(object):
    """
    Instance of this class will be a template user interface for a similar files finder app.
    """
    def setupUi(self, MainWindow):
        """This method sets up an UI in some window MainWindow.

        :param MainWindow: Window, where UI will be set up.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 730)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Setting tree widget, where the chains of similar files will be displayed.
        self.tree = QtWidgets.QTreeWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tree.setFont(font)
        self.tree.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tree.setColumnCount(1)
        self.tree.setObjectName("tree")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.tree.sizePolicy().hasHeightForWidth())
        self.tree.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.tree, 2, 0, 1, 2)

        # Setting a simple label with some explanation text.
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 981, 51))
        self.label.setObjectName("label")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        # Setting a search button, which will start the search of similar files in some directory.
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.search_button.setFont(font)
        self.search_button.setObjectName("search_button")
        self.gridLayout.addWidget(self.search_button, 1, 1, 1, 1)

        # Setting up a panel, where the path to the directory will be printed.
        self.path_panel = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.path_panel.setFont(font)
        self.path_panel.setObjectName("path_panel")
        self.gridLayout.addWidget(self.path_panel, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1140, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Similar files finder"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Please print path to the directory where you wish to search for "
                                                    "the similar files."))
