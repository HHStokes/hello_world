import pygame
from pygame.locals import *
import random

pygame.init()

class Character(pygame.sprite.Sprite):
    def __init__(self,background,xBoundry,yBoundry):
        ##as a key for me pygame.draw.rect(Surface, color (rgb)(0-255), Rect(), width = 0)
        ## pygame.draw.ret(background, (0,255,0), (50,50,50,50))
        pygame.sprite.Sprite.__init__(self)
        self.blue = (75,75,255)
        self.red = (255,75,75)
        self.white = (255,255,255)
        self.green = (75,255,75)
        self.purple = (255,75,255)
        self.orange = (150,150,75)
        self.image = pygame.Surface([10,10])
        self.image.fill()

        self.currentX = 0
        self.currentY = 0
        self.background = background
        self.isDead = False
        self.xBound = xBoundry
        self.yBound = yBoundry

    def update():
        
    def placeMob(self):
        self.currentX = random.randint(0,self.xBound)
        self.currentY = random.randint(0,self.yBound)
    
    def mobDie(self):
        self.isDead = True
        self.draw_mobRed()
    
    def rollover(self):
        if self.currentX > self.xBound:
            self.currentX = 0;
        elif self.currentY > self.yBound:
            self.currentY = 0;

        
    def draw_mobBlue(self):

        self.placeMob()
                                            ##x,y,width, height
        pygame.draw.rect(self.background, self.blue, (self.currentX,self.currentY,10,10))
   
    
    def draw_mobGreen(self):
        self.placeMob()
                                            ##x,y,width, height
        pygame.draw.rect(self.background, self.green, (self.currentX,self.currentY,10,10))
      

    #Drawing the mob red is used to inidcate death, so we don't want to place one randomly
    def draw_mobRed(self):
                                            ##x,y,width, height
        pygame.draw.rect(self.background, self.red, (self.currentX,self.currentY,10,10))
    
    def draw_mobPurple(self):
        self.placeMob()
                                            ##x,y,width, height
        pygame.draw.rect(self.background, self.purple, (self.currentX,self.currentY,10,10))

    
    ##def draw_playerShip(self):
        #pygame.draw.polygon(self.background,self.white,)



    #def draw_pellet(self):
        #code









