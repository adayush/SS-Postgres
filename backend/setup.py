import psycopg

# from schema import PostgresSettings
from constants import CREATE_DB, CREATE_TABLE

with psycopg.connect(f"host=postgres port=5432 dbname=sharpsell user=postgres password=postgres") as conn:
    conn.autocommit = True
    with conn.cursor() as cur:

        # Execute a command: this creates a new table
        # cur.execute(CREATE_DB)
        cur.execute(CREATE_TABLE)
        for item in cur.execute("SELECT * FROM orders;").fetchall():
            print(item)

        conn.commit()
