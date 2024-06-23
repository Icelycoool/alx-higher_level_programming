#!/usr/bin/python3
import MySQLdb
from sys import argv
"""A script that lists all states from the database hbtn_0e_0_usa"""


if __name__ == "__main__":

    # Connecting tot he database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
