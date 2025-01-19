import sqlite3

def init_db():
    conn = sqlite3.connect('reminders.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            datetime TEXT NOT NULL,
            status TEXT DEFAULT 'pending'
        )
    ''')
    conn.commit()
    conn.close()

def add_reminder(title, datetime):
    conn = sqlite3.connect('reminders.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO reminders (title, datetime) VALUES (?, ?)', (title, datetime))
    conn.commit()
    conn.close()

def get_reminders():
    conn = sqlite3.connect('reminders.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reminders')
    reminders = cursor.fetchall()
    conn.close()
    return reminders