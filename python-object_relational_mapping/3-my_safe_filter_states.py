#!/usr/bin/python3
"""
module with one function used to connect
and display certain data from db
"""
import MySQLdb
import sys


def mysqlconnect():
    """
    the function that connect and display the
    state that have a N in first place int heir name
    and their id from the db
    """
    db_connection = MySQLdb.connect(
        host="Localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    cirsort = db_connection.cursor()
    if "'" not in sys.argv[4]:
        cirsort.execute("""SELECT * from states
            WHERE BINARY name = '{}'
            ORDER BY states.id ASC;""".format(sys.argv[4]))
        listed = cirsort.fetchall()
        for element in listed:
            print(element)
    db_connection.close()


if __name__ == '__main__':
    mysqlconnect()
