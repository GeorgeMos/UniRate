#Global Lib Imports
from PyQt6.QtCore import QSize, Qt, pyqtSignal, QObject, QPropertyAnimation, QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QStackedLayout, QVBoxLayout, \
    QHBoxLayout, QScrollArea
from PyQt6.QtWidgets import QTabWidget, QToolBar, QLabel, QTableView, QScrollArea, QComboBox, QFileDialog, QLineEdit, QScrollBar
from PyQt6.QtGui import QPalette, QColor, QAction
import sys
import PyQt6
import pandas as pd
from random import randint

#Local imports
from API.upAPI import upAPI
from API.uniRateAPI import uniRateAPI
from Globals import userType


class review(QWidget):
    def __init__(self, text, user):
        super().__init__()
        self.setUpdatesEnabled(True)

        self.scrollPane = QScrollArea()
        self.containerWidget = QWidget()
        self.userLineEdit = QLineEdit()
        self.userLineEdit.setText(user)
        self.userLineEdit.setEnabled(False)

        self.textLineEdit = QLineEdit()
        self.textLineEdit.setText(text)
        self.textLineEdit.setEnabled(False)

        self.likeWidget = QWidget()

        self.likeBtn = QPushButton("Like")
        self.likeBtn.setFixedWidth(50)
        self.likeBtn.clicked.connect(self.like)

        self.repBtn = QPushButton("Report")
        self.repBtn.setFixedWidth(50)
        self.repBtn.clicked.connect(self.report)

        self.likeLabel = QLabel("Likes: " + str(randint(0, 50)))

        self.likeLayout = QHBoxLayout()
        self.likeLayout.addWidget(self.likeBtn)
        self.likeLayout.addWidget(self.likeLabel)
        self.likeLayout.addWidget(QWidget())
        self.likeLayout.addWidget(self.repBtn)
        self.likeWidget.setLayout(self.likeLayout)
        self.likeLayout.setStretch(0, 0)
        self.likeLayout.setStretch(1, 0)
        self.likeLayout.setStretch(2, 1)

        self.paneLayout = QVBoxLayout()

        self.paneLayout.addWidget(self.textLineEdit)
        self.paneLayout.addWidget(self.likeWidget)

        self.containerWidget.setLayout(self.paneLayout)
        self.scrollPane.setWidgetResizable(True)
        self.scrollPane.setWidget(self.containerWidget)
        self.scrollPane.setFixedHeight(100)

        self.vLayout = QVBoxLayout()

        self.vLayout.addWidget(self.userLineEdit)
        self.vLayout.addWidget(self.scrollPane)
        self.vLayout.setStretch(1, 1)

        self.setMouseTracking(True)

        self.setLayout(self.vLayout)

    def mouseMoveEvent(self, a0):
        if self.parent().parent().parent().parent().userLevel == userType.NONE:
            self.anim = QPropertyAnimation(self, b"pos")
            #self.anim.setEndValue(QPoint(400, 400))
            self.anim.setEndValue(QPoint(randint(-200, 400), randint(0, 500)))
            self.raise_()
            self.anim.setDuration(500)
            self.anim.start()
        return super().mouseMoveEvent(a0)
    
    def report(self):
        self.repBtn.setEnabled(False)

    def like(self):
        self.likeBtn.setEnabled(False)

class ReviewContainer(QWidget):
    def __init__(self, subjectCode, type :userType):
        super().__init__()
        self.setUpdatesEnabled(True)
        self.subjectCode = subjectCode
        self.userLevel = type

        self.revArr = []

        if(self.subjectCode != ""):
            num = int(str(self.subjectCode).split(" ")[1])
            data = uniRateAPI.getRandomReviews(num)
            values = data.values


            for i in values:
                userData = uniRateAPI.getRandomUsers(i[1])
                if len(userData.values) > 0:
                    name = userData.values[0][1] + " " + userData.values[0][2]
                else:
                    name = ""

                if self.userLevel == userType.TEACHER:
                    name = "Anonymus User"
                self.revArr.append(review(i[2], name))

        self.vLayout = QVBoxLayout()


        self.scrollPane = QScrollArea()
        self.containerWidget = QWidget()

        self.paneLayout = QVBoxLayout()

        for rev in self.revArr:
            self.paneLayout.addWidget(rev)
        
        self.containerWidget.setLayout(self.paneLayout)
        self.scrollPane.setWidgetResizable(True)
        self.scrollPane.setWidget(self.containerWidget)

        self.vLayout.addWidget(self.scrollPane)

        self.setLayout(self.vLayout)
        