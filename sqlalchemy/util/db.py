from sqlalchemy import Column, String, Integer, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_INFO = {
    "host": "127.0.0.1",
    "user": "root",
    "passwd": "",
    "port": 3306,
    "db": "pytest",
    "pool_size": 10,
}

ENGINE = create_engine(
    'mysql+pymysql://',
    connect_args={
        "host": DB_INFO["host"],
        "user": DB_INFO["user"],
        "passwd": DB_INFO["passwd"],
        "port": DB_INFO["port"],
        "db": DB_INFO["db"],
        "charset": "utf8",
    },
    pool_size=DB_INFO["pool_size"])

session = sessionmaker(bind=ENGINE)()
Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    username = Column(String, primary_key=True)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password
