#!/usr/bin/python3

import MySQLdb
import sqlalchemy
import sys

def mysqlconnect():
    db_connection= MySQLdb.connect(
        host="Localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    cirsort = db_connection.cursor()
    cirsort.execute("SELECT * from states ORDER BY states.id ASC;")
    listed = cirsort.fetchall()
    for element in listed:
        print(element)
    db_connection.close()

if __name__ == '__main__':
    mysqlconnect()
