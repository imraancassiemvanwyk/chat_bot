import schedule
import time
import sqlite3
from datetime import datetime


def check_reminders():
    conn = sqlite3.connect('reminders.db')
    cursor = conn.cursor()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor.execute("SELECT title FROM reminders WHERE datetime = ? AND status = 'pending'", (current_time,))
    due_reminders = cursor.fetchall()

    for reminder in due_reminders:
        print(f"Reminder Alert: {reminder[0]}")
        cursor.execute("UPDATE reminders SET status = 'completed' WHERE title = ?", (reminder[0],))

    conn.commit()
    conn.close()


def start_scheduler():
    schedule.every(1).minute.do(check_reminders)
    while True:
        schedule.run_pending()
        time.sleep(1)