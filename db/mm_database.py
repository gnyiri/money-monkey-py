import threading
from PyQt5 import QtSql
from util.mm_logger import MMLogger


class MMDatabase(object):
    _INST_LOCK = threading.Lock()
    _INSTANCE = None

    @classmethod
    def get_instance(cls):
        """ Method for getting the only instance """
        if cls._INSTANCE is None:
            with cls._INST_LOCK:
                if cls._INSTANCE is None:
                    cls._INSTANCE = MMDatabase()
        assert cls._INSTANCE is not None
        return cls._INSTANCE

    def __new__(cls, *args, **kwargs):
        """ To make sure there will be only one instance """
        if not isinstance(cls._INSTANCE, cls):
            cls._INSTANCE = object.__new__(cls, *args, **kwargs)
        return cls._INSTANCE

    def __init__(self):
        self._logger = MMLogger.get_instance()
        self._logger.info("Open database")
        self._database_url = "database.db"
        self._database = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self._database.setDatabaseName(self._database_url)

    def init_db(self):
        statements = list()
        statements.append("""DROP TABLE account_type;""")
        statements.append("""DROP TABLE `account`;""")
        statements.append("""DROP TABLE `transaction`;""")
        statements.append("""DROP TABLE `transaction_type`;""")

        statements.append("""CREATE TABLE account_type (id INTEGER, name TEXT, PRIMARY KEY(id));""")
        statements.append("""CREATE TABLE `account` (`id` INTEGER, `name` TEXT, `initial_balance` INTEGER, `account_type_id` INTEGER, PRIMARY KEY(id));""")
        statements.append("""CREATE TABLE `transaction_type` (`id` INTEGER, `name` TEXT, PRIMARY KEY(id));""")
        statements.append("""CREATE TABLE `transaction` (`id` INTEGER, `name` TEXT, `date` TEXT, `transaction_type_id` INTEGER, PRIMARY KEY(id));""")

        for statement in statements:
            query = QtSql.QSqlQuery()
            ok = query.exec_(statement)
            if not ok:
                self._logger.info("Database initialization failed! %s", self._database.lastError().text())
                return

        self._logger.info("Database creation done!")

    def execute_sql(self, statement):
        query = QtSql.QSqlQuery()
        ok = query.exec_(statement)

        if not ok:
            self._logger.error("SQL statement %s failed!", statement)
