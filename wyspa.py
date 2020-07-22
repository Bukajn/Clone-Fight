import pygame
from podloze import Podloze
import asset
class Wyspa(Podloze):
    def __init__(self,wlasciwosci ,pos, mnoznik=1,CzyKontronlowane=0):
        super().__init__(wlasciwosci ,pos, mnoznik,CzyKontronlowane)
        self.numerElementu = 1
    def PoWczytaniu(self):
        self.orginalImg=(asset.imgLatajacaWyspa)
        self.img = pygame.image.load(self.orginalImg)
        self.img = pygame.transform.rotozoom(self.img, 0, self.mnoznik)
        self.__init__([self.main,self.orginalImg,self.d,self.szerokosc],self.pos,self.mnoznik,self.CzyKontronlowane)
    def UstawMotyw(self, styl):
        if styl == 1:
            self.img = pygame.image.load(asset.imgLatajacaWyspa)
        elif styl == 2:
            self.img = pygame.image.load(asset.imgLatajacaWyspaM2)