import pygame, asset
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

        self.elementy=[]
        self.Stworzenielementow()
    def wys(self):
        self.ZmianaPozycji()
        pygame.draw.rect(self.main.screen,(0,0,0),self.Pole)
        pygame.draw.rect(self.main.screen, (128, 128, 128), self.Pasekgorny)

        self.przyciskZamykania.Wys()
        for i in self.elementy:
            i.wys()
    def ZmianaPozycji(self):
        self.pos = pygame.Vector2(self.obiekt.pos.x - self.szerokosc - 10, self.obiekt.pos.y)
        self.Pole = pygame.Rect(self.pos.x, self.pos.y, self.szerokosc, self.wysokosc)
        self.Pasekgorny = pygame.Rect(self.pos.x, self.pos.y, self.szerokosc, 20)
        self.przyciskZamykania.pos = self.pos+pygame.Vector2(self.szerokosc-20,0)
        y=20
        for i in self.elementy:
            i.ZmianaPolozenia(self.pos+pygame.Vector2(0,y))
            y+=30
    def Stworzenielementow(self):
        try:
            ElementyDododania = self.obiekt.wlasciwosciDozmiany
        except:
            return

        for i in ElementyDododania:
            if i[0]=="powiekszenie":
                self.elementy.append(Powiekszanie(self,self.pos+pygame.Vector2(0,20),self.main,i[1],i[2],i[3]))

    def Czynajechany(self):
        mousePos = pygame.mouse.get_pos()
        if mousePos[0] > self.pos.x and mousePos[0] < self.pos.x + self.szerokosc:
            if mousePos[1] > self.pos.y and mousePos[1] < self.pos.y + self.wysokosc:
                return True
        return False
    def Zamknij(self):

        self.main.create_maps.oknowlasciwosci=None
    def WprowadzZmiany(self):
        wlasciwosciDoZwrocenia=[]
        for i in self.elementy:
           wlasciwosciDoZwrocenia.append(i.Zwroc())
        self.obiekt.PrzyjmijWlasciwosci(wlasciwosciDoZwrocenia)
class Powiekszanie():
    def __init__(self,okno,pos,main,tytul,doZmiany,skala):
        self.main = main
        self.pos = pygame.Vector2(pos)
        self.doZmiany=doZmiany
        self.okno=okno
        self.skala=skala
        self.font = pygame.font.Font(asset.czcionkaRoboto,10)
        self.tytul = self.font.render(tytul,True,(255,255,255))
        self.PrzyciskMinus=Przycisk(self.main, "  -", pygame.Vector2(30, 10), self.pos + pygame.Vector2(0, 15), (128, 128, 128), 10, self.Minus)
        self.PrzyciskPlus = Przycisk(self.main, "  +", pygame.Vector2(30, 10), self.pos + pygame.Vector2(120, 15),(128, 128, 128), 10, self.Plus)
        self.liczba = self.font.render(str(self.doZmiany),True,(255,255,255))
    def wys(self):
        self.main.screen.blit(self.tytul, self.pos)
        self.main.screen.blit(self.liczba, self.pos+pygame.Vector2(60,15))
        self.PrzyciskMinus.Wys()
        self.PrzyciskPlus.Wys()
        self.liczba = self.font.render(str(self.doZmiany), True, (255, 255, 255))
    def ZmianaPolozenia(self,pos):
        self.pos =pos
        self.PrzyciskMinus.pos = self.pos+pygame.Vector2(0,15)
        self.PrzyciskPlus.pos = self.pos + pygame.Vector2(120, 15)
    def Plus(self):
        self.doZmiany+=self.skala
        self.okno.WprowadzZmiany()
    def Minus(self):
        if self.doZmiany>0:
            self.doZmiany-=self.skala
            self.okno.WprowadzZmiany()
    def Zwroc(self):
        return self.doZmiany