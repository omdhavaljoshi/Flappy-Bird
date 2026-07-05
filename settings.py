# Imports -->
import pygame
import os
import obstacle as o

dir = os.path.dirname(__file__)
height,width = 900,500
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
GAME_OVER_SCREEN = "game over"
current_screen = GAME_SCREEN
player_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
flappy = None
is_jumping = False
game_over = False
bg_colour = (100,224,117)
resume_button = pygame.Rect(width-350,height-600,200,60)
quit_button = pygame.Rect(width-350,height-500,200,60)
resume_img = os.path.join(dir,r"Images/resume.png")
quit_img = os.path.join(dir,r"Images/quit.png")
resume_btn_img = pygame.image.load(resume_img)
resume_btn_img = pygame.transform.scale(resume_btn_img,(200,60))
quit_btn_img = pygame.image.load(quit_img)
quit_btn_img = pygame.transform.scale(quit_btn_img,(200,60))
font = pygame.font.Font(os.path.join(dir,r"flappy-font.ttf"),50)
spawn_obstacle = pygame.USEREVENT + 1
gap_height = 350
top_pipe = None
bottom_pipe = None
score = 0
jump_sound = pygame.mixer.Sound(os.path.join(dir,r"sfx_wing.wav"))
point_sound = pygame.mixer.Sound(os.path.join(dir,r"sfx_point.wav"))
hit_sound = pygame.mixer.Sound(os.path.join(dir,r"sfx_hit.wav"))
die_sound = pygame.mixer.Sound(os.path.join(dir,r"sfx_die.wav"))