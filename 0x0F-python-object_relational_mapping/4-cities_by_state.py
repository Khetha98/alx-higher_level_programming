#!/usr/bin/python3
"""  it list all states from database """
import MySQLdb
import sys


if __name__ == "__main__":
    db_connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db_connect.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db_connect.close()
