from sqlalchemy.orm import sessionmaker
from util.db import User
from util.db import ENGINE

session = sessionmaker(bind=ENGINE)()

def insert(user, password):
    try:
        user = User(user, password)
        session.add(user)
        session.commit()
    except Exception as e:
        print(e)


def update(user, field, value):
    session.query(User).filter(User.username == user).update({field: value})
    session.commit()


def delete(value):
    session.query(User).filter(User.username == value).delete()
    session.commit()


def read_all():
    result = [r.username for r in session.query(User).all()]
    print(f"result is {result}")

def read_one(value):
    result= session.query(User).filter_by(username=value).first()
    print(result.password)
