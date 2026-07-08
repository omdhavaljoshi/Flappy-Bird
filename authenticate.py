import settings as s
import database as db
import time

def sign_up(username,password):
    db.cursor.execute("""SELECT user_id FROM flappy_birdLogin""")
    user_ids = db.cursor.fetchall()
    print(user_ids,username)
    if (username,) in user_ids:
        print("username taken")
        s.account_created = False
    else:
        db.cursor.execute("""INSERT INTO flappy_birdLogin(user_id,password) VALUES(?,?)""",(username,password))
        db.cursor.execute("""INSERT INTO flappy_birdScore(user_id,high_score) VALUES(?,?)""", (username,0))
        print("accouunt created")
        s.account_created = True
        db.connection.commit()