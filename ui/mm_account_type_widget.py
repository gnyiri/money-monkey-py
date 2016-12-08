from PyQt5.Qt import QWidget, QTableView, QVBoxLayout, QHBoxLayout, QPushButton, QAbstractItemView
from model.mm_account_type_model import MMAccountTableModel
from .mm_dialogs import MMAddNewAccountTypeDialog
from util.mm_base import MMBase


class MMAccountTypeWidget(QWidget, MMBase):

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        MMBase.__init__(self)

        main = QVBoxLayout()
        self.model = MMAccountTableModel(self)
        self.view = QTableView(self)
        self.view.setModel(self.model)
        self.view.setSelectionBehavior(QTableView.SelectRows)
        self.view.setAlternatingRowColors(True)
        self.view.verticalHeader().setVisible(False)
        self.view.setColumnHidden(0, True)
        main.addWidget(self.view)
        horizontal = QHBoxLayout()
        add_new_item_button = QPushButton("Add new item")
        add_new_item_button.clicked.connect(self.add_account_type)
        horizontal.addWidget(add_new_item_button)
        main.addLayout(horizontal)
        self.setLayout(main)

    def add_account_type(self):
        dialog = MMAddNewAccountTypeDialog(self)
        if dialog.exec_() == MMAddNewAccountTypeDialog.Accepted:
            pass
