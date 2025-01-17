import os, pygame, sys
from pygame.locals import *


# Initialize screen
pygame.init()
disp = pygame.display.set_mode((800, 600),RESIZABLE)
color = (139,71,93)
#background_img = pygame.image.load('game.webp')

# Changing surface color
disp.fill(color)
pygame.display.set_caption('THE WORD GAME!') 
size = disp.get_size()
width = size[0]
height = size[1]



title = pygame.Rect(((width/16)+1, (height/8)+1, 7*width/8, height/4))
menu1 = pygame.Rect(((width/4)+1, (height/2)+1, 2*width/4, height/10))
menu2 = pygame.Rect(((width/4)+1, (height/2)+1+(3*height/20), 2*width/4, height/10))
menu3 = pygame.Rect(((width/4)+1, (height/2)+1+(6*height/20), 2*width/4, height/10))

#Draws dark grey rectangles.
pygame.draw.rect(disp, (81,81,81), menu1)
pygame.draw.rect(disp, (81,81,81), menu2)
pygame.draw.rect(disp, (81,81,81), menu3)

#Draws light grey ovals 
#ovals on top of rectangles
pygame.draw.ellipse(disp, (81,81,81), title)
pygame.draw.ellipse(disp, (142,142,142), menu1)
pygame.draw.ellipse(disp, (142,142,142), menu2)
pygame.draw.ellipse(disp, (142,142,142), menu3)

#choose font style for the menu 
font_title = pygame.font.SysFont('Algerian', 64)
font_menu = pygame.font.SysFont('Bodoni MT Black', 32)

#Creates and draws the text.
surface_title = font_title.render('THE WORD GAME!', True, (224,238,238))
rect_title = surface_title.get_rect() #get_rect() is my favorite Pygame function.
rect_title.center = (width/2,(height/4)+3)
surface_new_game = font_menu.render('START', True, (0,0,0))
rect_new_game = surface_new_game.get_rect()

rect_new_game.center = (width/2,(height/2)+(height/20)+3)
surface_load_game = font_menu.render('RULES', True, (0,0,0))
rect_load_game = surface_load_game.get_rect()
rect_load_game.center = (width/2,(height/2)+(4*height/20)+3)
surface_exit = font_menu.render('QUIT', True, (0,0,0))
rect_exit = surface_exit.get_rect()
rect_exit.center = (width/2,(height/2)+(7*height/20)+3)

while True: 
    #DISPLAYSURF.blit(background_img, (0,0))
    disp.blit(surface_title, rect_title)
    disp.blit(surface_new_game, rect_new_game)
    disp.blit(surface_load_game, rect_load_game)
    disp.blit(surface_exit, rect_exit)
    window = 1
    #disp.blit(background_img, (0,0))
    for event in pygame.event.get():
        if window == 1:
            if event.type == VIDEORESIZE:
                #This line creates a new display in order to clear the screen.
                #I figured this out myself, so if you know of a better way to do this, let me know.
                disp = pygame.display.set_mode((event.w, event.h),RESIZABLE)

                width = event.w
                height = event.h

                #Creates the rectangle objects that will be behind the title and menu buttons.
                title = pygame.Rect(((width/16)+1, (height/8)+1, 7*width/8, height/4))
                menu1 = pygame.Rect(((width/4)+1, (height/2)+1, 2*width/4, height/10))
                menu2 = pygame.Rect(((width/4)+1, (height/2)+1+(3*height/20), 2*width/4, height/10))
                menu3 = pygame.Rect(((width/4)+1, (height/2)+1+(6*height/20), 2*width/4, height/10))

                #Draws dark blue rectangles.
                pygame.draw.rect(disp, (139,139,0), menu1)
                pygame.draw.rect(disp, (139,139,0), menu2)
                pygame.draw.rect(disp, (139,139,0), menu3)

                #Draws blue ovals on top of the rectangles.
                pygame.draw.ellipse(disp, (139,139,0), title)
                pygame.draw.ellipse(disp, (0,0,255), menu1)
                pygame.draw.ellipse(disp, (0,0,255), menu2)
                pygame.draw.ellipse(disp, (0,0,255), menu3)

                #Creates and draws the text.
                rect_title = surface_title.get_rect()
                rect_title.center = (width/2,(height/4)+3)
                rect_new_game = surface_new_game.get_rect()
                rect_new_game.center = (width/2,(height/2)+(height/20)+3)
                rect_load_game = surface_load_game.get_rect()
                rect_load_game.center = (width/2,(height/2)+(4*height/20)+3)
                rect_exit = surface_exit.get_rect()
                rect_exit.center = (width/2,(height/2)+(7*height/20)+3)
        
                pygame.display.update() #Necessary to update the screen

            #When you let go of the left mouse button in the area of a button, the button does something.
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    if (menu1.left < event.pos[0] < menu1.right) and (menu1.top < event.pos[1] < menu1.bottom):
                        print("START") #Placeholder
                        window = 3
                    if (menu2.left < event.pos[0] < menu2.right) and (menu2.top < event.pos[1] < menu2.bottom):
                        print("RULES") #Placeholder
                        window = 2
                    if (menu3.left < event.pos[0] < menu3.right) and (menu3.top < event.pos[1] < menu3.bottom):
                        pygame.event.post(pygame.event.Event(QUIT)) #Exits the game

            #When you mouse-over a button, the text turns green.
            if event.type == MOUSEMOTION:
                if (menu1.left < event.pos[0] < menu1.right) and (menu1.top < event.pos[1] < menu1.bottom):
                    surface_new_game = font_menu.render('START', True, (255,255,0))
                else:
                    surface_new_game = font_menu.render('START', True, (0,0,0))
                if (menu2.left < event.pos[0] < menu2.right) and (menu2.top < event.pos[1] < menu2.bottom):
                    surface_load_game = font_menu.render('RULES', True, (255,255,0))
                else:
                    surface_load_game = font_menu.render('RULES', True, (0,0,0))
                if (menu3.left < event.pos[0] < menu3.right) and (menu3.top < event.pos[1] < menu3.bottom):
                    surface_exit = font_menu.render('QUIT', True, (255,255,0))
                else:
                    surface_exit = font_menu.render('QUIT', True, (0,0,0))           
        if window == 2:
            exec(open('rules.py').read())
        if window == 3:
            exec(open('game_screen.py').read())
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()