#!/usr/bin/python3
"""display all values in the states table"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], port=3305, host="localhost",
                         paswd=sys.argv[2], db=sys.argv[3])
    c = dc.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
            id ASC".format(sys.argv[4]))
    states = c.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    c.close()
    db.close()
