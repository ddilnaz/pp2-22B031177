import psycopg2
from config import config

def create_table():
    commands = (
        """
        CREATE TABLE phonebook (
            user_id serial PRIMARY KEY,
            name VARCHAR (50) UNIQUE NOT NULL,
            phone_number text
        )
        """
    )

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(commands)
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

create_table()