#Global Lib Imports
from PyQt6.QtCore import QSize, Qt, pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QStackedLayout, QVBoxLayout, \
    QHBoxLayout
from PyQt6.QtWidgets import QTabWidget, QToolBar, QLabel, QTableView, QScrollArea, QComboBox, QFileDialog, QLineEdit, QGraphicsColorizeEffect
from PyQt6.QtGui import QPalette, QColor, QAction, QPixmap
import sys
import PyQt6

#Local Imports
from Globals import Colors, Fonts, userType


class loginMain(QWidget):
    def __init__(self, parentWindow :QMainWindow):
        super().__init__()
        self.setUpdatesEnabled(True)
        self.userLevel :userType = userType.NONE
        self.parentWindow = parentWindow

        #Widgets Setup
        labelColor = color_effect = color_effect = QGraphicsColorizeEffect()
        color_effect.setColor(QColor(255, 255, 255))


        self.usernameLabel = QLabel("Username")
        self.usernameLabel.setFont(Fonts.loginLabelFont)
        
        self.passwordLabel = QLabel("Password")
        self.passwordLabel.setFont(Fonts.loginLabelFont)

        self.usernameField = QLineEdit()
        self.usernameField.setFixedWidth(200)
        self.passwordField = QLineEdit()
        self.passwordField.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordField.setFixedWidth(200)

        self.loginBtn = QPushButton()
        self.loginBtn.setText("Login")
        self.loginBtn.setFixedWidth(200)
        self.loginBtn.clicked.connect(self.loginBtnAction)

        self.image = QLabel("TEST")
        self.imgPixmap = QPixmap("Images/png/uniRate_1.png")
        self.image.setPixmap(self.imgPixmap)
        self.image.setScaledContents(True)
        self.image.setFixedWidth(200)
        self.image.setFixedHeight(200)


        #Layout Setup
        self.gridLayout = QGridLayout()
        #Y, X | ROW, COLUMN
        self.gridLayout.addWidget(self.image, 1, 2)
        self.gridLayout.addWidget(self.usernameLabel, 2, 1)
        self.gridLayout.addWidget(self.usernameField, 2, 2)
        self.gridLayout.addWidget(self.passwordLabel, 3, 1)
        self.gridLayout.addWidget(self.passwordField, 3, 2)
        self.gridLayout.addWidget(self.loginBtn, 4, 2)


        #Setup automatic stretching / self centering
        #self.gridLayout.setColumnMinimumWidth(0, 500)
        #self.gridLayout.setColumnMinimumWidth(3, 500)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(2, 1)

        #self.gridLayout.setRowMinimumHeight
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(5, 1)
        self.setLayout(self.gridLayout)

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, Colors.secondaryLogoColor)
        self.setPalette(palette)

    def loginBtnAction(self):
        #Testing
        if self.usernameField.text() == "admin":
            self.userLevel = userType.ADMIN
            self.parentWindow.uiUpdate()
        elif self.usernameField.text() == "student":
            self.userLevel = userType.STUDENT
            self.parentWindow.uiUpdate()
        elif self.usernameField.text() == "teacher":
            self.userLevel = userType.TEACHER
            self.parentWindow.uiUpdate()
        elif self.usernameField.text() == "testUser":
            self.userLevel = userType.NONE
            self.parentWindow.uiUpdate()
        else:
            self.userLevel = userType.NONE
        
        



        