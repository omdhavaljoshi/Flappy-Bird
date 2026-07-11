import pygame
import settings as s
import authenticate as a
import database as db

def draw_button(rectButton,color):
    pygame.draw.rect(s.screen,color,rectButton)

def drawInput(rect,text,active):
    color = "Black" if active == False else (182,150,18)
    pygame.draw.rect(s.screen,color,rect)
    s.rendered_text = s.font_2.render(text,False,"white")
    s.screen.blit(s.rendered_text,(rect.x+30,rect.y+15))
    
def draw_game_screen():
    s.screen.blit(s.bg,(0,0))
    s.screen.blit(s.ground,(s.ground_x,s.ground_y))
    s.player_group.draw(s.screen)
    s.obstacle_group.draw(s.screen)
    score_font = s.font.render(f"{int(s.score)}", False,(0,0,0))
    if s.new_high_score == True and s.score != 0:
        score_font = score_font = s.font.render(f"{int(s.score)}", False,(239,191,6))
    s.screen.blit(score_font, (s.width-250,s.height-750))

def draw_pause_screen():
    s.screen.fill(s.bg_colour)
    draw_button(s.resume_button,"black")
    draw_button(s.quit_button,"black")
    s.screen.blit(s.resume_btn_img,(s.width-350,s.height-600))
    s.screen.blit(s.quit_btn_img,(s.width-350,s.height-500))
    title = s.font.render("Game Paused", True, "Black")
    s.screen.blit(title,(s.width-400,s.height-700))

def draw_game_over_screen():
    s.screen.fill(s.bg_colour)
    title = s.font.render("Game Over", True, "Black")
    s.screen.blit(title,(s.width-375,s.height-700))
    draw_button(s.restart_button,"black")
    s.screen.blit(s.restart_btn_img,(s.width-350,s.height-600))
    draw_button(s.quit_button,"black")
    s.screen.blit(s.quit_btn_img,(s.width-350,s.height-500))
    draw_button(s.score_board,(242, 197, 114))
    score = s.font.render(f"Score: {int(s.score)}", False,(0,0,0))
    high_score = s.font.render(f"High Score: {int(s.high_score)}", False,(0,0,0))
    if s.new_high_score == True:
        new_score = s.font.render("New High Score!",False,(182,150,18))
        s.screen.blit(new_score,(s.width-450,s.height-280))
        db.save_high_score(s.current_user)
    if s.score == s.high_score and s.new_high_score == False:
        so_close = s.font.render("So Close!",False,(59, 67, 227))
        s.screen.blit(so_close,(s.width-370,s.height-280))
    s.screen.blit(score,(s.width-430,s.height-380))
    s.screen.blit(high_score,(s.width-430,s.height-330))
    draw_button(s.sign_out_button,"black")
    s.screen.blit(s.sign_out_btn_img,(s.width-350,s.height-200))

def draw_signup_screen():
    s.screen.fill(s.bg_colour)
    title = s.font.render("Sign Up", True, "black")
    s.screen.blit(title,(s.width-350,s.height-700))
    user_nameTitle = s.font_2.render("Username:", True,"Black")
    s.screen.blit(user_nameTitle,(40,s.height-600))
    drawInput(s.username_box,s.username_text,s.active_input == "usernamebox")
    passwordTitle = s.font_2.render("Password:", True,"Black")
    s.screen.blit(passwordTitle,(40,s.height-500))
    drawInput(s.password_box,s.password_text,s.active_input == "passwordbox")
    draw_button(s.sign_up_button,"black")
    s.screen.blit(s.sign_up_btn_img,(s.width-350,s.height-400))
    if s.account_created == True:
        created = s.font_2.render("Account created successfully",True,"red")
        s.screen.blit(created,(s.width-370,s.height-300))
    elif s.account_created == False:
        usernameWarning = s.font_2.render("User name already exists",True,"red")
        s.screen.blit(usernameWarning,(s.width-360,s.height-300))

def draw_signin_screen():
    s.screen.fill(s.bg_colour)
    title = s.font.render("Sign In", True, "black")
    s.screen.blit(title,(s.width-350,s.height-700))
    user_nameTitle = s.font_2.render("Username:", True,"Black")
    s.screen.blit(user_nameTitle,(40,s.height-600))
    drawInput(s.username_box,s.username_text,s.active_input == "usernamebox")
    passwordTitle = s.font_2.render("Password:", True,"Black")
    s.screen.blit(passwordTitle,(40,s.height-500))
    drawInput(s.password_box,s.password_text,s.active_input == "passwordbox")
    draw_button(s.sign_in_button2,"black")
    s.screen.blit(s.sign_in_btn_img,(s.width-350,s.height-400))
    if s.sign_in_successful == True:
        signed_in = s.font_2.render("Sign in sucessful",True,"red")
        s.screen.blit(signed_in,(s.width-370,s.height-300))
    elif s.sign_in_successful == False:
        usernameWarning = s.font_2.render("Username or password is incorrect",True,"red")
        s.screen.blit(usernameWarning,(s.width-450,s.height-300))

def draw_auth_screen():
    user = db.latest_user()
    print(user)
    if user is not None:
        db.cursor.execute("""SELECT password FROM flappy_birdLogin WHERE user_id = ?""",(user,))
        password = db.cursor.fetchone()
        a.sign_in(user,password[0])
    else:
        s.screen.fill(s.bg_colour)
        title = s.font.render("Flappy Bird", True, "black")
        s.screen.blit(title,(s.width-390,s.height-700))
        draw_button(s.sign_in_button,"black")
        s.screen.blit(s.sign_in_btn_img,(s.width-350,s.height-600))
        draw_button(s.sign_up_button2,"black")
        s.screen.blit(s.sign_up_btn_img,(s.width-350,s.height-500))
    
def set_screen_logic(mousePos):
    if s.current_screen == s.PAUSE_SCREEN:
        if s.resume_button.collidepoint(mousePos):
            s.playing = True
            s.current_screen = s.GAME_SCREEN
        if s.quit_button.collidepoint(mousePos):
            s.running = False
    if s.current_screen == s.GAME_OVER_SCREEN:
        if s.restart_button.collidepoint(mousePos):
            s.playing = False
            s.obstacle_group.empty()
            s.score = 0
            s.flappy.reset()
            s.new_high_score = False
            s.current_screen = s.GAME_SCREEN
        if s.quit_button.collidepoint(mousePos):
            s.running = False
        if s.sign_out_button.collidepoint(mousePos):
            a.sign_out()
    if s.current_screen == s.SIGN_UP_SCREEN:
        if s.username_box.collidepoint(mousePos):
            s.active_input = "usernamebox"
        if s.password_box.collidepoint(mousePos):
            s.active_input = "passwordbox"
        if s.sign_up_button.collidepoint(mousePos):
            a.sign_up(s.username_text,s.password_text)
            s.username_text = ""
            s.password_text = ""
    if s.current_screen == s.AUTH_SCREEN:
        if s.sign_in_button.collidepoint(mousePos):
            s.current_screen = s.SIGN_IN_SCREEN
        if s.sign_up_button2.collidepoint(mousePos):
            s.current_screen = s.SIGN_UP_SCREEN
    if s.current_screen == s.SIGN_IN_SCREEN:
        if s.username_box.collidepoint(mousePos):
            s.active_input = "usernamebox"
        if s.password_box.collidepoint(mousePos):
            s.active_input = "passwordbox"
        if s.sign_in_button2.collidepoint(mousePos):
            a.sign_in(s.username_text,s.password_text)
            s.username_text = ""
            s.password_text = ""