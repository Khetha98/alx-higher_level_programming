#!/usr/bin/python3
"""  it lists sttes from the database """

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Access to the database and get states
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    db_cursor = db.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    rows_selected = db_cursor.fetchall()

    for i in rows_selected:
        print(i)
