from PyQt5.Qt import QMainWindow, QAction, QFileDialog, QIcon, QProgressBar, QPushButton, QTabWidget, QTableView
from util.mm_base import MMBase
from .mm_mainwidget import MMMainWidget
from .mm_dialogs import MMAddNewAccountTypeDialog


class MMMainWindow(QMainWindow, MMBase):
    """
    Main Window
    """
    def __init__(self):
        QMainWindow.__init__(self)
        MMBase.__init__(self)

        self.setWindowTitle("Money Monkey - Financial Manager")
        self.progressbar = None
        self.toolbar = None
        self.status_bar = None
        self.main_widget = None
        self.build_ui()
        self.show()

    def build_ui(self):
        self.main_widget = MMMainWidget(self)

        menu_bar = self.menuBar()
        action_menu = menu_bar.addMenu("&Actions")

        init_db_action = QAction("Initialize Database", self)
        init_db_action.triggered.connect(self.init_db)

        add_account_type_action = QAction("Add account type", self)
        add_account_type_action.setShortcut("Ctrl+A")
        add_account_type_action.triggered.connect(self.add_account_type)

        action_menu.addAction(init_db_action)
        action_menu.addAction(add_account_type_action)

        self.toolbar = self.addToolBar("Exit")
        self.status_bar = self.statusBar()
        self.progressbar = QProgressBar(self)
        self.progressbar.show()
        self.progressbar.setValue(0)
        self.progressbar.setRange(0, 100)
        self.progressbar.hide()
        self.status_bar.addPermanentWidget(self.progressbar)
        self.setCentralWidget(self.main_widget)

    def init_db(self):
        self.app.database.init_db()

    def add_account_type(self):
        dialog = MMAddNewAccountTypeDialog(self)
        if dialog.exec_() == MMAddNewAccountTypeDialog.Accepted:
            pass
