import pygame
WHITE = (255, 255, 255)
BLACK =(0,0,0)
RED =(255, 0, 0)

class Target(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

         super().__init__()

         self.image = pygame.Surface([width, height]) 
         self.image.fill(WHITE)
         self.image.set_colorkey(WHITE)

         pygame.draw.ellipse(self.image, RED, [200, 200, 50, 50])

         self.rect = self.image.get_rect()

