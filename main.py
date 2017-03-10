from PyQt5 import QtWidgets, QtCore, QtGui
from mainwindow import Ui_MainWindow
import sys
from graph import Graph, Node
from reader import Reader


class MainWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
    #Инициализвация переменных
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()
        self.openFileButton.pressed.connect(self.open_file_button_click)
        self.solutionButton.pressed.connect(self.solution_button_click)
        self.g = 0
        self.visualize = True

    def open_file_button_click(self):
        #Обработчик нажатия кнопки открыть файл
        self.frame.setStyleSheet("")
        fd = QtWidgets.QFileDialog()
        filepath = fd.getOpenFileName(None, fd.tr("Open Graph file"), ".", fd.tr("Textfile(*.txt)"))[0]
        if filepath == '':
            return 1
        #Вызов Парсера для файла
        self.g = Reader.read(filepath)
        Mb = QtWidgets.QMessageBox()
        Mb.setText("Вы хотите включить режим визуализации?\nПримечание. Большие графы могут отображаться некорректно.")
        Mb.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        Mb.setDefaultButton(QtWidgets.QMessageBox.Yes)
        Mb.setModal(True)
        ret = Mb.exec()
        if ret == QtWidgets.QMessageBox.Yes:
            self.visualize = True
        elif ret == QtWidgets.QMessageBox.No:
            self.visualize = False
        if self.visualize:
            self.g.draw_graph('lol', 'png')
            self.frame.setStyleSheet("background-image: url(lol.png); background-repeat: no-repeat;")

    def solution_button_click(self):
        #Обработчик нажатия кнопки выполнить
        self.frame.setStyleSheet("")
        pairs = self.g.find_shortest_way(self.g.start, self.g.finish)
        comps = self.g.find_comps()
        if self.visualize:
            self.solutionLabel.setText(f"Количеcтво связных компонент: {comps}")
            self.g.draw_graph('lol', 'png', pairs)
            self.frame.setStyleSheet("background-image: url(lol.png); background-repeat: no-repeat;")
        else:
            if pairs:
                path = []
                for i in range(-1, -len(pairs) - 1, -1):
                    if i == -1:
                        path.append(pairs[i][1])
                    path.append(pairs[i][0])
            else:
                path = "Нет пути"
            self.solutionLabel.setText(f"Путь из {self.g.start} в {self.g.finish} : {path}\n"
                                       f"Количеcтво связных компонент: {comps}")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
