#!/usr/bin/python3
"""  It list all states from database """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = db_con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    db = cursor.fetchall()
    for row in db:
        print(row)
    cursor.close()
    db.close()
