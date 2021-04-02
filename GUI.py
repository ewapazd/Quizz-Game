from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,QComboBox, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTabWidget, QTabWidget, QSizePolicy, QGridLayout, QGroupBox, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt

import sys
import math
import random

from Questions import *
#Code for creating dictionaries. Print it and copy here
#for i in range(1,11):
#    print(str(i)+':'+'\'P'+str(i)+'\',')

dict_pictures = {
1:'P1',
2:'P2',
3:'P3',
4:'P4' ,
5:'P5' ,
6:'P6' ,
7:'P7' ,
8:'P8' ,
9:'P9' ,
10:'P10'
}

dict_descriptions = {
1:Q1,
2:Q2,
3:Q3,
4:Q4,
5:Q5,
6:Q6,
7:Q7,
8:Q8,
9:Q9,
10:Q10
}

dict_options_1 = {
1:B1_1,
2:B2_1,
3:B3_1,
4:B4_1,
5:B5_1,
6:B6_1,
7:B7_1,
8:B8_1,
9:B9_1,
10:B10_1
}

dict_options_2 = {
1:B1_2,
2:B2_2,
3:B3_2,
4:B4_2,
5:B5_2,
6:B6_2,
7:B7_2,
8:B8_2,
9:B9_2,
10:B10_2
}

dict_options_3 = {
1:B1_3,
2:B2_3,
3:B3_3,
4:B4_3,
5:B5_3,
6:B6_3,
7:B7_3,
8:B8_3,
9:B9_3,
10:B10_3,
}

dict_answers = {
1:B1_2,
2:B2_2,
3:B3_3,
4:B4_1,
5:B5_3,
6:B6_2,
7:B7_2,
8:B8_3,
9:B9_2,
10:B10_1,
}

dict_answer_description = {
1:A1,
2:A2,
3:A3,
4:A4,
5:A5,
6:A6,
7:A7,
8:A8,
9:A9,
10:A10,
}

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.setGeometry(0, 0, 600,600)
        self.setWindowTitle('Quizz Game')
        self.setWindowIcon(QIcon("images/icon.png"))

        self.intro_widget = QWidget()
        self.mainlayout = QVBoxLayout()

        self.introduction = QLabel()
        self.introduction.setStyleSheet("background-color: white")
        self.introduction.setWordWrap(True)
        self.introduction.setFont(QFont('Times Font', 10, QFont.Bold))
        self.introduction.setText('{}\n\n{}'.format(start,description))
        self.introduction.setAlignment(QtCore.Qt.AlignCenter)

        self.gobutton = QPushButton('Let\'s Go')
        self.gobutton.resize(100,100)
        self.gobutton.clicked.connect(self.close_main_open_game)
        self.gobutton.setMinimumHeight(100)

        self.mainlayout.addStretch(1)
        self.mainlayout.addWidget(self.introduction)
        self.mainlayout.addStretch(1)
        self.mainlayout.addWidget(self.gobutton)

        self.intro_widget.setLayout(self.mainlayout)
        self.setCentralWidget(self.intro_widget)

    def close_main_open_game(self):
        self.gamewindow = Main(parent = self)
        self.setCentralWidget(self.gamewindow)
        self.setGeometry(0, 0, 1000,700)

