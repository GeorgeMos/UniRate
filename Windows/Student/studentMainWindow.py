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
from Widgets.reviewContainer import ReviewContainer, QnaContainer
from Globals import userType, Fonts

class studentMain(QWidget):
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

        self.qnaLabel = QLabel()
        self.qnaLabel.setFont(Fonts.subTitleFont)

        self.subTitleLayout.addWidget(self.subTitle, 0, 0)
        self.subTitleLayout.addWidget(self.rateLabel, 1, 0)





        self.hLayout = QGridLayout()
        self.subCont = SubjectContainer(self.type)
        self.subCont.subClicked.textChanged.connect(self.onSubClicked)
        self.revCont = ReviewContainer("", self.type)

        self.subTitleLayout.addWidget(self.revCont, 2, 0)
        self.subTitleWidget.setLayout(self.subTitleLayout)
        self.qnaCont = QnaContainer("", self.type)
        self.subTitleLayout.addWidget(self.qnaLabel, 3, 0)

        self.qnaBtn = QPushButton("Ask Something")
        self.qnaBtn.setFixedWidth(100)
        #self.subTitleLayout.addWidget(self.qnaBtn, 4, 0)

        self.subTitleLayout.addWidget(self.qnaCont, 5, 0)

        self.hLayout.addWidget(self.subCont, 0, 0)
        self.hLayout.addWidget(self.subTitleWidget, 0, 1)

        self.hLayout.setColumnStretch(1, 1)
        self.vLayout = QVBoxLayout()
        self.toolbar = QToolBar("Main bar")
        self.vLayout.addWidget(self.toolbar)

        self.profileAction = QAction("My Progress", self)
        self.profileAction.setStatusTip("My Progress")
        self.profileAction.triggered.connect(self.progClicked)
        self.toolbar.addAction(self.profileAction)

        self.reviewAction = QAction("Favorites", self)
        self.reviewAction.setStatusTip("Write a review for the selected subject")
        self.reviewAction.triggered.connect(self.favClicked)
        self.toolbar.addAction(self.reviewAction)

        self.dummy = QWidget()
        self.dummy.setLayout(self.hLayout)
        self.vLayout.addWidget(self.dummy)
        self.vLayout.setStretch(1, 1)

        self.setLayout(self.vLayout)

    def onSubClicked(self):
        self.subClicked = self.subCont.subClicked.text()
        self.subTitleLayout.removeWidget(self.revCont)
        self.subTitleLayout.removeWidget(self.qnaCont)
        self.revCont = ReviewContainer(self.subClicked, self.type)
        self.qnaCont = QnaContainer(self.subClicked, self.type)
        self.subTitleLayout.addWidget(self.revCont, 2, 0)
        self.subTitleLayout.addWidget(self.qnaBtn, 4, 0)
        self.subTitleLayout.addWidget(self.qnaCont, 5, 0)
        #self.hLayout.setColumnStretch(1, 1)
        self.rateLabel.setText("Rating: " + str(randint(0, 10)) + "/10")
        self.qnaLabel.setText("QnA:")
        self.subTitle.setText(self.subClicked)
        self.subTitleLayout.update()
        self.update()

    def progClicked(self):
        pass

    def favClicked(self):
        pass



        

        