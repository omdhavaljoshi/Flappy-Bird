# Imports -->
import pygame
import os
import obstacle as o
import database as db

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
current_user = None
GAME_SCREEN = "game screen"
PAUSE_SCREEN = "pause screen"
GAME_OVER_SCREEN = "game over"
SIGN_IN_SCREEN = "sign in"
SIGN_UP_SCREEN = "sign up"
AUTH_SCREEN = "auth"
MENU_SCREEN = "menu"
current_screen = AUTH_SCREEN
player_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
flappy = None
is_jumping = False
game_over = False
bg_colour = (100,224,117)

# buttons ->
resume_button = pygame.Rect(width-350,height-600,200,60)
quit_button = pygame.Rect(width-350,height-500,200,60)
restart_button = pygame.Rect(width-350,height-600,200,60)
sign_up_button = pygame.Rect(width-350,height-400,200,60)
sign_in_button = pygame.Rect(width-350,height-600,200,60)
sign_up_button2 = pygame.Rect(width-350,height-500,200,60)
sign_in_button2 = pygame.Rect(width-350,height-400,200,60)
sign_out_button = pygame.Rect(width-350,height-200,200,60)
# images ->
resume_img = os.path.join(dir,r"Images/resume.png")
quit_img = os.path.join(dir,r"Images/quit.png")
restart_img = os.path.join(dir,r"Images/restart.png")
sign_up_img = os.path.join(dir,r"Images/sign up.png")
sign_in_img = os.path.join(dir,r"Images/Sign in.png")
sign_out_img = os.path.join(dir,r"Images/Sign out.png")
# button images ->
resume_btn_img = pygame.image.load(resume_img)
resume_btn_img = pygame.transform.scale(resume_btn_img,(200,60))
quit_btn_img = pygame.image.load(quit_img)
quit_btn_img = pygame.transform.scale(quit_btn_img,(200,60))
restart_btn_img = pygame.image.load(restart_img)
restart_btn_img = pygame.transform.scale(restart_btn_img,(200,60))
sign_up_btn_img = pygame.image.load(sign_up_img)
sign_up_btn_img = pygame.transform.scale(sign_up_btn_img,(200,60))
sign_in_btn_img = pygame.image.load(sign_in_img)
sign_in_btn_img = pygame.transform.scale(sign_in_btn_img,(200,60))
sign_out_btn_img = pygame.image.load(sign_out_img)
sign_out_btn_img = pygame.transform.scale(sign_out_btn_img,(200,60))
# input boxes ->
username_box = pygame.Rect(width-320,height-600,250,60)
password_box = pygame.Rect(width-320,height-500,250,60)
# input texts ->
username_text = ""
password_text = ""

font = pygame.font.Font(os.path.join(dir,r"flappy-font.ttf"),50)
font_2 = pygame.font.Font(None,35)
spawn_obstacle = pygame.USEREVENT + 1
gap_height = 350
top_pipe = None
bottom_pipe = None
score = 0
high_score = 0
jump_sound = pygame.mixer.Sound(os.path.join(dir,r"sfx_wing.wav"))
point_sound = pygame.mixer.Sound(os.path.join(dir,r"sfx_point.wav"))
hit_sound = pygame.mixer.Sound(os.path.join(dir,r"sfx_hit.wav"))
die_sound = pygame.mixer.Sound(os.path.join(dir,r"sfx_die.wav"))
score_board = pygame.Rect(width-450,height-400,400,180)
new_high_score = False
active_input = None
rendered_text = font_2.render("",True,"black")
account_created = None
sign_in_successful = None