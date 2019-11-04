from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from sip import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    print("Qt5 Version Number is: {0}".format(QT_VERSION_STR))
    print("PyQt5 Version is: {}".format(PYQT_VERSION_STR))
    print("Sip Version is: {}".format(SIP_VERSION_STR))
    #sys.exit(app.exec_())
