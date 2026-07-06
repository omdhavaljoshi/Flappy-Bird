import pygame
import settings as s

def draw_button(rectButton,color):
    pygame.draw.rect(s.screen,color,rectButton)
    
def draw_game_screen():
    s.screen.blit(s.bg,(0,0))
    s.screen.blit(s.ground,(s.ground_x,s.ground_y))
    s.player_group.draw(s.screen)
    s.obstacle_group.draw(s.screen)
    score_font = s.font.render(f"{int(s.score)}", False,(0,0,0))
    if s.score == s.high_score and s.score != 0:
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
        new_score = s.font.render("New High Score!",False,(239,191,6))
    s.screen.blit(score,(s.width-430,s.height-380))
    s.screen.blit(high_score,(s.width-430,s.height-330))
    s.screen.blit(new_score,(s.width-450,s.height-280))
    
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
            s.current_screen = s.GAME_SCREEN
        if s.quit_button.collidepoint(mousePos):
            s.running = False