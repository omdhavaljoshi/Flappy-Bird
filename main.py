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
pygame.display.set_caption("Flappy bird")
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
                if s.current_screen != s.GAME_SCREEN:
                    s.playing = False
            if event.key == pygame.K_SPACE:
                s.is_jumping = True
            if s.active_input == "usernamebox":
                if event.key == pygame.K_BACKSPACE:
                    s.username_text = s.username_text[:len(s.username_text)-1]
                else:
                    s.username_text += event.unicode
            if s.active_input == "passwordbox":
                if event.key == pygame.K_BACKSPACE:
                    s.password_text = s.password_text[:len(s.password_text)-1]
                else:
                    s.password_text += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            sl.set_screen_logic(mouse_pos)
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
        sl.draw_pause_screen()

    if s.current_screen == s.GAME_OVER_SCREEN:
        sl.draw_game_over_screen()

    if s.current_screen == s.SIGN_UP_SCREEN:
        sl.draw_signup_screen()

    if s.current_screen == s.AUTH_SCREEN:
        sl.draw_auth_screen()

    if s.current_screen == s.SIGN_IN_SCREEN:
        sl.draw_signin_screen()
    
    if s.current_screen == s.MENU_SCREEN:
        sl.draw_menu_screen()

    if pygame.sprite.spritecollide(s.flappy,s.obstacle_group,False,pygame.sprite.collide_mask) and s.playing == True:
        s.playing = False
        s.hit_sound.play()
        s.die_sound.play()
        s.current_screen = s.GAME_OVER_SCREEN

    if s.flappy.rect.y >= 700 and s.playing == True:
        s.playing = False
        s.hit_sound.play()
        s.die_sound.play()
        s.current_screen = s.GAME_OVER_SCREEN

    if s.flappy.rect.y <= 50:
        s.is_jumping = False
        
    s.player_group.update()
    s.obstacle_group.update()
    pygame.display.update()