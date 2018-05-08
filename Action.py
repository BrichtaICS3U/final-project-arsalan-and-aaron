# ICS3U
# Assignment 2: Action
# <Aaron>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame, random
from snow import Snow
pygame.init()
background = pygame.image.load("Images/Window.png")
# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the screen size
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Aaron Action")
speed = 1
SNOW = pygame.sprite.Group()

for i in range(120):
    mySnow = Snow(WHITE, 10,10, random.randint(5,20))
    mySnow.rect.x = random.randint(0,400)
    mySnow.rect.y = random.randint(0,400)
    SNOW.add(mySnow)

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
screen.blit(background, (0, 0))
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    for snow in SNOW:
        snow.moveBackward(8)
        if snow.rect.y > SCREENHEIGHT:
            snow.changeSpeed(random.randint(5,20))
            snow.rect.y = -200
            snow.rect.x = random.randint(0,400)                 
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(BLACK)
    SNOW.draw(screen)
    # Queue different shapes and lines to be drawn
    # pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
