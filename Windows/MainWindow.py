#Global Lib Imports
from PyQt6.QtCore import QSize, Qt, pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QStackedLayout, QVBoxLayout, \
    QHBoxLayout
from PyQt6.QtWidgets import QTabWidget, QToolBar, QLabel, QTableView, QScrollArea, QComboBox, QFileDialog
from PyQt6.QtGui import QPalette, QColor, QAction, QIcon
import sys
import PyQt6

#Local imports
import Windows.loginWindow as loginW
import Windows.Admin.adminMainWindow as adminW
import Windows.Student.studentMainWindow as studentW
import Windows.Teacher.teacherMainWindow as teacherW
import Widgets.Color
from Globals import userType

from Widgets import subjectContainer as sc


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.renameArr = [[]]
        self.currAction = ''

        #Widgets Setup
        self.mainWidget = QWidget()
        self.adminWindowWidget = adminW.adminMain(userType.ADMIN)
        self.admintestWindowWidget = adminW.adminMain(userType.NONE)
        self.studentWindowWidget = studentW.studentMain(userType.STUDENT)
        self.teacherWindowWidget = teacherW.teacherMain(userType.TEACHER)
        self.loginWindowWidget = loginW.loginMain(self)

        #Layout Setup
        self.stackLayout = QStackedLayout()
        self.stackLayout.addWidget(self.adminWindowWidget)
        self.stackLayout.addWidget(self.admintestWindowWidget)
        self.stackLayout.addWidget(self.studentWindowWidget)
        self.stackLayout.addWidget(self.teacherWindowWidget)
        self.stackLayout.addWidget(self.loginWindowWidget)
        self.stackLayout.setCurrentWidget(self.loginWindowWidget)
        self.mainWidget.setLayout(self.stackLayout)
        self.setCentralWidget(self.mainWidget)

        
        #self.testWidget = sc.SubjectContainer(userType.ADMIN)
        #self.setCentralWidget(self.testWidget)
        
        #Window setup
        self.setWindowTitle("UniRate")
        self.setMinimumSize(QSize(1000, 600))
        self.setMaximumSize(QSize(1920, 1080))
        self.showFullScreen()
        self.setUpdatesEnabled(True)


    def uiUpdate(self):
        if self.loginWindowWidget.userLevel == userType.ADMIN:
            print("admin")
            self.stackLayout.setCurrentWidget(self.adminWindowWidget)
        elif self.loginWindowWidget.userLevel == userType.STUDENT:
            print("student")
            self.stackLayout.setCurrentWidget(self.studentWindowWidget)
        elif self.loginWindowWidget.userLevel == userType.TEACHER:
            print("teacher")
            self.stackLayout.setCurrentWidget(self.teacherWindowWidget)
        elif self.loginWindowWidget.userLevel == userType.NONE:
            print("testUser")
            self.stackLayout.setCurrentWidget(self.admintestWindowWidget)
        else:
            print("BOGUS!")
        
    
            