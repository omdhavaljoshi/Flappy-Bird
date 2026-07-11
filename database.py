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

cursor.execute("""
CREATE TABLE IF NOT EXISTS latest_user(
                user_id TEXT)
""")
cursor.execute("""SELECT user_id FROM latest_user""")
last_user = cursor.fetchone()
# print(last_user)
# if len(last_user) == 0:
#     cursor.execute("""INSERT INTO latest_user(user_id) VALUES(?)""", ("",))

def save_high_score(current_user):
    cursor.execute("""UPDATE flappy_birdScore SET high_score = ? WHERE user_id = ?""",(s.high_score,current_user))
    print(f"high score saved for {current_user}:{s.high_score}")
    connection.commit()

def latest_user():
    cursor.execute("""SELECT user_id FROM latest_user""")
    user = cursor.fetchone()
    # print(user)
    if user is None:
        # print("test")
        return None
    else:
        # print(user)
        return user[0]