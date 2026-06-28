import pygame
import settings as s

class Flappy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bird_images = []
        self.load_images()
        self.image = self.bird_images[0]
        self.rect = self.image.get_rect(center = (s.width-700,s.height-600))
        self.index = 0.0
        self.animation_speed = 0.1
        self.gravity = 4
        self.jump_height = 80
        
    def load_images(self):
        for i in range(1,4):
            loaded_image = pygame.image.load(s.dir+r"/Images/bird"+f"{i}.png")
            loaded_image = pygame.transform.scale(loaded_image,(50,50))
            self.bird_images.append(loaded_image)
    
    def animate_flappy(self):
        self.index += self.animation_speed
        if self.index >= len(self.bird_images):
            self.index = 0.0
        self.image = self.bird_images[int(self.index)]

    def falling_flappy(self):
        self.rect.y += self.gravity

    def jump(self):
        self.rect.y -= self.jump_height
        
    def update(self):
        if s.playing == True:
            self.animate_flappy()
            self.falling_flappy()
            if s.is_jumping == True:
                s.is_jumping = False
                self.jump()