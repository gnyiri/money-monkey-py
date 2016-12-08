from PyQt5.QtWidgets import QWidget, QTabWidget
from PyQt5.Qt import QVBoxLayout
from model.mm_account_type_model import MMAccountTableModel
from .mm_account_type_widget import MMAccountTypeWidget


class MMMainWidget(QWidget):

    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.setMinimumSize(600, 400)
        layout = QVBoxLayout()
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setTabPosition(QTabWidget.West)
        self.tab_widget.addTab(MMAccountTypeWidget(self), "Account types")
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)
