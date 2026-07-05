import pygame
import settings as s

class Flappy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bird_images = []
        self.load_images()
        self.image = self.bird_images[0]
        self.rect = self.image.get_rect(center = (s.width-400,s.height-600))
        self.index = 0
        self.gravity = 0.5
        self.jump_height = -60
        self.velocity = 0
        self.count = 0
        self.angle = 20
        
    def load_images(self):
        for i in range(1,4):
            loaded_image = pygame.image.load(s.dir+r"/Images/bird"+f"{i}.png")
            loaded_image = pygame.transform.scale(loaded_image,(50,50))
            self.bird_images.append(loaded_image)
    
    def animate_flappy(self):
        self.count += 1
        if self.count >= 15:
            self.index = (self.index+1)%3
            self.count = 0
        original_image = self.bird_images[self.index]
        centerX,centerY = self.rect.center
        self.image = pygame.transform.rotate(original_image,self.angle)
        self.rect = self.image.get_rect(center = (centerX,centerY))

    def falling_flappy(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity
        # self.angle -= 1
        if self.velocity >=0:
            self.angle -= 2
        if self.velocity<0:
            self.angle = 30
        if self.angle <= -90:
            self.angle = -90
        
    def jump(self):
        self.rect.y += self.jump_height
        self.velocity = -10
        
    def update(self):
        if s.playing == True:
            self.animate_flappy()
            self.falling_flappy()
            if s.is_jumping == True:
                self.jump()
                s.is_jumping = False