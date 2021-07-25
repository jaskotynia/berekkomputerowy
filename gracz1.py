import pygame
from pygame.math import Vector2

#jas
class player1(object):

    def __init__(self,game):
        self.game=game

        self.punkty=0;
        self.pos =  Vector2(1000,0)#pozycja startawa 
        self.vel =  Vector2(0,0)
        self.acc =  Vector2(0,0)       

    def add_force(self,force):
        self.acc += force 

                         
    def tick(self):
        # input  
        pressed =pygame.key.get_pressed()
        if pressed[pygame.K_UP] :
            self.add_force(Vector2(0,-1))
        if pressed[pygame.K_DOWN] :
            self.add_force(Vector2(0,1))    
        if pressed[pygame.K_LEFT] :
            self.add_force(Vector2(-1,0))
        if pressed[pygame.K_RIGHT] :
            self.add_force(Vector2(1,0))

        self.vel  *= 0.8  
        #self.vel -= Vector2(0,-1) #GRAWITACJA

        self.vel  += self.acc #PREDKOSCI
        self.pos  += self.vel
        self.acc  *= 0.9  #PRYSPIESZENIE


    def draw(self):
        rect = pygame.Rect(self.pos.x,self.pos.y,50,50) #wIELKOSC
        pygame.draw.rect(self.game.screen,(0,255,0),rect)