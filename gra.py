import pygame
import sys
import random
from gracz1 import player1
from gracz2 import player2
from pygame import mixer ##muzyka 

class Game(object):

    def __init__(self):
        # konfigugacjad

        #INICJALIZUJEMY GRACZY
        self.gracz1 = player1(self) 
        self.gracz2 = player2(self)
        

        pygame.init()

        self.screen = pygame.display.set_mode((1200,600))
       
        #inicjalizacja tekstu
        pygame.font.init() 
        self.font = pygame.font.Font(pygame.font.get_default_font(), 20)

        self.clock =pygame.time.Clock()
        self.delta =0.0
        self.max_tps =20.0
        self.gracz_berek=1
        while True:
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    sys.exit(0)
                #elif event.type ==pygame.KEYDOWN and event.key == pygame.K_SPACE:W
                    #box.x= 0 
                    #box.y= 0
                 # zegar
            self.delta += self.clock.tick()/1000.0
            while self.delta >  1/self.max_tps: 
                self.tick()
                self.delta -= 1/ self.max_tps


            # rysowanie 
            self.screen.fill ((0,0,0))
            self.draw()
            
            #TODO
            #jezeli gracz dotknie bandy dostaje minusowy punkt 

            # sprawdzanie kolizji gracz 1 
            if abs(int(self.gracz2.pos.x)-int(self.gracz1.pos.x)) <50 and \
                self.gracz_berek==1 and \
                abs(int(self.gracz2.pos.y)-(self.gracz1.pos.y))<50 :
                self.gracz_berek=2 
                self.gracz2.pos.x=0 #ustawienie pozycji
                self.gracz2.punkty+=1
                pygame.mixer.init()
                pygame.mixer.music.load('C:\\git\\jas\\berekkomputerowy\\boom.mp3') 
                pygame.mixer.music.play()
            # dodawanie punktów
            
            # sprawdzanie klizji gracz 2
            elif abs(int(self.gracz2.pos.x)-int(self.gracz1.pos.x)) <50 and \
                self.gracz_berek==2 and \
                abs(int(self.gracz2.pos.y)-(self.gracz1.pos.y))<50 :
                self.gracz_berek=1
                self.gracz1.pos.x=1000 #ustawienie pozycji
                self.gracz1.punkty+=1
                pygame.mixer.init()
                pygame.mixer.music.load('C:\\git\\jas\\berekkomputerowy\\boom.mp3') 
                pygame.mixer.music.play()               
            # dodawanie punktów
            

            #Tekst
            textsurface = self.font.render(
                "punkty " + str(int(self.gracz2.punkty))+
                "gracz2 x " + str(int(self.gracz2.pos.x))+
                " y " + str(int(self.gracz2.pos.y)) +
                " berek "+str( self.gracz_berek)
                , False, (255, 255, 255))
            self.screen.blit(textsurface,(0,0))

            textsurface2 = self.font.render(
                "punkty " + str(int(self.gracz1.punkty))+
                "gracz1 x " + str(int(self.gracz1.pos.x))+
                " y " + str(int(self.gracz1.pos.y))
                , False, (255, 255, 255))
            self.screen.blit(textsurface2,(600,0))


            pygame.display.flip()

    def tick(self):
        self.gracz1.tick()
        self.gracz2.tick()

    def draw(self):
        self.gracz1.draw()
        self.gracz2.draw()

        
if __name__=="__main__":
    Game()
# https://www.ypygame.init()youtube.com/watch?v=tnq0whNwhZE&ab_channel=PiotrBaja
# https://www.youtube.com/watch?v=JxwyIFLM34E&ab_channel=PiotrBaja
