#!/usr/bin/env python
# -*- coding:utf-8 -*-
from attr import dataclass
from injector import inject
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declared_attr, declarative_base

from . import config


@inject
@dataclass
class Database:
    engine = create_engine(config.DATABASE_URL, connect_args={"check_same_thread": False})
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = Session()


class CustomBase(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=CustomBase)
