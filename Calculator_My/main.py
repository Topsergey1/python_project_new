from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import operator

from MainWindow import Ui_MainWindow

# Calculator state.
READY = 0
INPUT = 1

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Setup numbers.
        for n in range(0, 10):
            getattr(self, 'pushButton_n%s' % n).pressed.connect(lambda v=n: self.input_number(v))
        self.pushButton_n00.pressed.connect(self.operation_n00)


        # Setup operations.
        self.pushButton_add.pressed.connect(lambda: self.operation(operator.add))
        self.pushButton_sub.pressed.connect(lambda: self.operation(operator.sub))
        self.pushButton_mul.pressed.connect(lambda: self.operation(operator.mul))
        self.pushButton_div.pressed.connect(lambda: self.operation(operator.truediv))  # operator.div for Python2.7


        self.pushButton_pc.pressed.connect(self.operation_pc)
        self.pushButton_sqr.pressed.connect(self.operation_sqrt)
        self.pushButton_pm.pressed.connect(self.operation_pm)
        self.pushButton_1divx.pressed.connect(self.operation_1divx)

        self.pushButton_eq.pressed.connect(self.equals)

        # Setup actions
        #self.actionReset.triggered.connect(self.reset)
        self.pushButton_ac.pressed.connect(self.reset)
        self.pushButton_ce.pressed.connect(self.reset_ce)
        self.pushButton_del.pressed.connect(self.delete)

        #self.actionExit.triggered.connect(self.close)

        self.pushButton_mp.pressed.connect(self.memory_plus)
        self.pushButton_mm.pressed.connect(self.memory_minus)
        self.pushButton_mr.pressed.connect(self.memory_recall)
        self.pushButton_mc.pressed.connect(self.memory_reset)

        self.memory = 0
        self.reset()

        self.show()

    def display(self):
        self.lcdNumber.display(self.stack[-1])

    def reset(self):
        self.state = READY
        self.stack = [0]
        self.last_operation = None
        self.current_op = None
        self.display()

    def reset_ce(self):
        self.state = READY
        self.stack[-1] = 0
        self.display()

    def delete(self): #deleting the last digit
        if self.state == INPUT:
            self.stack[-1] = (self.stack[-1] - (self.stack[-1] % 10)) / 10
            self.display()

    #functions for working with memory
    def memory_plus(self):
        self.state = READY
        self.memory += self.lcdNumber.value()

    def memory_minus(self):
        self.state = READY
        self.memory -= self.lcdNumber.value()

    def memory_recall(self):
        self.state = READY
        self.stack[-1] = self.memory
        self.display()

    def memory_reset(self):
        self.memory = 0

    def input_number(self, v):
        if self.state == READY:
            self.state = INPUT
            self.stack[-1] = v
        else:
            self.stack[-1] = self.stack[-1] * 10 + v

        self.display()

    def operation(self, op):
        if self.current_op:  # Complete the current operation
            self.equals()

        self.stack.append(0)
        self.state = INPUT
        self.current_op = op

    def operation_pc(self):
        self.state = INPUT
        self.stack[-1] *= 0.01
        self.display()

    def operation_sqrt(self): #Calculating the square root of a number_____
        self.state = INPUT
        if self.stack[-1] >= 0:
            self.stack[-1] = operator.pow(self.stack[-1], 0.5)
            self.display()
        else:
            self.lcdNumber.display('Error')

    def operation_pm(self):
        self.state = INPUT
        self.stack[-1] = self.stack[-1] * -1
        self.display()

    def operation_n00(self):
        self.input_number(0)
        self.input_number(0)

    def operation_1divx(self):
        self.state = INPUT
        self.stack[-1] = self.stack[-1] ** -1
        self.display()

    def equals(self):
        # Support to allow '=' to repeat previous operation
        # if no further input has been added.
        if self.state == READY and self.last_operation:
            s, self.current_op = self.last_operation
            self.stack.append(s)

        if self.current_op:
            self.last_operation = self.stack[-1], self.current_op

            try:
                self.stack = [self.current_op(*self.stack)]
            except Exception:
                self.lcdNumber.display('Err')
                self.stack = [0]
            else:
                self.current_op = None
                self.state = READY
                self.display()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Calculon")

    window = MainWindow()
    app.exec_()