"""
This module contains all the functions and classes to create and run a similar files finder application.
"""

import sys
import os

from PyQt5 import QtGui, QtWidgets

import supertool.sff_window as sff
from supertool.similar_files_finder import similar_files_chains


class MainApplication(QtWidgets.QMainWindow):
    """
    Instances of this class will be similar files finder applications.
    """
    def __init__(self):
        """
        Constructor of class MainApplication.
        """
        super(MainApplication, self).__init__()
        self.ui = sff.SimilarFilesUIMainWindow()
        self.ui.setupUi(self)
        self.ui.search_button.clicked.connect(self.search_pressed)
        self.ui.tree.setHeaderLabels([''])

    def search_pressed(self):
        """
        This method is called when the button 'search' is pressed. It searches for the similar files chains in the
        directory from the ui.path_panel and displays them in the ui.tree.
        """
        self.ui.tree.clear()
        path = self.ui.path_panel.displayText()
        try:
            file_chains = similar_files_chains(path)
        except ValueError:
            self.ui.tree.setHeaderLabels(['Wrong directory.'])
        else:
            if len(file_chains) > 0:
                self.ui.tree.setHeaderLabels(['Similar files in directory {}:'.format(os.path.abspath(path))])
            else:
                self.ui.tree.setHeaderLabels(['No similar files found.'])
            for chain in file_chains:
                root = QtWidgets.QTreeWidgetItem(self.ui.tree, ['These {} files have similar contents:'.format(len(chain))])
                for file in chain:
                    son = QtWidgets.QTreeWidgetItem(root, [str(os.path.relpath(file.path, path))])


def run_similar_files_finder_app():
    """
    This function runs an instance of class MainWindow (the similar files finder application).
    """
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()
    sys.exit(app.exec_())
