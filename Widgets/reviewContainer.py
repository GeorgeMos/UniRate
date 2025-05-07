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
from API.uniRateAPI import uniRateAPI


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

        self.setLayout(self.vLayout)

class ReviewContainer(QWidget):
    def __init__(self):
        super().__init__()
        self.setUpdatesEnabled(True)

        self.revArr = []

        for i in range(10):
            self.revArr.append(review("Text", "Username"))

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
        