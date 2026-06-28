import pygame
import settings as s

#ground scroll -->
def ground_scrolling():
    s.ground_x -= s.scroll_speed
    if s.ground_x <= -102:
        s.ground_x = 0

def move_on_play():
    ground_scrolling()