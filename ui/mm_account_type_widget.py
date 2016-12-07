from PyQt5.Qt import QWidget, QTableView, QVBoxLayout, QHBoxLayout, QPushButton
from model.mm_account_type_model import MMAccountTableModel
from .mm_dialogs import MMAddNewAccountTypeDialog
from util.mm_base import MMBase


class MMAccountTypeWidget(QWidget, MMBase):

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        MMBase.__init__(self)

        vbox_layout = QVBoxLayout()
        self.model = MMAccountTableModel(self)
        self.view = QTableView(self)
        self.view.setModel(self.model)
        vbox_layout.addWidget(self.view)
        hbox_layout = QHBoxLayout()
        add_new_item_button = QPushButton("Add new item")
        add_new_item_button.clicked.connect(self.add_account_type)
        hbox_layout.addWidget(add_new_item_button)
        vbox_layout.addLayout(hbox_layout)
        self.setLayout(vbox_layout)

    def add_account_type(self):
        dialog = MMAddNewAccountTypeDialog(self)
        if dialog.exec_() == MMAddNewAccountTypeDialog.Accepted:
            self.app.database.execute_sql("""INSERT INTO account_type (name) values('""" + dialog.name.text() + """'); """)
