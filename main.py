# Imports -->
import pygame
pygame.init()
import settings as s
import game_logic as gl
import screen_logic as sl
import flappy_player as fp

s.screen = pygame.display.set_mode((s.width,s.height))
s.bg = pygame.image.load(s.background_img)
s.bg = pygame.transform.scale(s.bg,(s.width,s.height))
s.ground = pygame.image.load(s.ground_img)
s.resume_btn_img = pygame.image.load(s.resume_img)
s.resume_btn_img = pygame.transform.scale(s.resume_btn_img,(200,60))
s.quit_btn_img = pygame.image.load(s.quit_img)
s.quit_btn_img = pygame.transform.scale(s.quit_btn_img,(200,60))
s.flappy = fp.Flappy()
s.player_group.add(s.flappy)

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

    if s.playing == True:
        gl.move_on_play()

    if s.current_screen == s.GAME_SCREEN:
        sl.draw_game_screen()

    if s.current_screen == s.PAUSE_SCREEN:
        sl.draw_puase_screen()
        print(s.playing)

    if s.flappy.rect.y >= 700:
        s.playing = False
        s.game_over = True

    if s.flappy.rect.y <= 50:
        s.is_jumping = False
        
    s.player_group.update()
    pygame.display.update()