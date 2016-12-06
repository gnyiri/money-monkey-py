import sys
import argparse
import logging
from PyQt5.Qt import QApplication
from ui.mm_mainwindow import MMMainWindow


if __name__ == '__main__':

    APP = QApplication(sys.argv)
    ui = MMMainWindow()
    ui.show()
    sys.exit(APP.exec_())