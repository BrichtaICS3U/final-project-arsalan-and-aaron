# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, random, sys
from Classes import Target
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
Background3 = (127, 183, 190)

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
global score
global lives
score = 0 #variable for game score
lives = 3 #variable for lives
mscore = 0
mlives = 3
hscore = 0
hlives = 3

TARGET = pygame.sprite.Group()
for i in range(3):
    myTarget = Target(RED, 150, 150, random.randint(5, 20))
    myTarget.rect.x = random.randint(50, 750)
    myTarget.rect.y = random.randint(50, 750)
    TARGET.add(myTarget)
    
MTARGET = pygame.sprite.Group()
for i in range (3):
    myMtarget = Target(RED, 100, 100, random.randint(5, 20))
    myMtarget.rect.x = random.randint(50, 750)
    myMtarget.rect.y = random.randint(50, 750)
    MTARGET.add(myMtarget)

HTARGET = pygame.sprite.Group()
for i in range (3):
    myHtarget = Target(RED, 75, 75, random.randint(5, 20))
    myHtarget.rect.x = random.randint(50, 750)
    myHtarget.rect.y = random.randint(50, 750)
    HTARGET.add(myHtarget)

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

def Back():
    global level
    level += 7

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
    global level
    level = 6

def Hard():
    "hard"
    print("You clicked hard!")
    global level
    level = 7

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

    elif level == 8:
        for button in level8_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
                
def mouseTargetdown(score, lives, mscore, mlives, hscore, hlives, level):
    pos = pygame.mouse.get_pos()
    Hit = False
    for Target in TARGET:
        if Target.rect.collidepoint(pos):
            Hit = True
            score += 1
            print ("Your score is:", (score), "!")
            
            pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
            pygame.mixer.music.load('Ding.mp3')
            pygame.mixer.music.play(0) #  0 means play just once, -1 means loop forever)
            
            Target.rect.x = random.randint(50, 750)
            Target.rect.y = random.randint(-750, -50)
    for Mtarget in MTARGET:
        if Mtarget.rect.collidepoint(pos):
            Hit = True
            mscore += 1
            print ("Your score is:", (mscore), "!")

            pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
            pygame.mixer.music.load('Ding.mp3')
            pygame.mixer.music.play(0) #  0 means play just once, -1 means loop forever)

            Mtarget.rect.x = random.randint(50, 750)
            Mtarget.rect.y = random.randint(-750, -50)

    for Htarget in HTARGET:
        if Htarget.rect.collidepoint(pos):
            Hit = True
            hscore += 1
            print ("Your score is:", (hscore), "!")
            
            pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
            pygame.mixer.music.load('Ding.mp3')
            pygame.mixer.music.play(0) #  0 means play just once, -1 means loop forever)

            Htarget.rect.x = random.randint(50, 750)
            Htarget.rect.y = random.randint(-750, -50)

    if Hit == False:
        lives -= 1
        mlives -= 1
        hlives -= 1
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load('Buzz.mp3')
        pygame.mixer.music.play(0)
        if level == 5 and lives == 0:
            print ("No more lives! Game over.")
            #Back_Menu()
            level = 8
            #score = 0
            lives = 3
            mscore = 0
            mlives = 3
            hscore = 0
            hlives = 3

            pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
            pygame.mixer.music.load('Buzz.mp3')
            pygame.mixer.music.play(0)

        if level == 6 and mlives == 0:
            print ("No more lives! Game over.")
            #Back_Menu()
            level = 8
            score = 0
            lives = 3
            mscore = 0
            mlives = 3
            hscore = 0
            hlives = 3

            pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
            pygame.mixer.music.load('Buzz.mp3')
            pygame.mixer.music.play(0)

        if level == 7 and hlives == 0:
            print ("No more lives! Game over.")
            #Back_Menu()
            level = 8
            score = 0
            lives = 3
            mscore = 0
            mlives = 3
            hscore = 0
            hlives = 3

            pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
            pygame.mixer.music.load('Buzz.mp3')
            pygame.mixer.music.play(0)
            

    #if Hit == True:
        #myTarget.rect.0.x = random.randint(50, 750)
        #myTarget.rect.y = random.randint(50, 750)
    return score, lives, mscore, mlives, hscore, hlives, level
                    

