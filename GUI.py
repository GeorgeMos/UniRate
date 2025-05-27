#Global Lib Imports
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette, QColor, QAction, QIcon
from PyQt6.QtCore import QSize
import sys

#Local Lib Imports
from Windows.MainWindow import MainWindow


#Start the main gui loop
def startLoop():
    app = QApplication(sys.argv)

    window = MainWindow()
    #window.setWindowIcon(QIcon("Images/png/uniRate_1.png"))
    app_icon = QIcon()
    app_icon.addFile("Images/png/uniRate_1.png", QSize(16, 16))
    app.setWindowIcon(app_icon)
    window.setWindowTitle("UniRate")
    window.show()
    window.showMaximized()

    # Start the event loop.
    app.exec()