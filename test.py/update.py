import psycopg2
from config import config

def update_user(user_id, name):
    sql = """
    update phonebook
    set user_id = %s
    where name = %s;
    """
    conn = None
    try: 
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_id, name))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

update_user(3, 'Berek')