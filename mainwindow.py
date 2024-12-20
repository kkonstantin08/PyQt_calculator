import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, \
    QMainWindow
from calculator1 import Ui_MainWindow
from PyQt6 import QtWidgets


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.lineedit_result = ''
        self.button_0.clicked.connect(self.common_func)
        self.button_1.clicked.connect(self.common_func)
        self.button_3.clicked.connect(self.common_func)
        self.button_4.clicked.connect(self.common_func)
        self.button_2.clicked.connect(self.common_func)
        self.button_5.clicked.connect(self.common_func)
        self.button_6.clicked.connect(self.common_func)
        self.button_7.clicked.connect(self.common_func)
        self.button_8.clicked.connect(self.common_func)
        self.button_9.clicked.connect(self.common_func)
        self.button_multiply.clicked.connect(self.special_func)
        self.button_split.clicked.connect(self.special_func)
        self.button_take.clicked.connect(self.special_func)
        self.button_add.clicked.connect(self.special_func)
        self.button_delete.clicked.connect(self.special_func)
        self.button_result.clicked.connect(self.special_func)
        self.button_point.clicked.connect(self.special_func)
        self.button_level.clicked.connect(self.special_func)

    def special_func(self):
        sender = self.sender()
        sender = sender.text()
        print(sender)
        if '/' in sender:
            self.lineedit_result = self.lineedit_result + '/'
            self.lineEdit.setText(self.lineedit_result)
        if '*' in sender:
            self.lineedit_result = self.lineedit_result + '*'
            self.lineEdit.setText(self.lineedit_result)
        if '-' in sender:
            self.lineedit_result = self.lineedit_result + '-'
            self.lineEdit.setText(self.lineedit_result)
        if '+' in sender:
            self.lineedit_result = self.lineedit_result + '+'
            self.lineEdit.setText(self.lineedit_result)
        if '**' in sender:
            self.lineedit_result = self.lineedit_result + '*'
            self.lineEdit.setText(self.lineedit_result)
        if '.' in sender:
            self.lineedit_result = self.lineedit_result + '.'
            self.lineEdit.setText(self.lineedit_result)
        if 'С' in sender:
            self.lineedit_result = ''
            self.lineEdit.setText('')
            self.lcdNumber.display(0)
        if '=' in sender:
            result = eval(self.lineedit_result)
            self.lcdNumber.display(result)


    def common_func(self):
        sender = self.sender().text()
        self.lineedit_result = self.lineedit_result + sender[-1]
        self.lineEdit.setText(self.lineedit_result)


app = QApplication(sys.argv)
app.setStyle('Fusion')
window = Window()
window.show()
sys.exit(app.exec())
