import pygame
WHITE = (255, 255, 255)
BLACK =(0,0,0)
RED =(255, 0, 0)
Background_colour = (239, 210, 203)

class Target(pygame.sprite.Sprite):

    def __init__(self, color, width, height, speed):

         super().__init__()

         self.image = pygame.Surface([width, height]) 
         self.image.fill(BLACK)
         self.image.set_colorkey(BLACK)

         self.width = width
         self.height = height
         self.color = color
         self.speed = speed


         pygame.draw.ellipse(self.image, RED, [0, 0, 50, 50])
         pygame.draw.ellipse(self.image, WHITE, [8, 8, 35, 35])
         pygame.draw.ellipse(self.image, RED, [15, 15, 20, 20])

         self.rect = self.image.get_rect()

    def moveDown(self, speed):
        self.rect.y += 3 * (speed*1)

    def moveRight(self, speed):
        self.rect.x += 5 * (speed *1)

    def changeSpeed(self, speed):
        self.speed = speed

    def call_back(self):
        """Runs a function when clicked"""
        self.call_back_()





class TargetMedium(pygame.sprite.Sprite):

    def __init__(self, color, width, height, speed):

         super().__init__()

         self.image = pygame.Surface([width, height]) 
         self.image.fill(BLACK)
         self.image.set_colorkey(BLACK)

         self.width = width
         self.height = height
         self.color = color
         self.speed = speed

         #self.call_back_ = action

         pygame.draw.ellipse(self.image, RED, [0, 0, 50, 50])
         pygame.draw.ellipse(self.image, WHITE, [8, 8, 35, 35])
         pygame.draw.ellipse(self.image, RED, [15, 15, 20, 20])

         self.rect = self.image.get_rect()

    def moveDown(self, speed):
        self.rect.y += self.speed * speed / 20

    def changeSpeed(self, speed):
        self.speed = speed

    def call_back(self):
        """Runs a function when clicked"""
        self.call_back_()

    def moveRight (self):
        speed = 2
        self.rect.x += self.speed
        if self.rect.x > SCREENWIDTH:
            self.rect.x = -100
#-------

class Background(pygame.sprite.Sprite):

    def __init__ (self, color, width, height):

         super().__init__()

         self.image = pygame.Surface([width, height]) 
         self.image.fill(WHITE)
         self.image.set_colorkey(WHITE)

         self.width = width
         self.height = height
         self.color = color

         pygame.draw.rect(self.image, Background_colour, [0, 0, 800, 800])

         self.rect = self.image.get_rect()

    def call_back(self):
        self.call_back_()
