from PyQt6.QtGui import QColor, QFont
from enum import Enum
class userType(Enum):
     ADMIN = 1
     STUDENT = 2
     TEACHER = 3
     NONE = 0
class Colors():
     mainLogoColor = QColor(1, 8, 75, 255)
     secondaryLogoColor = QColor(12, 192, 223, 255)

class Fonts():
     loginLabelFont = QFont("Times", 10)
     loginLabelFont.setBold(True)
     