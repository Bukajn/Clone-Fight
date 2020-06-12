import pygame
from Postac import Postac

class Player(Postac):
    def __init__(self,main):
        super().__init__(main)
        self.cooldown=0.1
        self.celStrzalu = "enemy"
        self.punktkierunkowyStrzlu=pygame.mouse.get_pos()
    def wys(self):
        super().wys()
        self.CzySkoczyc()
        self.punktkierunkowyStrzlu=pygame.mouse.get_pos()
    def CzySkoczyc(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_SPACE]  and self.state==0:
            self.jumpSound.play()
            self.skocz=True
        if pygame.mouse.get_pressed()[0]:
            self.strzel=True
    def HPdoDodania(self,ilosc):
        if self.hp+ilosc<self.max_hp:
            self.hp+=ilosc
            self.main.GUI.pasekZdrowia.hpdododania +=ilosc
        else:
            self.hp = self.max_hp
            self.main.GUI.pasekZdrowia.hpdododania+=self.max_hp-self.hp