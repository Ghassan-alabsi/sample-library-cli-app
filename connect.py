#!/usr/bin/python
import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
                host="localhost",
                database="Group2DB",
                user="postgres",
                password="postgres")

		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        # print('PostgreSQL database version:')
        # cur.execute('SELECT * FROM public."book"')
        

        # display the PostgreSQL database server version
        # db_version = cur.fetchall()
        # print(db_version)
        # for i in db_version:
        #     print(i)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()