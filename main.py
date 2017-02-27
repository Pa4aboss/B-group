from PyQt5 import QtWidgets, QtCore, QtGui
from mainwindow import Ui_MainWindow
import sys
#from graph import Graph, Node
from reader import Reader


class MainWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()
        self.openFileButton.pressed.connect(self.open_file_button_click)
        self.solutionButton.pressed.connect(self.solution_button_click)

    def open_file_button_click(self):
        fd = QtWidgets.QFileDialog()
        #g = Reader.read(fd.getOpenFileName())
        g.draw_graph('lol', 'png')
        self.frame.setStyleSheet("background-image: url(lol.png);")

    def solution_button_click(self):
        self.frame.setStyleSheet("")
        #here is place for pathfinder
        comps = g.find_comps()
        self.solutionLabel.setText(f"Количеcтво связных компонент: {comps}")
        g.draw_graph('lol', 'png')
        self.frame.setStyleSheet("background-image: url(lol.png);")

#if __name__ == '__main__':
g = 0
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
