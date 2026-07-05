import pygame
import settings as s

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,height,top):
        super().__init__()
        self.height = height
        self.top = top
        self.original_image = pygame.image.load(s.dir+r"/Images/pipe.png")
        self.image = pygame.transform.scale(self.original_image,(80,self.height))
        if self.top == True:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect = self.image.get_rect(topleft = (750,0))
        else:
            self.rect = self.image.get_rect(bottomleft = (750,750))

    def move_left(self):
        if s.playing == True:
            self.rect.x -= s.scroll_speed
            if self.rect.right < 0:
                self.kill()
                s.score += 1
                s.point_sound.play()

    def update(self):
        self.move_left()