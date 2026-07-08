import sqlite3
import settings as s

connection = sqlite3.connect("flappybird_database.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS flappy_birdScore(
                sn INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                high_score INTEGER)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS flappy_birdLogin(
                sn INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                password TEXT)
""")

def save_high_score(current_user):
    cursor.execute("""UPDATE flappy_birdScore SET high_score = ? WHERE user_id = ?""",(s.high_score,current_user))
    connection.commit()