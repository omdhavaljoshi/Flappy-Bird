# Imports -->
import pygame
import os
import obstacle as o

dir = os.path.dirname(__file__)
height,width = 900,800
fps = 60
clock = pygame.time.Clock()
screen = None
running = True
background_img = os.path.join(dir,r"Images/bg.png")
bg = None
ground_img = os.path.join(dir,r"Images/ground.png")
ground = None
ground_x = 0
ground_y = 750
scroll_speed = 4
playing = False
GAME_SCREEN = "game screen"
PAUSE_SCREEN = "pause screen"
current_screen = GAME_SCREEN
player_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
flappy = None
obstacle = o.Obstacle()
is_jumping = False
game_over = False
bg_colour = (100,224,117)
resume_button = pygame.Rect(300,300,200,60)
quit_button = pygame.Rect(300,400,200,60)
resume_img = os.path.join(dir,r"Images/resume.png")
quit_img = os.path.join(dir,r"Images/quit.png")
resume_btn_img = None
quit_btn_img = None
font = pygame.font.Font(None,40)
spawn_obstacle = pygame.USEREVENT + 1