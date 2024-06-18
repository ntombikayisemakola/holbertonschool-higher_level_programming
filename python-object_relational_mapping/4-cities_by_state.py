#!/usr/bin/python3

"""
A script that lists all cities from the database hbtn_0e_4_usa.
Username, password, and database name are given as user args.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)
        
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    sql = """SELECT cities.id, cities.name, states.name
             FROM cities
             JOIN states ON cities.state_id = states.id
             ORDER BY cities.id ASC"""
    
    cursor.execute(sql)
    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()

