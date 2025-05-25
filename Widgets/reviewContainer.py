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

        self.paneLayout = QVBoxLayout()

        self.paneLayout.addWidget(self.textLineEdit)

        self.containerWidget.setLayout(self.paneLayout)
        self.scrollPane.setWidgetResizable(True)
        self.scrollPane.setWidget(self.containerWidget)

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
        