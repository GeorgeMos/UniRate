#Global Lib Imports
from PyQt6.QtCore import QSize, Qt, pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QStackedLayout, QVBoxLayout, \
    QHBoxLayout
from PyQt6.QtWidgets import QTabWidget, QToolBar, QLabel, QTableView, QScrollArea, QComboBox, QFileDialog
from PyQt6.QtGui import QPalette, QColor, QAction
import sys
import PyQt6



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.renameArr = [[]]
        self.currAction = ''

        self.setWindowTitle("UniRate")
        self.setMinimumSize(QSize(1000, 600))
        self.setMaximumSize(QSize(1920, 1080))
        self.showFullScreen()
        self.setUpdatesEnabled(True)
        
    
            