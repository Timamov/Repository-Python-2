import psycopg2

PGHOST='ep-super-field-a20ay3ih-pooler.eu-central-1.aws.neon.tech'
PGDATABASE='neondb'
PGUSER='neondb_owner'
PGPASSWORD='npg_ov5L2JBFdyXT'
PORT=5432


PGHOST = 'ep-divine-smoke-a26bo7d2-pooler.eu-central-1.aws.neon.tech'
PGDATABASE = 'neondb'
PGUSER = 'neondb_owner'
PGPASSWORD = 'npg_ly1wBZkHW7mg'

with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as connection:
    with connection.cursor() as cursor:
        query = '''
        CREATE TABLE IF NOT EXISTS topic( 
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        )
        '''
        cursor.execute(query)
        query = '''
        CREATE TABLE IF NOT EXISTS "user"(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            description VARCHAR(50) NOT NULL
        )
        '''
        cursor.execute(query)
        query = '''
        CREATE TABLE IF NOT EXISTS posts(
            id SERIAL PRIMARY KEY,
            id_topic INTEGER REFERENCES topic (id),
            id_user INTEGER REFERENCES "user"(id),
            message VARCHAR(50) NOT NULL
        )
        '''

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

       # query_insert = 'INSERT INTO topic (name) VALUES (%s)'
       # cursor.execute(query_insert, ('What`s the time?',))
       # query_insert = 'INSERT INTO "user" (name, description) VALUES (%s, %s)'
       # cursor.execute(query_insert, ('Alex', 'I use messages'))
      # query_insert = 'INSERT INTO posts (id_topic, id_user, message) VALUES (%s, %s, %s)'
      # cursor.execute(query_insert, (1, 2, 'I\'m in Tokyo and now is morning',))
        pass

with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as connection:
    with connection.cursor() as cursor:
               query = """
                   CREATE TABLE IF NOT EXISTS brand (
                       id SERIAL PRIMARY KEY,
                       name VARCHAR(50) UNIQUE NOT NULL
                   )
               """
               cursor.execute(query)

               query = """
                   CREATE TABLE IF NOT EXISTS customer (
                       id SERIAL PRIMARY KEY,
                       name VARCHAR(50) NOT NULL
                   );

                   CREATE TABLE IF NOT EXISTS car (
                       id SERIAL PRIMARY KEY,
                       model VARCHAR(50) NOT NULL,
                       cost INTEGER,
                       brand_id INTEGER REFERENCES brand(id),
                       customer_id INTEGER REFERENCES customer(id)
                   );
               """
               cursor.execute(query) # 1



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

