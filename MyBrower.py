from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys


class MainWindow(QMainWindow):
    myTitle = '首页'
    myUrl = 'https://www.qq.com'

    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()

    def load(self):
        self.setWindowTitle(self.myTitle)
        self.browser.load(QUrl(self.myUrl))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    num = len(sys.argv)
    if num > 1:
        win.myUrl = sys.argv[1]
    if num > 2:
        win.myUrl = sys.argv[1]
        win.myTitle = sys.argv[2]
    win.load()
    win.showFullScreen()
    sys.exit(app.exec_())
