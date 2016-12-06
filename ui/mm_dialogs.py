from PyQt5.Qt import QDialog, QDialogButtonBox, QFormLayout, QCheckBox, QLineEdit, QVBoxLayout


class MMAddNewAccountTypeDialog(QDialog):
    """
    Dialog for setting global parameters
    """
    def __init__(self, parent):
        QDialog.__init__(self, parent)

        self.setWindowTitle("Add new account type")
        self.setMinimumHeight(200)
        self.setMinimumWidth(200)

        layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        self.name = QLineEdit()
        form_layout.addRow("Name: ", self.name)
        layout.addLayout(form_layout)
        self.setLayout(layout)

    def ok_clicked(self):
        QDialog.accept(self)

    def cancel_clicked(self):
        QDialog.reject(self)
