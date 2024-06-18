#!/usr/bin/python3
import sys
import MySQLdb

def list_cities(mysql_username, mysql_password, db_name):
    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query
        query = """
        SELECT cities.id, cities.name, states.name 
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """
        cursor.execute(query)

        # Fetch all the results
        results = cursor.fetchall()

        # Print each row in the specified format
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error {e}")
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <mysql_username> <mysql_password> <db_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    list_cities(mysql_username, mysql_password, db_name)
