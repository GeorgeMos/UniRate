#Global Lib Imports
from PyQt6.QtCore import QSize, Qt, pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QStackedLayout, QVBoxLayout, \
    QHBoxLayout
from PyQt6.QtWidgets import QTabWidget, QToolBar, QLabel, QTableView, QScrollArea, QComboBox, QFileDialog
from PyQt6.QtGui import QPalette, QColor, QAction
import sys
import PyQt6

#Local imports
import Windows.loginWindow as loginW
import Windows.Admin.adminMainWindow as adminW
import Windows.Student.studentMainWindow as studentW
import Windows.Teacher.teacherMainWindow as teacherW
import Widgets.Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.renameArr = [[]]
        self.currAction = ''

        #Widgets Setup
        mainWidget = QWidget()
        adminWindowWidget = adminW.adminMain()
        studentWindowWidget = studentW.studentMain()
        teacherWindowWidget = teacherW.teacherMain()
        loginWindowWidget = loginW.loginMain()

        #Layout Setup
        stackLayout = QStackedLayout()
        stackLayout.addWidget(adminWindowWidget)
        stackLayout.addWidget(studentWindowWidget)
        stackLayout.addWidget(teacherWindowWidget)
        stackLayout.addWidget(loginWindowWidget)
        stackLayout.setCurrentWidget(loginWindowWidget)
        mainWidget.setLayout(stackLayout)
        self.setCentralWidget(mainWidget)
        
        #Window setup
        self.setWindowTitle("UniRate")
        self.setMinimumSize(QSize(1000, 600))
        self.setMaximumSize(QSize(1920, 1080))
        self.showFullScreen()
        self.setUpdatesEnabled(True)
        
    
            