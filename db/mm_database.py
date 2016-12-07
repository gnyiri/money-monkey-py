import threading
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from util.mm_logger import MMLogger

Base = declarative_base()


class AccountType(Base):
    __tablename__ = "account_type"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    initial_balance = Column(Integer, nullable=False)
    account_type_id = Column(Integer, ForeignKey('account_type.id'))
    account_type = relationship(AccountType)


class TransactionType(Base):
    __tablename__ = "transaction_type"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    date = Column(String(255), nullable=False)
    value = Column(Integer, nullable=False)
    transaction_type_id = Column(Integer, ForeignKey('transaction_type.id'))
    transaction_type = relationship(TransactionType)


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
        self._database_url = "sqlite:///database.db"
        self._engine = create_engine(self._database_url)

    def init_db(self):
        Base.metadata.create_all(self._engine)

    def insert_account_type(self, account_type_instance):
        DB
