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
        s.current_screen = s.AUTH_SCREEN
        db.connection.commit()

def sign_in(username,password):
    db.cursor.execute("""SELECT * FROM flappy_birdLogin WHERE password = ? AND user_id = ?""",(password,username))
    accounts = db.cursor.fetchall()
    if len(accounts) != 0:
        s.current_user = username
        print("successfully signed in")
        s.sign_in_successful = True
        s.current_screen = s.GAME_SCREEN
        db.cursor.execute("""SELECT high_score FROM flappy_birdScore WHERE user_id = ?""",(username,))
        score = db.cursor.fetchall()
        list_score = list(score[0])
        s.high_score = list_score.pop(0)
        print(s.high_score)
    else:
        s.sign_in_successful = False
        print("username or password is incorrect")