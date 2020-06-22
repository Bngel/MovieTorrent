import sys
from MovieSource import *
from PyQt5.QtWidgets import QApplication,QMainWindow

class Movie(QMainWindow,Ui_MovieSource):
    def __init__(self,parent=None):
        super(Movie, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    movie = Movie()
    movie.show()
    sys.exit(app.exec_())