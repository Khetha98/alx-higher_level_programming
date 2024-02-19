#!/usr/bin/python3
"""  it lists sttes from the database """

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Access to the database and get states
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
