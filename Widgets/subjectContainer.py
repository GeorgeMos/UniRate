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

        self.hLayout.addWidget(self.mainAction)

        self.setLayout(self.hLayout)



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
    def __init__(self, userLevel):
        super().__init__()
        self.setUpdatesEnabled(True)
        self.userLevel = userLevel

        self.subArr = []
        subFrame = upAPI.getRandomSubjects()
        for i in range(subFrame.shape[0]):
            name = subFrame[subFrame.index == i]
            name = name.values[0][0]
            self.subArr.append(subject(name))

        self.vLayout = QVBoxLayout()

        self.searchBar = searchBar()
        self.subjects = subjects(self.subArr)

        self.vLayout.addWidget(self.searchBar)
        self.vLayout.addWidget(self.subjects)

        self.setLayout(self.vLayout)


