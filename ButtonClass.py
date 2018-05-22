# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

Hit = False

import pygame, sys, random
from Classes import Target
from Classes import Background
from Classes import TargetSmall
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
YELLOW = (254, 215, 10)
Background_colour = (239, 210, 203)
DARK_BLUE = (7, 59, 76)
Title_Background = (225, 206, 122)
Background2 = (194, 248, 203)


SCREENWIDTH = 800
SCREENHEIGHT = 800
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

#background
background = pygame.image.load("Target.png")
pygame.display.set_caption("Aim Trainer")

#music
#pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
#pygame.mixer.music.load('Cricket.mp3')
#pygame.mixer.music.play(-1) #-1 means loops for ever, 0 means play just once)

#------GAME
TARGET = pygame.sprite.Group()
for i in range(3):
    myTarget = Target(RED, 100, 100, random.randint(5, 20))
    myTarget.rect.x = random.randint(50, 750)
    myTarget.rect.y = random.randint(50, 750)
    TARGET.add(myTarget)
    score = 0

BACKGROUND = pygame.sprite.Group()
for i in range(1):
    myBackground = Background(Background_colour, 800, 800)
    myBackground.rect.x = 0
    myBackground.rect.x = 0
    BACKGROUND.add(myBackground)
    lives = 3

# -----MENU
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
        self.txt = txt #text
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

def Play ():
    global level
    level = 3

def Back_Menu():
    global level
    level = 1

def Instructions():
    global level
    level = 4

def Easy():
    "easy"
    print("You clicked easy!")
    global level
    level = 5

def Medium():
    "medium"
    print("You clicked medium!")

def Hard():
    "hard"
    print("You clicked hard!")

def Custom():
    "Custom"
    print("You clicked Custom!")

def sound_ON():
    """this will turn the sound on"""
    print("sound ON")
    pygame.mixer.unpause()
    

def sound_OFF():
    """this will turn the sound off"""
    print("sound OFF")
    pygame.mixer.pause()

def music_ON():
        "This will turn the music ON"""
        print("Music ON")
        pygame.mixer.unpause()

def music_OFF():
    "This will turn the music off"
    print("Music OFF")
    pygame.mixer.unpause

def mousebuttondown(level):
    global Hit
    Hit = False
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
    elif level == 3:
        for button in level3_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 4:
        for button in level4_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 5:
        score = 0
        lives = 3
        for Target in TARGET:
            if Target.rect.collidepoint(pos):
                Hit = True
                score += 1
                print ("Your score is", (score), "!")
                
        for Background in BACKGROUND:
            if Background.rect.collidepoint(pos) and Hit == False:
                lives -= 1
                print ("You missed!")
                print ("You have", (lives), "lives")
                if lives == 0:
                    print ("No more lives! Game over.")
                    Back_Menu()
                    

level = 1
carryOn = True
clock = pygame.time.Clock()

#create button objects

#buttons in the Main Menu (level 1)
button_01 = Button("PLAY", (SCREENWIDTH/8, SCREENHEIGHT/2 + 50 ), Play, BUTTON1)
button_02 = Button("INSTRUCTIONS", (SCREENWIDTH/8, SCREENHEIGHT/2 + 110 ), Instructions, BUTTON1)
button_03 = Button("SETTINGS",(SCREENWIDTH/8, SCREENHEIGHT/2 + 170), my_next_function, BUTTON2)#transfers the screen to layer 2
button_04 = Button("QUIT", (SCREENWIDTH/8, SCREENHEIGHT/2 + 230), my_quit_function, BUTTON3)#terminates the program


#buttons in Settings (level 2)
button_05 = Button("MENU", (SCREENWIDTH/8, SCREENHEIGHT/2 + 230), Back_Menu, BUTTON3)#returns to layer 1
button_ON = Button("ON", (SCREENWIDTH/2, SCREENHEIGHT/2 - 200), sound_ON, BUTTON2, size=(45, 50))#turns sound on
button_OFF = Button("OFF",(SCREENWIDTH/2 + 100, SCREENHEIGHT/2 - 200), sound_OFF,BUTTON2, size=(45, 50))#turns sound off
button2_ON = Button("ON", (SCREENWIDTH/2, SCREENHEIGHT/2 - 100), music_ON, BUTTON2, size=(45, 50))#turns Music on
button2_OFF = Button("OFF",(SCREENWIDTH/2 + 100, SCREENHEIGHT/2 - 100), music_OFF,BUTTON2, size=(45, 50))#turns Music off

#buttons in Play (level 3)
button_easy = Button("EASY", (SCREENWIDTH/2 - 200, SCREENHEIGHT/2 - 200), Easy, BUTTON3)
button_medium = Button("MEDIUM", (SCREENWIDTH/2, SCREENHEIGHT/2 - 200), Medium, BUTTON3)
button_hard = Button("HARD", (SCREENWIDTH/2 + 200, SCREENHEIGHT/2 - 200), Hard, BUTTON3)
button_Custom = Button ("CUSTOM",(SCREENWIDTH/2, SCREENHEIGHT/2 -100),  Custom, BUTTON3)
button_menu = Button("MENU", (SCREENWIDTH/8, SCREENHEIGHT/2 + 230), Back_Menu, BUTTON3)

#buttons in Instructions (level 4)
button_menu2 =  Button("MENU", (SCREENWIDTH/8, SCREENHEIGHT/2 + 230), Back_Menu, BUTTON3)
button_play2 = Button("PLAY", (SCREENWIDTH/2 + 300, SCREENHEIGHT/2 + 230), Play, BUTTON3)

#Easy mode = level 5

#buttons in Custom Settings (level 6)

