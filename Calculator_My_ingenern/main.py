from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import operator

from Calculator_My_ingenern import Ui_MainWindow

# Calculator state.
READY = 0
INPUT = 1

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)



        self.memory = 0
        #self.reset()

        self.show()

    def display(self):
        self.lcdNumber.display(self.stack[-1])




if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Calculon")

    window = MainWindow()
    app.exec_()