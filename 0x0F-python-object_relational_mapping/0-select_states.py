#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":

    db_connect = MYSQLdb.connect(
        host="localhost", user=argv[1], port =3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states")

    rows = db_cursor.fetchall

    for row in rows:
        print(row)
