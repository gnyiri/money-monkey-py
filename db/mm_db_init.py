from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


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

engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)
