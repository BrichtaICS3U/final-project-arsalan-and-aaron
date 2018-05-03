# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys
pygame.init()

# Define some colours
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_GREY = (197, 197, 197)
DARK_GREY = (44, 66, 63)
BUTTON1 = (148, 155, 150)
BUTTON2 = (130, 145, 145)
BUTTON3 = (76, 91, 97)

SCREENWIDTH = 800
SCREENHEIGHT = 800
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

#background
background = pygame.image.load("Target.png")

#music
#pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
#pygame.mixer.music.load('Cricket.mp3')
#pygame.mixer.music.play(-1) #-1 means loops for ever, 0 means play just once)


class Button():
    """This is a class for a generic button.
    
       txt = text on the button
       location = (x,y) coordinates of the button's centre
       action = name of function to run when button is pressed
       bg = background colour (default is white)
       fg = text colour (default is black)
       size = (width, height) of button
       font_name = name of font
       font_size = size of font
    """
    def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(150, 50), font_name="Segoe Print", font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size

        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action

    def draw(self):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        """Checks if mouse is over button using rect collision"""
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GRAY  # mouseover color

    def call_back(self):
        """Runs a function when clicked"""
        self.call_back_()

def my_shell_function():
    """A generic function that prints something in the shell"""
    print('Fire the nukes!')

def my_next_function():
    """A function that advances to the next level"""
    global level
    level += 1

def my_previous_function():
    """A function that retreats to the previous level"""
    global level
    level -= 1

def my_quit_function():
    """A function that will quit the game and close the pygame window"""
    pygame.quit()
    sys.exit()

def Hello():
    """this function will print out hello in the shell"""
    print("Hello")

def sound_ON():
    """this will turn the sound on"""
    print("sound ON")
    pygame.mixer.unpause()
    

def sound_OFF():
    """this will turn the sound off"""
    print("sound OFF")
    pygame.mixer.pause()
    
   

def mousebuttondown(level):
    """A function that checks which button was pressed"""
    pos = pygame.mouse.get_pos()
    if level == 1:
        for button in level1_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 2:
        for button in level2_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

level = 1
carryOn = True
clock = pygame.time.Clock()



#create button objects

#buttons on layer one
#feel free to change any of the settings to your fancy
button_01 = Button("PLAY", (SCREENWIDTH/2, SCREENHEIGHT/3 ), Hello,BUTTON1)
button_04 = Button("SETTINGS",(SCREENWIDTH/2, SCREENHEIGHT/3 + 100),my_next_function,BUTTON2)#transfers the screen to layer 2
button_03 = Button("QUIT", (SCREENWIDTH/2, SCREENHEIGHT/3 + 200), my_quit_function, BUTTON3)#terminates the program


#buttons on layer two
#feel free to change any of the settings to your fancy
#i didn't add colour to the on and off button cause i had no idea what you wanted so i left that for you#
button_02 = Button("BACK", (SCREENWIDTH/2, SCREENHEIGHT/3 + 200), my_previous_function,BUTTON3)#returns to layer 1
button_ON = Button("ON", (((SCREENWIDTH/6)*2) + 60, SCREENHEIGHT/3 + 100), sound_ON,BUTTON2, size=(45, 50))#turns sound on
button_OFF = Button("OFF",(((SCREENWIDTH/6)*3) + 70, SCREENHEIGHT/3 + 100), sound_OFF,BUTTON2, size=(45, 50))#turns sound off

#arrange button groups depending on level
level1_buttons = [button_01, button_03, button_04]
level2_buttons = [button_02,button_ON,button_OFF]


#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            mousebuttondown(level)
        

    # --- Draw code goes here

    # Clear the screen to white
    screen.blit(background, (0, 0))

    # Draw buttons
    if level == 1:
        for button in level1_buttons:
            button.draw()
        #Title
        fontTitle = pygame.font.Font('freesansbold.ttf', 32)
        textSurfaceTitle = fontTitle.render('summative', True, LIGHT_GREY) 
        textRectTitle = textSurfaceTitle.get_rect()
        textRectTitle.center = (400, 100)# I changed the height of the text because it was overlapping over the button

        screen.blit(textSurfaceTitle, textRectTitle)
    
    elif level == 2:
        for button in level2_buttons:
            button.draw()
        #SettingsTitle
        fontSettingsTitle = pygame.font.Font('freesansbold.ttf', 32)
        textSurfaceSettingsTitle = fontSettingsTitle.render('Settings', True, LIGHT_GREY) 
        textRectSettingsTitle = textSurfaceSettingsTitle.get_rect()
        textRectSettingsTitle.center = (400, 100)

        fontSoundSubt = pygame.font.Font('freesansbold.ttf', 28)
        textSurfaceSoundSubt = fontSoundSubt.render('Sound', True, LIGHT_GREY) 
        textRectSoundSubt = textSurfaceSoundSubt.get_rect()
        textRectSoundSubt.center = (400, 250)

        screen.blit(textSurfaceSoundSubt, textRectSoundSubt)
        screen.blit(textSurfaceSettingsTitle, textRectSettingsTitle)    

    

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

