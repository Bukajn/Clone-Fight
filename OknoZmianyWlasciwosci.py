import pygame
from button import Przycisk
class Okno():
    def __init__(self,main,obiekt):
        self.main=main
        self.obiekt=obiekt
        self.szerokosc=150
        self.wysokosc =200
        self.pos = pygame.Vector2(self.obiekt.pos.x - self.szerokosc - 10, self.obiekt.pos.y)
        self.Pole = pygame.Rect(self.pos.x, self.pos.y, self.szerokosc, self.wysokosc)
        self.Pasekgorny = pygame.Rect(self.pos.x, self.pos.y, self.szerokosc, 20)
        self.przyciskZamykania = Przycisk(self.main,"",pygame.Vector2(20,20),self.pos+pygame.Vector2(self.szerokosc-20,0),(255,0,0),0,self.Zamknij)
    def wys(self):
        self.ZmianaPozycji()
        pygame.draw.rect(self.main.screen,(0,0,0),self.Pole)
        pygame.draw.rect(self.main.screen, (128, 128, 128), self.Pasekgorny)
        self.przyciskZamykania.Wys()
    def ZmianaPozycji(self):
        self.pos = pygame.Vector2(self.obiekt.pos.x - self.szerokosc - 10, self.obiekt.pos.y)
        self.Pole = pygame.Rect(self.pos.x, self.pos.y, self.szerokosc, self.wysokosc)
        self.Pasekgorny = pygame.Rect(self.pos.x, self.pos.y, self.szerokosc, 20)
        self.przyciskZamykania.pos = self.pos+pygame.Vector2(self.szerokosc-20,0)


    def Czynajechany(self):
        mousePos = pygame.mouse.get_pos()
        if mousePos[0] > self.pos.x and mousePos[0] < self.pos.x + self.szerokosc:
            if mousePos[1] > self.pos.y and mousePos[1] < self.pos.y + self.wysokosc:
                return True
        return False
    def Zamknij(self):

        self.main.create_maps.oknowlasciwosci=None
