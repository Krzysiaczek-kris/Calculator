import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLCDNumber
from PyQt6 import uic


class Variables:
    def __init__(self):
        self.number = 0
        self.number2 = 0
        self.result = 0
        self.fresh = False
        self.float = False

    def set_number_1(self, number):
        self.number = number

    def set_number_2(self, number):
        self.number2 = number

    def add(self):
        self.result = self.number + self.number2
        return self.result

    def subtract(self):
        self.result = self.number - self.number2
        return self.result

    def multiply(self):
        self.result = self.number * self.number2
        return self.result

    def divide(self):
        if self.number2 == 0:
            return 'Error'
        self.result = self.number / self.number2
        return self.result


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("D:/Python/Calculator/calc.ui", self)

        # Connect signals to slots
        self.pushButton_0.clicked.connect(lambda: self.update_display('0'))
        self.pushButton_1.clicked.connect(lambda: self.update_display('1'))
        self.pushButton_2.clicked.connect(lambda: self.update_display('2'))
        self.pushButton_3.clicked.connect(lambda: self.update_display('3'))
        self.pushButton_4.clicked.connect(lambda: self.update_display('4'))
        self.pushButton_5.clicked.connect(lambda: self.update_display('5'))
        self.pushButton_6.clicked.connect(lambda: self.update_display('6'))
        self.pushButton_7.clicked.connect(lambda: self.update_display('7'))
        self.pushButton_8.clicked.connect(lambda: self.update_display('8'))
        self.pushButton_9.clicked.connect(lambda: self.update_display('9'))
        self.pushButton_comma.clicked.connect(lambda: self.update_display('.'))

        self.pushButton_plus.clicked.connect(lambda: self.set_operation('+'))
        self.pushButton_minus.clicked.connect(lambda: self.set_operation('-'))
        self.pushButton_multiply.clicked.connect(lambda: self.set_operation('*'))
        self.pushButton_divide.clicked.connect(lambda: self.set_operation('/'))
        self.pushButton_eval.clicked.connect(self.calculate_result)
        # self.pushButton_clear.clicked.connect(self.clear_display)

        self.show()

        # Initialize variables
        self.vars = Variables()
        self.operation = ''

    def update_display(self, value):
        if self.vars.fresh:
            self.vars.fresh = False
            self.lcdNumber.display('0')
            self.vars.set_number_1(0)
            self.vars.set_number_2(0)
        text = self.lcdNumber.value()
        if text == '0':
            text = ''
        if value == '.':
            self.vars.float = True
            return
        if self.vars.float:
            self.lcdNumber.display(float(text) + float(value)/10)
        else:
            self.lcdNumber.display(float(text)*10 + float(value))

    def set_operation(self, operation):
        self.vars.set_number_1(float(self.lcdNumber.value()))
        self.lcdNumber.display('0')
        self.operation = operation
        self.vars.fresh = False
        self.vars.float = False

    def calculate_result(self):
        self.vars.set_number_2(float(self.lcdNumber.value()))
        self.vars.fresh = True
        self.vars.float = False
        if self.operation == '+':
            result = self.vars.add()
        elif self.operation == '-':
            result = self.vars.subtract()
        elif self.operation == '*':
            result = self.vars.multiply()
        elif self.operation == '/':
            result = self.vars.divide()
            if result == 'Error':
                self.lcdNumber.display(result)
                return
            result = round(result, 8)
        else:
            return
        self.lcdNumber.display(str(result))

    def clear_display(self):
        self.lcdNumber.display('0')
        self.operation = ''


app = QApplication([])
window = UI()
sys.exit(app.exec())
