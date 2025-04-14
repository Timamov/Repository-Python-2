import psycopg2

PGHOST='ep-super-field-a20ay3ih-pooler.eu-central-1.aws.neon.tech'
PGDATABASE='neondb'
PGUSER='neondb_owner'
PGPASSWORD='npg_ov5L2JBFdyXT'
PORT=5432

with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as connection:
    with connection.cursor() as cursor:
        query = '''
        CREATE TABLE IF NOT EXISTS brand (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        );
        CREATE TABLE IF NOT EXISTS customer(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        );
        CREATE TABLE IF NOT EXISTS car (
            id SERIAL PRIMARY KEY,
            model VARCHAR(50) UNIQUE NOT NULL,
            cost INTEGER,
            brand_id INTEGER REFERENCES brand(id),
            customer_id INTEGER REFERENCES customer(id)
        )            
            '''
        cursor.execute(query)

with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as connection:
    with connection.cursor() as cursor:


    # query_insert = 'INSERT INTO brand (name) VALUES (%s)'
    #result1 = cursor.execute(query_insert, ('BMW',))
    # print(result1)

    # query_insert = 'INSERT INTO owner (name) RETURNING id, name '
    # owners = [
    #     ('Max',),
    #     ('Boyko',),
    #     ('Alex',)
    # ]
    # cursor.executemany(cursor)