class Main(QWidget):
    def __init__(self, parent):
        super(Main,self).__init__(parent)

        self.number = 1

        self.layout = QHBoxLayout()
        self.box = QVBoxLayout()

        self.roll_button = QPushButton('Roll')
        self.roll_button.resize(100,100)
        self.roll_button.clicked.connect(self.roll_number)
        self.roll_button.clicked.connect(self.set_picture_details)
        self.roll_button.clicked.connect(self.set_picture)
        self.roll_button.setMinimumHeight(100)

        self.next_button = QPushButton('Next')
        self.next_button.resize(100,100)
        self.next_button.clicked.connect(self.next_number)
        self.next_button.clicked.connect(self.set_picture_details)
        self.next_button.clicked.connect(self.set_picture)
        self.next_button.setMinimumHeight(100)

        self.picture= QLabel()
        self.picture.setPixmap(QPixmap('images/P{}.png'.format(self.number)))
        self.picture_description = QLabel()
        self.picture_description.setStyleSheet("background-color: white")
        self.picture_description.setFont(QFont('Times Font', 12, QFont.Bold))
        self.picture_description.setText(dict_descriptions.get(self.number))
        self.picture_description.setWordWrap(True)
        self.picture_description.setAlignment(QtCore.Qt.AlignCenter)
        self.picture_description.setMinimumHeight(100)

        self.button1 = QPushButton(dict_options_1.get(self.number))
        self.button2 = QPushButton(dict_options_2.get(self.number))
        self.button3 = QPushButton(dict_options_3.get(self.number))

        self.button1.clicked.connect(self.set_after_user_click)
        self.button2.clicked.connect(self.set_after_user_click)
        self.button3.clicked.connect(self.set_after_user_click)

        self.button1.clicked.connect(self.set_button1)
        self.button2.clicked.connect(self.set_button2)
        self.button3.clicked.connect(self.set_button3)

        self.answer_description = QLabel()
        self.answer_description.setStyleSheet("background-color: white")
        self.answer_description.setFont(QFont('Times Font', 12, QFont.Bold))
        self.answer_description.setWordWrap(True)
        self.answer_description.setMinimumHeight(100)

        self.box.addStretch(1)
        self.box.addWidget(self.picture_description)
        self.box.addWidget(self.button1)
        self.box.addWidget(self.button2)
        self.box.addWidget(self.button3)
        self.box.addWidget(self.answer_description)
        self.box.addStretch(1)
        self.box.addWidget(self.next_button)
        self.box.addWidget(self.roll_button)

        self.layout.addWidget(self.picture)
        self.layout.addLayout(self.box)

        self.setLayout(self.layout)


    def roll_number(self):

        self.number = random.randint(1,10)

        self.button1.setStyleSheet("background-color: None")
        self.button2.setStyleSheet("background-color: None")
        self.button3.setStyleSheet("background-color: None")

        self.answer_description.setText('')

    def next_number(self):

        self.number = self.number+1
        if self.number > max(dict_answers.keys()):
            sys.exit()

        self.button1.setStyleSheet("background-color: None")
        self.button2.setStyleSheet("background-color: None")
        self.button3.setStyleSheet("background-color: None")

        self.answer_description.setText('')

    def set_picture_details(self):
        self.picture_description.setText(dict_descriptions.get(self.number))
        self.opt1 = dict_options_1.get(self.number)
        self.button1.setText(dict_options_1.get(self.number))
        self.button2.setText(dict_options_2.get(self.number))
        self.button3.setText(dict_options_3.get(self.number))

    def set_picture(self):
        pixmap = QPixmap('images/P{}.png'.format(self.number))
        pixmap = pixmap.scaledToWidth(475)
        self.picture.setPixmap(pixmap)

    def set_after_user_click(self, button):
        self.answer_description.setText(dict_answer_description.get(self.number))

        if self.button1.text() == dict_answers.get(self.number):
            self.button1.setStyleSheet("background-color: green")
        elif self.button2.text() == dict_answers.get(self.number):
            self.button2.setStyleSheet("background-color: green")
        else:
            self.button3.setStyleSheet("background-color: green")

    def set_button1(self):
        if self.button1.text() == dict_answers.get(self.number):
            self.button1.setStyleSheet("background-color: green")
        else:
            self.button1.setStyleSheet("background-color: red")

    def set_button2(self):
        if self.button2.text() == dict_answers.get(self.number):
            self.button2.setStyleSheet("background-color: green")
        else:
            self.button2.setStyleSheet("background-color: red")

    def set_button3(self):
        if self.button3.text() == dict_answers.get(self.number):
            self.button3.setStyleSheet("background-color: green")
        else:
            self.button3.setStyleSheet("background-color: red")

def main():
    stylesheet = """
        QMainWindow {
            background-image: url("images/background.png");
            background-repeat: no-repeat;
            background-position: center;
        }
    """
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
