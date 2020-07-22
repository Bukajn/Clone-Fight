import pygame, asset
from mana_coin import Mana_coin
class Apteczka(Mana_coin):
    def __init__(self,wlasciwosci,pos,mnoznik=1,iloscdodawanejMany=10):
        super().__init__(wlasciwosci,pos,mnoznik,iloscdodawanejMany)
        self.numerElementu=4
        self.iloscHP=self.iloscdodawanejMany

        self.miejscedocelowe=pygame.Vector2(263,579)
    def Dodaj(self):
        self.main.Player.HPdoDodania(self.iloscHP)
    def PoWczytaniu(self):
        self.orginalImg=asset.imgApteczka
        self.orginalzbieraniesound[0] = asset.zbieranieMana_coin
        self.img = pygame.image.load(self.orginalImg)
        self.img=pygame.transform.rotozoom(self.img,0,self.mnoznik)
        self.zbieraniesound =pygame.mixer.Sound(self.orginalzbieraniesound[0])
        self.zbieraniesound.set_volume(self.orginalzbieraniesound[1])
        self.clock = pygame.time.Clock()
        self.__init__([self.main,self.orginalImg,self.szerokosc,self.dlugosc],self.pos,self.mnoznik,self.iloscdodawanejMany)