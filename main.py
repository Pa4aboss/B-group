from PyQt5 import QtGui, QtCore, QtWidgets
from mainwindow import Ui_MainWindow
import sys


class MainWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()


#if __name__ == '__main__':
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
