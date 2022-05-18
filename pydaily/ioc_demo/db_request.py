#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sqlite3

from injector import inject, singleton, Module, provider, Injector


class DbRequestHandler:

    @inject
    def __init__(self, db: sqlite3.Connection):
        self.db = db

    def get(self):
        cursor = self.db.cursor()
        cursor.execute('select key,value from data order by key')
        return cursor.fetchall()


class DBConfig:
    def __init__(self, conn_str: str):
        self.conn_str = conn_str


def config_binding(binder):
    config = DBConfig(':memory:')
    binder.bind(DBConfig, to=config, scope=singleton)


class DatabaseModule(Module):
    @singleton
    @provider
    def provide_sqlite_connection(self, configuration: DBConfig) -> sqlite3.Connection:
        conn = sqlite3.connect(configuration.conn_str)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS data (key PRIMARY KEY, value)')
        cursor.execute('INSERT OR REPLACE INTO data VALUES ("hello", "world")')
        return conn



