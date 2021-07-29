import psycopg2
import os

db_host = os.getenv('dev_db_host')
db_name = os.getenv('dev_db_name')
db_user = os.getenv('dev_db_username')
db_password = os.environ.get('dev_db_password')

print(f"dbname={db_name} user={db_user} password={db_password} host={db_host}")

# Connect to your postgres DB
conn = psycopg2.connect(f"dbname={db_name} user={db_user} password={db_password} host={db_host}")
SQL1 = "select * from people.person;"

with conn:
    with conn.cursor() as curs:
        curs.execute(SQL1)
        records = curs.fetchall()

    for rec in records:
        print(rec)

# leaving contexts doesn'   t close the connection
conn.close()