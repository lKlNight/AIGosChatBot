import psycopg2 as pg

try:
    conn = pg.connect(
        host='localhost',
        database='db_for_chatbot',
        port=5433,
        user='postgres',
        password='pass123'
    )

    cursor = conn.cursor()
    print("Connection established.")

except Exception as err:
    print("Something went wrong.")
    print(err)

sql = '''COPY demo FROM  
        'C:\\Users\\DELL\\Downloads\\Demo_data.csv'  
        DELIMITER ',' TXT HEADER'''

# executing above query
cursor.execute(sql)

# Display the table
cursor.execute('SELECT * FROM demo')
print(cursor.fetchall())

# Closing the connection
conn.close()