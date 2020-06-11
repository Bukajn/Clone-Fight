import pygame
from PasekMany import PasekMany
from paseknaladowania import Paseknaladowania
from PasekZdrowia import PasekZdrowia
class GUI(object):
    def __init__(self,main):
        self.main=main
        self.pos = pygame.Vector2(20,550)
        self.colour =(56,215,178)
        self.pole = pygame.Rect(self.pos.x,self.pos.y,760,50)
        self.pasekMany = PasekMany(self.main,self)
        self.paseknaladowania = Paseknaladowania(self.main,self)
        self.pasekZdrowia= PasekZdrowia(self.main,self)
        self.mana =0.0
        self.max_mana=100.0

    def wys(self):
        pygame.draw.rect(self.main.screen,self.colour,self.pole)
        self.pasekMany.wys()
        self.paseknaladowania.wys()
        self.pasekZdrowia.wys()

