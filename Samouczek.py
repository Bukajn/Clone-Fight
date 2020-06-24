import pygame,asset
from Poziom import Poziom
from Poziom import PrzedmiotInteraktywny
class Samouczek(Poziom):
    def __init__(self,main):
        self.main= main
        self.mapa="samouczek"
        self.styl=2
        self.DomColour = (125, 161, 10)
        self.obiekty = [[pygame.Rect(-2, 311, 802, 402),self.DomColour],[pygame.Rect(-2, -73, 802, 102),self.DomColour],[pygame.Rect(698, 0, 107, 211),self.DomColour],
                        [pygame.Rect(-2, 0, 107, 311),self.DomColour],
                        PrzedmiotInteraktywny(self.main,
                                              asset.imgDrzwi,asset.imgDrzwiObramowka,
                                              asset.imgDrzwiOtwarte,asset.imgDrzwiOtwarteObramowka,
                                              (700,211),
                                              self.OtworzDrzwi,self.ZamknijDrzwi,
                                              asset.soundDoor,asset.soundDoor)]#[pygame.Rect(700, 211, 10, 100),(99, 63, 8)]

        super().__init__(main,self.mapa,self.styl)

        self.UstawWlasciwosci()
    def UstawWlasciwosci(self):
        super().UstawWlasciwosc()
        print(self.obiektyDoKontrolowania)
        #niewidzialnosc i szerokosc
        self.obiektyDoKontrolowania[0].CzyWyswietlac = False
        self.obiektyDoKontrolowania[0].d=10
    def OtworzDrzwi(self):
        self.obiektyDoKontrolowania[0].CzyKolizja=False
    def ZamknijDrzwi(self):
        self.obiektyDoKontrolowania[0].CzyKolizja = True

    def wys(self):
        #print(pygame.mouse.get_pos())
        for i in self.obiekty:
            if type(i) == list:
                if type(i[0]) == pygame.Rect:
                    pygame.draw.rect(self.main.screen,i[1],i[0])
            else:
                i.wys()
