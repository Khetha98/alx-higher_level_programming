#!/usr/bin/python3
"""
list all states from database
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db.cursor()

    db_cursor.execute("SELECT * FROM states")

    rows_selected = db_cursor.fetchall()

    for i in rows_selected:
        print(i)
