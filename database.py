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

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS latest_user(
#                 user_id TEXT)
# """)
# cursor.execute("""SELECT user_id FROM latest_user""")
# last_user = cursor.fetchall()
# if len(last_user) == 0:
#     cursor.execute("""INSERT INTO latest_user(user_id) VALUES(?)""", (None,))

def save_high_score(current_user):
    cursor.execute("""UPDATE flappy_birdScore SET high_score = ? WHERE user_id = ?""",(s.high_score,current_user))
    print(f"high score saved for {current_user}:{s.high_score}")
    connection.commit()

def latest_user():
    cursor.execute("""SELECT user_id FROM latest_user""")
    user = cursor.fetchone()
    print(user)
    if user[0][0] == None:
        return None
    else:
        return user[0][0]