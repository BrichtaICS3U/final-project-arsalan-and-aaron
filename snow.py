import pygame
WHITE = (255, 255, 255)
BLACK =(0,0,0)
RED =(255, 0, 0)
class Snow(pygame.sprite.Sprite):

    def __init__(self, color, width, height, speed):

         super().__init__()

         self.image = pygame.Surface([width, height]) 
         self.image.fill(RED)
         self.image.set_colorkey(RED)

         self.width=width 
         self.height=height
         self.color = color
         self.speed = speed

         