#arrange button groups depending on level
level1_buttons = [button_01, button_02, button_03, button_04]
level2_buttons  = [button_05, button_ON, button_OFF, button2_ON,button2_OFF]
level3_buttons = [button_easy, button_medium, button_hard, button_menu, button_Custom]
level4_buttons = [button_menu, button_play2]

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            mousebuttondown(level)
        
 
    # --- Game logic goes here


    # Clear the screen to white
    screen.blit(background, (0, 0))

    # Draw buttons
    #Menu
    if level == 1:
        for button in level1_buttons:
            button.draw()
        #Title
        fontTitle = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceTitle = fontTitle.render('...', True, DARK_BLUE) 
        textRectTitle = textSurfaceTitle.get_rect()
        textRectTitle.center = (400, 100)# I changed the height of the text because it was overlapping over the button

        screen.blit(textSurfaceTitle, textRectTitle)
    
    #Settings
    elif level == 2:
        screen.fill(Title_Background)
        for button in level2_buttons:
            button.draw()
        #SettingsTitle
        fontSettingsTitle = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceSettingsTitle = fontSettingsTitle.render('Settings', True, DARK_BLUE) 
        textRectSettingsTitle = textSurfaceSettingsTitle.get_rect()
        textRectSettingsTitle.center = (400, 100)

        fontSoundSubt = pygame.font.Font('freesansbold.ttf', 35)
        textSurfaceSoundSubt = fontSoundSubt.render('Sound:', True, DARK_BLUE) 
        textRectSoundSubt = textSurfaceSoundSubt.get_rect()
        textRectSoundSubt.center = (200, 200)

        fontMusicTitle = pygame.font.Font('freesansbold.ttf', 35)
        textSurfaceMusicTitle = fontMusicTitle.render('Music:', True, DARK_BLUE) 
        textRectMusicTitle = textSurfaceMusicTitle.get_rect()
        textRectMusicTitle.center = (195, 300)

        screen.blit(textSurfaceSoundSubt, textRectSoundSubt)
        screen.blit(textSurfaceSettingsTitle, textRectSettingsTitle)
        screen.blit(textSurfaceMusicTitle, textRectMusicTitle)

    #Play
    elif level == 3:
        screen.fill(Background_colour)
        for button in level3_buttons:
            button.draw()
        #Title
        fontPlayTitle = pygame.font.Font('freesansbold.ttf', 50)
        textSurfacePlayTitle = fontPlayTitle.render('Choose Difficulty', True, DARK_BLUE) 
        textRectPlayTitle = textSurfacePlayTitle.get_rect()
        textRectPlayTitle.center = (400, 100)

        screen.blit(textSurfacePlayTitle, textRectPlayTitle)

    #Instructions
    elif level == 4:
        screen.fill(Background2)
        for button in level4_buttons:
            button.draw()
        #Title/Text
        fontInstructionsTitle = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceInstructionsTitle = fontInstructionsTitle.render('Instructions', True, DARK_BLUE) 
        textRectInstructionsTitle = textSurfaceInstructionsTitle.get_rect()
        textRectInstructionsTitle.center = (400, 100)
  
        fontTextTitle = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceTextTitle = fontTextTitle.render('This is a target aiming game to improve your reaction time and aim', True, DARK_BLUE) 
        textRectTextTitle = textSurfaceTextTitle.get_rect()
        textRectTextTitle.center = (400, 200)
  
        fontText2Title = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceText2Title = fontText2Title.render('with a mouse. Click the appearing targets before they disappear.', True, DARK_BLUE) 
        textRectText2Title = textSurfaceText2Title.get_rect()
        textRectText2Title.center = (390, 230)
  
        fontText3Title = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceText3Title = fontText3Title.render('Each harder difficulty decreases button pop-up time, so a higher', True, DARK_BLUE) 
        textRectText3Title = textSurfaceText3Title.get_rect()
        textRectText3Title.center = (330, 280)
  
        fontText4Title = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceText4Title = fontText4Title.render('reaction and better aiming is needed for harder levels. You have', True, DARK_BLUE) 
        textRectText4Title = textSurfaceText4Title.get_rect()
        textRectText4Title.center = (395, 310)
  
        fontText5Title = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceText5Title = fontText5Title.render('three strikes, targets will keep appearing and disappearing until you', True, DARK_BLUE) 
        textRectText5Title = textSurfaceText5Title.get_rect()
        textRectText5Title.center = (395, 340)
  
        fontText6Title = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceText6Title = fontText6Title.render('miss three targets, once you miss three targets, the game is over.', True, DARK_BLUE) 
        textRectText6Title = textSurfaceText6Title.get_rect()
        textRectText6Title.center = (395, 370)
          
        screen.blit(textSurfaceTextTitle, textRectTextTitle)
        screen.blit(textSurfaceText2Title, textRectText2Title)
        screen.blit(textSurfaceText3Title, textRectText3Title)
        screen.blit(textSurfaceText4Title, textRectText4Title)
        screen.blit(textSurfaceText5Title, textRectText5Title)
        screen.blit(textSurfaceText6Title, textRectText6Title)
        screen.blit(textSurfaceInstructionsTitle, textRectInstructionsTitle)

    #Easy Mode
    elif level == 5:
        screen.fill(Background_colour)
        BACKGROUND.draw(screen)
        for target in TARGET:
            #target.moveDown(8)
            if target.rect.y > SCREENHEIGHT:
                target.changeSpeed(random.randint(5,20))
                target.rect.y = -200
                target.rect.x = random.randint(0,400)

        TARGET.draw(screen)
       

    

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

