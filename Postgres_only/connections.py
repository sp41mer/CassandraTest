__author__ = 'sp41mer'
from models import *
import psycopg2

def create_tables():
    database.connect()
    database.create_tables([User,Group])

conn_string = "host='localhost' dbname='only_postgres_parcing' user='root' password='root'"
conn = psycopg2.connect(conn_string)
cur = conn.cursor()
cur.execute("create table users_and_friends (id SERIAL PRIMARY KEY, vk_id INT, friends INT[]);"
            "create table groups_and_users (id SERIAL PRIMARY KEY, vk_id INT, users INT[]);")
conn.commit()
cur.close()
conn.close()
create_tables()



