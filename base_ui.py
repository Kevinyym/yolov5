import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window. show()
    app. exec()