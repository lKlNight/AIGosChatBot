
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


def fetch_data():
    cursor.execute('''SELECT * FROM dialogs_history''')
    data = cursor.fetchall()
    return data

def lerning_request():
    cursor.execute('''SELECT request FROM dialogs_history LIMIT 1''')
    data = cursor.fetchone()
    return data

def lerning_answer():
    cursor.execute('''SELECT answer FROM dialogs_history LIMIT 1''')
    data = cursor.fetchone()
    return data

def create_entry(request, answer):
    cursor.execute('''INSERT INTO dialogs_history (request, answer) 
                    VALUES (%s, %s)''', (request, answer))
    conn.commit()


def delete_entry():
    cursor.execute('''DELETE FROM dialogs_history 
                    WHERE request = %s''', ("Тестовое сообщение",))
    conn.commit()
    return 'Data deleted successfully'