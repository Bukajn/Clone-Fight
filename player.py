import pygame
from Postac import Postac
from Promien import Promien
import asset
class Player(Postac):
    def __init__(self,main):
        self.pos = pygame.Vector2(336, 0)
        super().__init__(main)

        self.klatkiWPrawo=[asset.imgRight1,asset.imgRight2,asset.imgRight3,asset.imgRight4,asset.imgRight5,asset.imgRight6]
        self.klatkiWPrawo=[pygame.transform.rotozoom(pygame.image.load(x),0,1.5) for x in self.klatkiWPrawo]

        self.klatkiWLewo=[asset.imgLeft1,asset.imgLeft2,asset.imgLeft3,asset.imgLeft4,asset.imgLeft5,asset.imgLeft6]
        self.klatkiWLewo = [pygame.transform.rotozoom(pygame.image.load(x), 0, 1.5) for x in self.klatkiWLewo]

        self.predkoscAnimacji=0.03

        self.cooldown=1
        self.celStrzalu = "enemy"
        self.punktkierunkowyStrzlu=pygame.mouse.get_pos()
        self.promien =None
        self.cooldownPromien =10
        self.zegarPromien = pygame.time.Clock()
        self.czasUplynietyPromien=0
        self.CzyMoznaSkoczyc = True
        self.czyMozeWykonacPromien=True
    def wys(self):
        if self.main.StartMenuOtworzone==False:
            super().wys()
            self.CzySkoczyc()
            self.punktkierunkowyStrzlu=pygame.mouse.get_pos()
            if self.pos.y>600:
                self.HPdoDodania(-self.hp)
            if pygame.mouse.get_pressed()[2] and self.main.CzyKreatorOtworzony==False and self.main.GUI.mana>0 and self.czasUplynietyPromien>self.cooldownPromien and self.czyMozeWykonacPromien:
                self.promien = Promien(self.main)
                self.main.GUI.pasekMany.DodawajMane(-self.main.GUI.mana)
                self.czasUplynietyPromien=0
                self.zegarPromien.tick()
            elif self.czasUplynietyPromien < self.cooldownPromien:
                self.czasUplynietyPromien += self.zegarPromien.tick()/1000
            if self.promien!= None:
                self.promien.wys()

    def CzySkoczyc(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_SPACE]  and self.state==0 and self.CzyMoznaSkoczyc:
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