level = 1
carryOn = True
clock = pygame.time.Clock()

#create button objects

#buttons in the Main Menu (level 1)
button_01 = Button("PLAY", (SCREENWIDTH/8, SCREENHEIGHT/2 + 50 ), Play, BUTTON1)
button_02 = Button("INSTRUCTIONS", (SCREENWIDTH/8, SCREENHEIGHT/2 + 110 ), Instructions, BUTTON1)
button_03 = Button("SETTINGS",(SCREENWIDTH/8, SCREENHEIGHT/2 + 170), my_next_function, BUTTON2)#transfers the screen to layer 2
button_04 = Button("QUIT", (SCREENWIDTH/8, SCREENHEIGHT/2 + 230), my_quit_function, BUTTON3)#terminates the program
button_05 = Button("QUIT", (SCREENWIDTH/8, SCREENHEIGHT/2 + 230), Back, BUTTON3)

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
button_menu = Button("MENU", (SCREENWIDTH/8, SCREENHEIGHT/2 + 230), Back_Menu, BUTTON3)

#buttons in Instructions (level 4)
button_menu2 =  Button("MENU", (SCREENWIDTH/8, SCREENHEIGHT/2 + 230), Back_Menu, BUTTON3)
button_play2 = Button("PLAY", (SCREENWIDTH/2 + 300, SCREENHEIGHT/2 + 230), Play, BUTTON3)

#Easy mode = level 5


#buttons in Gameover screen (Level 8)
button_menu = Button("MENU", (SCREENWIDTH/8, SCREENHEIGHT/2 + 230), Back_Menu, BUTTON3)
button_playagain = Button("PLAY AGAIN", (SCREENWIDTH/2 + 300, SCREENHEIGHT/2 + 230), Play, BUTTON3)

