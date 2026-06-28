import pygame
import settings as s

def draw_button(rectButton,color):
    pygame.draw.rect(s.screen,color,rectButton)
    # label = s.font.render(text,True,"White")
    # coordinates = label.get_rect(center = rectButton.center)
    # s.screen.blit(label,coordinates)

def draw_game_screen():
    s.screen.blit(s.bg,(0,0))
    s.screen.blit(s.ground,(s.ground_x,s.ground_y))
    s.player_group.draw(s.screen)

def draw_puase_screen():
    s.screen.fill(s.bg_colour)
    draw_button(s.resume_button,"black")
    draw_button(s.quit_button,"black")
    s.screen.blit(s.resume_btn_img,(300,300))
    s.screen.blit(s.quit_btn_img,(300,400))
    title = s.font.render("Game Paused", True, "Black")
    s.screen.blit(title, (300,250))

def set_screen_logic(mousePos):
    if s.current_screen == s.PAUSE_SCREEN:
        if s.resume_button.collidepoint(mousePos):
            s.playing = True
            s.current_screen = s.GAME_SCREEN
        if s.quit_button.collidepoint(mousePos):
            s.running = False