import csv
import psycopg2
from config import config

conn = None
params = config()
conn = psycopg2.connect(**params)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS info(name text, email text)")

with open('1.csv', 'r') as f:
    cur.copy_from(f, 'info', sep=',')
    cur.close()
    conn.commit()


f.close()