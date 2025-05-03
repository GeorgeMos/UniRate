#Global Lib Imports
from PyQt6.QtCore import QSize, Qt, pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QStackedLayout, QVBoxLayout, \
    QHBoxLayout
from PyQt6.QtWidgets import QTabWidget, QToolBar, QLabel, QTableView, QScrollArea, QComboBox, QFileDialog, QLineEdit
from PyQt6.QtGui import QPalette, QColor, QAction
import sys
import PyQt6

#Local Imports
from Globals import Colors, Fonts

class loginMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setUpdatesEnabled(True)

        #Widgets Setup
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

        #Layout Setup
        self.gridLayout = QGridLayout()
        #Y, X | ROW, COLUMN
        self.gridLayout.addWidget(self.usernameLabel, 1, 1)
        self.gridLayout.addWidget(self.usernameField, 1, 2)
        self.gridLayout.addWidget(self.passwordLabel, 2, 1)
        self.gridLayout.addWidget(self.passwordField, 2, 2)
        self.gridLayout.addWidget(self.loginBtn, 3, 2)


        #Setup automatic stretching / self centering
        #self.gridLayout.setColumnMinimumWidth(0, 500)
        #self.gridLayout.setColumnMinimumWidth(3, 500)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(3, 1)

        #self.gridLayout.setRowMinimumHeight
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.setLayout(self.gridLayout)

        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, Colors.secondaryLogoColor)
        self.setPalette(palette)



        