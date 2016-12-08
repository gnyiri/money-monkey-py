from PyQt5.Qt import QDialog, QDialogButtonBox, QFormLayout, QCheckBox, QLineEdit, QVBoxLayout, QDataWidgetMapper
from PyQt5.QtSql import QSqlTableModel
from model.mm_account_type_model import MMAccountTableModel


class MMAddNewAccountTypeDialog(QDialog):
    """
    Dialog for setting global parameters
    """
    def __init__(self, parent):
        QDialog.__init__(self, parent)

        self.setWindowTitle("Add new account type")
        self.model = MMAccountTableModel(self)

        layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        self.name = QLineEdit()

        form_layout.addRow("Name: ", self.name)
        layout.addLayout(form_layout)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.ok_clicked)
        self.button_box.rejected.connect(self.cancel_clicked)

        layout.addLayout(form_layout)
        layout.addWidget(self.button_box)
        self.setLayout(layout)

    def ok_clicked(self):
        print("ok clicked")
        row = self.model.rowCount()
        self.model.insertRow(row)
        self.model.setData(self.model.index(row, 1), self.name.text())
        self.model.submit()
        QDialog.accept(self)

    def cancel_clicked(self):
        QDialog.reject(self)
