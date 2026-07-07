import pygame
import settings as s

def draw_button(rectButton,color):
    pygame.draw.rect(s.screen,color,rectButton)

def drawInput(rect,text,active):
    print(active)
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
    if s.score == s.high_score and s.new_high_score == False:
        so_close = s.font.render("So Close!",False,(59, 67, 227))
        s.screen.blit(so_close,(s.width-370,s.height-280))
    s.screen.blit(score,(s.width-430,s.height-380))
    s.screen.blit(high_score,(s.width-430,s.height-330))

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
    if s.current_screen == s.SIGN_UP_SCREEN:
        if s.username_box.collidepoint(mousePos):
            s.active_input = "usernamebox"
        if s.password_box.collidepoint(mousePos):
            s.active_input = "passwordbox"