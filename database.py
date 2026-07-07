import sqlite3
import settings as s

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS flappy_bird_score(
                sn INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                high_score INTEGER)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS flappy_bird_login(
                sn INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                password TEXT)
""")

def save_high_score(current_user):
    cursor.execute("""UPDATE flappy_bird_score SET high_score = ? WHERE user_id = ?""",(s.high_score,current_user))
    connection.commit()