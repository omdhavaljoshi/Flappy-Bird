import pygame
import settings as s

def draw_button(rectButton,color):
    pygame.draw.rect(s.screen,color,rectButton)
    
def draw_game_screen():
    s.screen.blit(s.bg,(0,0))
    s.screen.blit(s.ground,(s.ground_x,s.ground_y))
    s.player_group.draw(s.screen)
    s.obstacle_group.draw(s.screen)
    score = s.font.render(f"{s.score//2}", False,(0,0,0))
    s.screen.blit(score, (s.width-250,s.height-750))

def draw_puase_screen():
    s.screen.fill(s.bg_colour)
    draw_button(s.resume_button,"black")
    draw_button(s.quit_button,"black")
    s.screen.blit(s.resume_btn_img,(s.width-350,s.height-600))
    s.screen.blit(s.quit_btn_img,(s.width-350,s.height-500))
    title = s.font.render("Game Paused", True, "Black")
    s.screen.blit(title, (s.width-400,s.height-700))

def draw_game_over_screen():
    s.screen.fill(s.bg_colour)

def set_screen_logic(mousePos):
    if s.current_screen == s.PAUSE_SCREEN:
        if s.resume_button.collidepoint(mousePos):
            s.playing = True
            s.current_screen = s.GAME_SCREEN
        if s.quit_button.collidepoint(mousePos):
            s.running = False