#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa.
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    query = """
            SELECT cities.name
            FROM cities, states
            WHERE cities.state_id = states.id AND states.name = %s
            ORDER BY cities.id ASC"""

    cur.execute(query, (argv[4],))

    rows = cur.fetchall()

    city_names = [row[0] for row in rows]

    print(", ".join(city_names))

    cur.close()
    db.close()
