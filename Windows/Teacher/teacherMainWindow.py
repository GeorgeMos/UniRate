#Global Lib Imports
from PyQt6.QtCore import QSize, Qt, pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QStackedLayout, QVBoxLayout, \
    QHBoxLayout
from PyQt6.QtWidgets import QTabWidget, QToolBar, QLabel, QTableView, QScrollArea, QComboBox, QFileDialog
from PyQt6.QtGui import QPalette, QColor, QAction
import sys
import PyQt6

from Widgets.subjectContainer import SubjectContainer, subject
from Widgets.reviewContainer import ReviewContainer
from Globals import userType

class teacherMain(QWidget):
    def __init__(self, type :userType):
        super().__init__()
        self.setUpdatesEnabled(True)
        self.subClicked = ""
        self.type = type

        self.hLayout = QGridLayout()

        self.subCont = SubjectContainer(self.type)
        self.subCont.subClicked.textChanged.connect(self.onSubClicked)
        self.revCont = ReviewContainer("", self.type)

        self.hLayout.addWidget(self.subCont, 0, 0)
        self.hLayout.addWidget(self.revCont, 0, 1)

        self.hLayout.setColumnStretch(1, 1)
        self.vLayout = QVBoxLayout()
        self.toolbar = QToolBar("Main bar")
        self.vLayout.addWidget(self.toolbar)

        self.profileAction = QAction("Profile", self)
        self.profileAction.setStatusTip("Profile")
        self.profileAction.triggered.connect(self.profileClicked)
        self.toolbar.addAction(self.profileAction)

        self.dummy = QWidget()
        self.dummy.setLayout(self.hLayout)
        self.vLayout.addWidget(self.dummy)
        self.vLayout.setStretch(1, 1)

        self.setLayout(self.vLayout)

    def onSubClicked(self):
        self.subClicked = self.subCont.subClicked.text()

        self.hLayout.removeWidget(self.revCont)
        self.revCont = ReviewContainer(self.subClicked, self.type)
        self.hLayout.addWidget(self.revCont, 0, 1)
        self.hLayout.setColumnStretch(1, 1)
        self.hLayout.update()
        self.update()

    def profileClicked(self):
        pass



        

        