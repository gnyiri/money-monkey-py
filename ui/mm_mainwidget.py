from PyQt5.QtWidgets import QWidget


class MMMainWidget(QWidget):

    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.setMinimumSize(600, 400)