#arrange button groups depending on level
level1_buttons = [button_01, button_02, button_03, button_04]
level2_buttons  = [button_05, button_ON, button_OFF, button2_ON,button2_OFF]
level3_buttons = [button_easy, button_medium, button_hard, button_menu]
level4_buttons = [button_menu, button_play2]
level8_buttons = [button_menu, button_playagain]
#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            if level < 5 or level == 8:
                mousebuttondown(level)
            else:
                score, lives, mscore, mlives, hscore, hlives,level = mouseTargetdown(score, lives, mscore, mlives, hscore, hlives,level)
        

 
    # --- Game logic goes here
    
    for target in TARGET:
        target.moveDown(1)

    for target in MTARGET:
        target.moveDown(2)

    for target in HTARGET:
        target.moveDown(3)

    if lives == 0:
        level == 8

    elif mlives == 0:
        level == 8

    elif hlives == 0:
        level == 8

    
        

    

    # Draw background
    screen.blit(background, (0, 0))
    
    # Draw buttons
    #Menu
    if level == 1:

        for button in level1_buttons:
            button.draw()
        #Title
        fontTitle = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceTitle = fontTitle.render('Aim Trainer', True, DARK_BLUE) 
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
        textSurfaceText2Title = fontText2Title.render('with a mouse. Click the targets and get a high score before time', True, DARK_BLUE) 
        textRectText2Title = textSurfaceText2Title.get_rect()
        textRectText2Title.center = (385, 230)

        fontText3Title = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceText3Title = fontText3Title.render('runs out.', True, DARK_BLUE) 
        textRectText3Title = textSurfaceText3Title.get_rect()
        textRectText3Title.center = (118, 260)
  
        fontText4Title = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceText4Title = fontText4Title.render('Each harder difficulty decreases the amount of lives and targets,', True, DARK_BLUE) 
        textRectText4Title = textSurfaceText4Title.get_rect()
        textRectText4Title.center = (390, 310)
  
        fontText5Title = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceText5Title = fontText5Title.render('so a higher reaction and better aiming is needed for harder levels.', True, DARK_BLUE) 
        textRectText5Title = textSurfaceText5Title.get_rect()
        textRectText5Title.center = (395, 340)
  
        fontText6Title = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceText6Title = fontText6Title.render('Targets will keep appearing and disappearing when clicked. Your', True, DARK_BLUE) 
        textRectText6Title = textSurfaceText6Title.get_rect()
        textRectText6Title.center = (390, 370)
  
        fontText7Title = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceText7Title = fontText7Title.render('amount of lives is how many times you can miss, once you have no', True, DARK_BLUE) 
        textRectText7Title = textSurfaceText7Title.get_rect()
        textRectText7Title.center = (400, 400)

        fontText8Title = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceText8Title = fontText8Title.render('lives, the game is over.', True, DARK_BLUE) 
        textRectText8Title = textSurfaceText8Title.get_rect()
        textRectText8Title.center = (185, 430)
          
        screen.blit(textSurfaceTextTitle, textRectTextTitle)
        screen.blit(textSurfaceText2Title, textRectText2Title)
        screen.blit(textSurfaceText3Title, textRectText3Title)
        screen.blit(textSurfaceText4Title, textRectText4Title)
        screen.blit(textSurfaceText5Title, textRectText5Title)
        screen.blit(textSurfaceText6Title, textRectText6Title)
        screen.blit(textSurfaceText7Title, textRectText7Title)
        screen.blit(textSurfaceText8Title, textRectText8Title)
        screen.blit(textSurfaceInstructionsTitle, textRectInstructionsTitle)

    #Easy Mode
    elif level == 5:
        screen.fill(Background3)     
        for target in TARGET:
            if target.rect.y > SCREENHEIGHT:
                target.changeSpeed(random.randint(5, 20))
                target.rect.y = -200
                target.rect.x = random.randint(0, 400)

        TARGET.draw(screen)
        fontText6Title = pygame.font.Font('freesansbold.ttf', 26)
        textSurfaceText6Title = fontText6Title.render(str(score), True, WHITE) 
        textRectText6Title = textSurfaceText6Title.get_rect()
        textRectText6Title.center = (750, 35)
        screen.blit(textSurfaceText6Title, textRectText6Title)

        fontScoreTitle = pygame.font.Font('freesansbold.ttf', 26)
        textSurfaceScoreTitle = fontScoreTitle.render('SCORE:', True, WHITE) 
        textRectScoreTitle = textSurfaceScoreTitle.get_rect()
        textRectScoreTitle.center = (675, 35)
        screen.blit(textSurfaceScoreTitle, textRectScoreTitle)

        TARGET.draw(screen)
        fontText7Title = pygame.font.Font('freesansbold.ttf', 26)
        textSurfaceText7Title = fontText7Title.render(str(lives), True, WHITE) 
        textRectText7Title = textSurfaceText7Title.get_rect()
        textRectText7Title.center = (755, 770)
        screen.blit(textSurfaceText7Title, textRectText7Title)

        fontScore2Title = pygame.font.Font('freesansbold.ttf', 26)
        textSurfaceScore2Title = fontScore2Title.render('LIVES:', True, WHITE) 
        textRectScore2Title = textSurfaceScore2Title.get_rect()
        textRectScore2Title.center = (695, 770)
        screen.blit(textSurfaceScore2Title, textRectScore2Title)

    #Medium Mode
    elif level == 6:
        screen.fill(Background3)
        for mtarget in MTARGET:
            if mtarget.rect.y > SCREENHEIGHT:
                mtarget.changeSpeed(random.randint(5, 20))
                mtarget.rect.y = -200
                mtarget.rect.x = random.randint(0, 400)


        MTARGET.draw(screen)
        fontText6Title = pygame.font.Font('freesansbold.ttf', 26)
        textSurfaceText6Title = fontText6Title.render(str(mscore), True, WHITE) 
        textRectText6Title = textSurfaceText6Title.get_rect()
        textRectText6Title.center = (750, 35)
        screen.blit(textSurfaceText6Title, textRectText6Title)

        fontScoreTitle = pygame.font.Font('freesansbold.ttf', 26)
        textSurfaceScoreTitle = fontScoreTitle.render('SCORE:', True, WHITE) 
        textRectScoreTitle = textSurfaceScoreTitle.get_rect()
        textRectScoreTitle.center = (675, 35)
        screen.blit(textSurfaceScoreTitle, textRectScoreTitle)

        fontText7Title = pygame.font.Font('freesansbold.ttf', 26)
        textSurfaceText7Title = fontText7Title.render(str(mlives), True, WHITE) 
        textRectText7Title = textSurfaceText7Title.get_rect()
        textRectText7Title.center = (755, 770)
        screen.blit(textSurfaceText7Title, textRectText7Title)

        fontScore2Title = pygame.font.Font('freesansbold.ttf', 26)
        textSurfaceScore2Title = fontScore2Title.render('LIVES:', True, WHITE) 
        textRectScore2Title = textSurfaceScore2Title.get_rect()
        textRectScore2Title.center = (695, 770)
        screen.blit(textSurfaceScore2Title, textRectScore2Title)

    #Hard Mode
    elif level == 7: 
        screen.fill(Background3)
        for htarget in HTARGET:
            if htarget.rect.y > SCREENHEIGHT:
                htarget.changeSpeed(random.randint(5, 20))
                htarget.rect.y = -200
                htarget.rect.x = random.randint(0, 400)
                
        HTARGET.draw(screen)
        fontText6Title = pygame.font.Font('freesansbold.ttf', 26)
        textSurfaceText6Title = fontText6Title.render(str(hscore), True, WHITE) 
        textRectText6Title = textSurfaceText6Title.get_rect()
        textRectText6Title.center = (750, 35)
        screen.blit(textSurfaceText6Title, textRectText6Title)

        fontScoreTitle = pygame.font.Font('freesansbold.ttf', 26)
        textSurfaceScoreTitle = fontScoreTitle.render('SCORE:', True, WHITE) 
        textRectScoreTitle = textSurfaceScoreTitle.get_rect()
        textRectScoreTitle.center = (675, 35)
        screen.blit(textSurfaceScoreTitle, textRectScoreTitle)

        fontText7Title = pygame.font.Font('freesansbold.ttf', 26)
        textSurfaceText7Title = fontText7Title.render(str(hlives), True, WHITE) 
        textRectText7Title = textSurfaceText7Title.get_rect()
        textRectText7Title.center = (755, 770)
        screen.blit(textSurfaceText7Title, textRectText7Title)

        fontScore2Title = pygame.font.Font('freesansbold.ttf', 26)
        textSurfaceScore2Title = fontScore2Title.render('LIVES:', True, WHITE) 
        textRectScore2Title = textSurfaceScore2Title.get_rect()
        textRectScore2Title.center = (695, 770)
        screen.blit(textSurfaceScore2Title, textRectScore2Title)

    #Game Over Screen
    elif level == 8:
        screen.fill(Background3)
        for button in level8_buttons:
            button.draw()
        
        font = pygame.font.Font('freesansbold.ttf', 26)
        text1= font.render("GAME OVER! YOUR SCORE IS" ,1,DARK_BLUE)
        screen.blit(text1,(200,100))

        fontText9Title = pygame.font.Font('freesansbold.ttf', 26)
        textSurfaceText9Title = fontText9Title.render(str(score), True, DARK_BLUE) 
        textRectText9Title = textSurfaceText9Title.get_rect()
        textRectText9Title.center = (610, 113)
        screen.blit(textSurfaceText9Title, textRectText9Title)
        
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
