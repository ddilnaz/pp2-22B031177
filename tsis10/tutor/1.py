from config import config
import psycopg2

def connect():
    # Connect to the PostgreSQL database server
    conn = None
    try:
        # reading connection parmeters
        parameters = config()
        # connecting to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**parameters)
        # creating the cursor
        cur = conn.cursor()
        # checking the version
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        # displaying the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


connect()