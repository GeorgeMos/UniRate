#Global Lib Imports
from PyQt6.QtCore import QSize, Qt, pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QStackedLayout, QVBoxLayout, \
    QHBoxLayout
from PyQt6.QtWidgets import QTabWidget, QToolBar, QLabel, QTableView, QScrollArea, QComboBox, QFileDialog
from PyQt6.QtGui import QPalette, QColor, QAction
import sys
import PyQt6

from Widgets.subjectContainer import SubjectContainer
from Widgets.reviewContainer import ReviewContainer
from Globals import userType

class adminMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setUpdatesEnabled(True)

        self.hLayout = QGridLayout()

        self.subCont = SubjectContainer(userType.ADMIN)
        self.revCont = ReviewContainer()

        self.hLayout.addWidget(self.subCont, 0, 0)
        self.hLayout.addWidget(self.revCont, 0, 1)

        self.hLayout.setColumnStretch(1, 1)

        self.setLayout(self.hLayout)


        

        