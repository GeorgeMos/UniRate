#Global Lib Imports
from PyQt6.QtCore import QSize, Qt, pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QStackedLayout, QVBoxLayout, \
    QHBoxLayout, QScrollArea
from PyQt6.QtWidgets import QTabWidget, QToolBar, QLabel, QTableView, QScrollArea, QComboBox, QFileDialog, QLineEdit, QScrollBar
from PyQt6.QtGui import QPalette, QColor, QAction
import sys
import PyQt6
import pandas as pd

#Local imports
from API.upAPI import upAPI
from Globals import userType

class searchBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setUpdatesEnabled(True)

        self.searchBtn = QPushButton()

        self.subjectField = QLineEdit()

        self.hLayout = QHBoxLayout()
        self.hLayout.addWidget(self.searchBtn)
        self.hLayout.addWidget(self.subjectField)

        self.setLayout(self.hLayout)

class subject(QWidget):
    def __init__(self, name):
        super().__init__()
        self.setUpdatesEnabled(True)
        self.name = name

        self.hLayout = QHBoxLayout()

        self.mainAction = QPushButton()
        self.mainAction.setText(self.name)
        self.mainAction.clicked.connect(self.clickAction)

        self.hLayout.addWidget(self.mainAction)

        self.setLayout(self.hLayout)

    def clickAction(self):
        #Absolute terrible way to make things work.
        self.parent().parent().parent().parent().parent().subClicked.setText(self.name)




class subjects(QWidget):
    def __init__(self, subArray : list):
        super().__init__()
        self.setUpdatesEnabled(True)

        self.scrollPane = QScrollArea()
        self.containerWidget = QWidget()
        self.subArray = subArray

        self.paneLayout = QVBoxLayout()
        for sub in self.subArray:
            self.paneLayout.addWidget(sub)
        self.containerWidget.setLayout(self.paneLayout)
        self.scrollPane.setWidgetResizable(True)
        self.scrollPane.setWidget(self.containerWidget)
    
        self.vLayout = QVBoxLayout()
        self.vLayout.addWidget(self.scrollPane)
        self.setLayout(self.vLayout)


    


class SubjectContainer(QWidget):
    def __init__(self, userLevel :userType):
        super().__init__()
        self.setUpdatesEnabled(True)
        self.userLevel = userLevel
        self.searchTerm = ""

        self.subClicked = QLineEdit()

        self.subArr = []
        subFrame = upAPI.getRandomSubjects(self.searchTerm)
        for i in subFrame.values:
            self.subArr.append(subject(i[0]))
            

        self.vLayout = QVBoxLayout()

        self.searchBar = searchBar()
        self.searchBar.subjectField.textChanged.connect(self.updateSubjects)
        self.subjects = subjects(self.subArr)

        self.vLayout.addWidget(self.searchBar)
        self.vLayout.addWidget(self.subjects)

        self.setLayout(self.vLayout)

    def updateSubjects(self):
        self.searchTerm = self.searchBar.subjectField.text()
        
        self.subArr = []
        subFrame = upAPI.getRandomSubjects(self.searchTerm)
        for i in subFrame.values:
            self.subArr.append(subject(i[0]))
        
        self.vLayout.removeWidget(self.subjects)
        self.subjects = subjects(self.subArr)
        self.vLayout.addWidget(self.subjects)
        self.subjects.update()
        self.vLayout.update()
        self.update()


            


