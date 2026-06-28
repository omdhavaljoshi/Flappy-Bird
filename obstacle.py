import pygame
import random
import settings as s

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.height = random.randint(300,450)
        self.image = pygame.image.load(s.dir+r"/Images/pipe.png")
        self.image = pygame.transform.scale(self.image,(80,self.height))
        self.rect = self.image.get_rect(bottomleft = (750,750))

    def move_left(self):
        if s.playing == True:
            self.rect.x -= s.scroll_speed
            if self.rect.right < 0:
                self.kill()

    def update(self):
        self.move_left()