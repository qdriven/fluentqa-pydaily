#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sqlite3
from sqlite3 import Connection, Cursor


def get_sqlite_connection():
    return sqlite3.connect("demo.sqlite")


def get_cursor(conn: Connection):
    return conn.cursor()


def execute(cursor: Cursor, sql: str, **kwargs):
    return cursor.execute(sql, **kwargs)


if __name__ == '__main__':
    conn = get_sqlite_connection()
    print(conn)
    c = get_cursor(conn)
    print(c)
    result = execute(c,"select * from person")
    print(type(result))
    print(result)

    for item in result.fetchall():
        print(type(item))
        print(item)

    ## other sql
    execute(c,"CREATE TABLE if not exists movie(title, year, score)")

    insert_script="""
     INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
    """
    execute(c,insert_script)
    conn.commit()
    data = [
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's Life of Brian", 1979, 8.0),
    ]
    c.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
    conn.commit()
