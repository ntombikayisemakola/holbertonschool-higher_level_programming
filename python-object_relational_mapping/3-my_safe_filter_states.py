#!/usr/bin/python3

"""
A script that lists all states from the database hbtn_0e_0_usa
where the name matches the argument and is safe from SQL injection.
Username, password, database name, and state name are given as user args.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state name searched>".format(sys.argv[0]))
        sys.exit(1)
        
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    sql = """SELECT * FROM states
             WHERE name = %s
             ORDER BY id ASC"""
    
    cursor.execute(sql, (sys.argv[4],))
    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
