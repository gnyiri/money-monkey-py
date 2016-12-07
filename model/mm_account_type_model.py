from PyQt5 import QtSql
from PyQt5 import QtCore


class MMAccountTableModel(QtSql.QSqlTableModel):
    def __init__(self, parent):
        QtSql.QSqlTableModel.__init__(self, parent)
        self.setTable("account_type")
        self.setEditStrategy(QtSql.QSqlTableModel.OnRowChange)
        self.setHeaderData(0, QtCore.Qt.Horizontal, "id")
        self.setHeaderData(1, QtCore.Qt.Horizontal, "name")
        self.select()
