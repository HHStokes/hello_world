import pygame
from pygame.locals import *
import character
from character import *

pygame.init()

def main():
    xBound = 640
    yBound = 480
    #screen from what I understand is the visible part of the game
    screen = pygame.display.set_mode((xBound,yBound)) #This determines the screen size
    screen.fill((5,5,5)) #This sets the screen to a dark shade
    pygame.display.set_caption("Blaster_Squares") #So our changes, albeit slight, are visible

    clock = pygame.time.Clock()

    ##variables for the gameloop

    loop = True
    FPS = 30
    playtime = 0.0
    
    new_mob = Character(screen,xBound,yBound)
    



    while loop:

        #new_mob.draw_mobGreen()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                #Using the excape key
                if event.key == pygame.K_ESCAPE:
                    loop = False
        
        #this refreshes the display
        pygame.display.flip()

    pygame.quit()




main()