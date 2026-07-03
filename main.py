# Imports -->
import pygame
pygame.init()
import settings as s
import game_logic as gl
import screen_logic as sl
import flappy_player as fp
import obstacle as o
import random

s.screen = pygame.display.set_mode((s.width,s.height))
s.bg = pygame.image.load(s.background_img)
s.bg = pygame.transform.scale(s.bg,(s.width,s.height))
s.ground = pygame.image.load(s.ground_img)
s.flappy = fp.Flappy()
s.player_group.add(s.flappy)
pygame.time.set_timer(s.spawn_obstacle,1500)

while s.running:
    s.clock.tick(s.fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            s.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                s.playing = not s.playing
                if s.playing == False:
                    s.current_screen = s.PAUSE_SCREEN
            if event.key == pygame.K_SPACE:
                s.is_jumping = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("work")
            mouse_pos = pygame.mouse.get_pos()
            print(s.playing)
            sl.set_screen_logic(mouse_pos)
            print(s.playing)
        if event.type == s.spawn_obstacle and s.playing == True:
            bottom_height = random.randint(300,450)
            top_height = s.height-bottom_height-s.gap_height
            s.top_pipe = o.Obstacle(top_height,True)
            s.bottom_pipe = o.Obstacle(bottom_height,False)
            s.obstacle_group.add(s.top_pipe)
            s.obstacle_group.add(s.bottom_pipe)

    if s.playing == True:
        gl.move_on_play()

    if s.current_screen == s.GAME_SCREEN:
        sl.draw_game_screen()

    if s.current_screen == s.PAUSE_SCREEN:
        sl.draw_puase_screen()

    if s.current_screen == s.GAME_OVER_SCREEN:
        sl.draw_game_over_screen()

    if pygame.sprite.spritecollide(s.flappy,s.obstacle_group,False,pygame.sprite.collide_mask):
        s.playing = False
        s.current_screen = s.GAME_OVER_SCREEN

    if s.flappy.rect.y >= 700:
        s.playing = False
        s.current_screen = s.GAME_OVER_SCREEN

    if s.flappy.rect.y <= 50:
        s.is_jumping = False
        
    s.player_group.update()
    s.obstacle_group.update()
    pygame.display.update()