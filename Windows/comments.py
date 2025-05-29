from PyQt6.QtCore import QSize, Qt, pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QStackedLayout, QVBoxLayout, \
    QHBoxLayout
from PyQt6.QtWidgets import QTabWidget, QToolBar, QLabel, QTableView, QScrollArea, QComboBox, QFileDialog
from PyQt6.QtGui import QPalette, QColor, QAction, QIcon
import sys
import PyQt6


class commentWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setFixedWidth(500)
        self.setFixedHeight(300)
        self.setWindowTitle(str(title))

        self.revArr = []

        self.mainWidget = QWidget()

        self.vLayout = QVBoxLayout()


        self.scrollPane = QScrollArea()
        self.containerWidget = QWidget()

        self.paneLayout = QVBoxLayout()

    def init(self):
        for rev in self.revArr:
            self.paneLayout.addWidget(rev)
        
        self.containerWidget.setLayout(self.paneLayout)
        self.scrollPane.setWidgetResizable(True)
        self.scrollPane.setWidget(self.containerWidget)

        self.vLayout.addWidget(self.scrollPane)

        self.mainWidget.setLayout(self.vLayout)

        self.setCentralWidget(self.mainWidget)