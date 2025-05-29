#Global Lib Imports
from PyQt6.QtCore import QSize, Qt, pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QStackedLayout, QVBoxLayout, \
    QHBoxLayout
from PyQt6.QtWidgets import QTabWidget, QToolBar, QLabel, QTableView, QScrollArea, QComboBox, QFileDialog
from PyQt6.QtGui import QPalette, QColor, QAction
import sys
import PyQt6
from random import randint

from Widgets.subjectContainer import SubjectContainer, subject
from Widgets.reviewContainer import ReviewContainer
from Globals import userType, Fonts

class adminMain(QWidget):
    def __init__(self, type :userType):
        super().__init__()
        self.setUpdatesEnabled(True)
        self.subClicked = ""
        self.type = type

        self.subTitleWidget = QWidget()
        self.subTitleLayout = QGridLayout()

        self.subTitle = QLabel(self.subClicked)
        self.subTitle.setFont(Fonts.subTitleFont)
        self.rateLabel = QLabel("")
        self.rateLabel.setFont(Fonts.rateLabelFont)

        self.subTitleLayout.addWidget(self.subTitle, 0, 0)
        self.subTitleLayout.addWidget(self.rateLabel, 1, 0)




        self.hLayout = QGridLayout()
        self.subCont = SubjectContainer(self.type)
        self.subCont.subClicked.textChanged.connect(self.onSubClicked)
        self.revCont = ReviewContainer("", self.type)

        self.subTitleLayout.addWidget(self.revCont, 1, 0)
        self.subTitleWidget.setLayout(self.subTitleLayout)

        self.hLayout.addWidget(self.subCont, 0, 0)
        self.hLayout.addWidget(self.subTitleWidget, 0, 1)

        self.hLayout.setColumnStretch(1, 1)
        self.vLayout = QVBoxLayout()
        self.toolbar = QToolBar("Main bar")
        self.vLayout.addWidget(self.toolbar)

        self.profileAction = QAction("Profile", self)
        self.profileAction.setStatusTip("Profile")
        self.profileAction.triggered.connect(self.profileClicked)
        self.toolbar.addAction(self.profileAction)

        self.repReviews = QAction("Reported", self)
        self.repReviews.triggered.connect(self.reportedClicked)
        self.toolbar.addAction(self.repReviews)

        self.dummy = QWidget()
        self.dummy.setLayout(self.hLayout)
        self.vLayout.addWidget(self.dummy)
        self.vLayout.setStretch(1, 1)

        self.setLayout(self.vLayout)

    def onSubClicked(self):
        self.subClicked = self.subCont.subClicked.text()
        self.subTitleLayout.removeWidget(self.revCont)
        self.revCont = ReviewContainer(self.subClicked, self.type)
        self.subTitleLayout.addWidget(self.revCont, 2, 0)
        #self.hLayout.setColumnStretch(1, 1)
        self.rateLabel.setText("Rating: " + str(randint(0, 10)) + "/10")
        self.subTitle.setText(self.subClicked)
        self.subTitleLayout.update()
        self.update()

    def profileClicked(self):
        pass

    def reportedClicked(self):
        pass



        

        