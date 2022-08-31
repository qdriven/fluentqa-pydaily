#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1. database connection
2. database operation
3. operation:  simple
4. orm: Object Relationship Management
"""
from datetime import date
from typing import Any

from sqlalchemy import *
from sqlalchemy.future import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

"""
1. engine: conenction
2. Base: BaseModel
3. Sessions: SessionsFactory
"""
Base = declarative_base()
engine = create_engine("sqlite:///demo.sqlite", echo=True, future=True)
_SessionFactory = sessionmaker(bind=engine)


def session_factory():
    """
    1. create tables
    2. return session
    Returns:

    """
    Base.metadata.create_all(engine)
    return _SessionFactory()


meta_data = MetaData()
users = Table('users', meta_data,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('fullname', String),
              )
meta_data.create_all(engine)


def manual_create_table():
    ins = users.insert().values(name='Test', fullname='fullname')
    engine.connect().execute(ins)
    print(ins)


class Person(Base):
    """
    ORM: object relationship mapping
    """
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_of_birth = Column(Date)
    height = Column(Integer)
    weight = Column(Integer)

    def __init__(self, name, date_of_birth, height, weight, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.name = name
        self.date_of_birth = date_of_birth
        self.height = height
        self.weight = weight

    @classmethod
    def select(cls, **kwargs):
        print(cls)
        s = select(cls)
        return engine.connect().execute(s)

    @staticmethod
    def static_select(**kwargs):
        s = select(Person)
        return engine.connect().execute(s)

def get_people():
    session = session_factory()
    q = session.query(Person)
    return q.all()

def create_people():
    try:
        session = session_factory()
        bruno = Person("Bruno Krebs", date(1984, 10, 20), 182, 84.5)
        john = Person("John Doe", date(1990, 5, 17), 173, 90)
        session.add(bruno)
        session.add(john)
        session.commit()
    except Exception as e:
        print(e)
    finally:
        session.close()

def textual_sql_demo():
    t = text("select * from users")
    return engine.connect().execute(t)

def textural_sql_binding_parameters():
    t = text("select * from person where :name")
    return engine.connect().execute(t,{"name":'John'})

def main():
    create_people()



if __name__ == '__main__':
    # manual_create_table()
    # main()

    result = Person.select()
    print(result)
    r = Person.static_select()
    print(r)
    for item in result:
        print(item)
    # select_clause = select(users,Person).where(users.c.name==Person.c.name)
    # print(select_clause)
    s = textual_sql_demo()
    print(s)
    sr = textural_sql_binding_parameters()
    print(sr)
    persons = get_people()
    for person in persons:
        print(type(person))
        print(person.name,person.height,person.weight)
