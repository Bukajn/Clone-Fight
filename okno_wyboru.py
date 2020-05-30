import pygame

class OknoWyboru(object):
    def __init__(self,main):
        self.main = main
        self.pos = pygame.Vector2(30,51)
        self.okno = pygame.Rect(self.pos.x,self.pos.y,750,500)
        self.przyciskZamykania = pygame.Rect(750,51,30,30)
        self.gornyPasek = pygame.Rect(30,51,720,30)
        self.elementy =[]
        self.UtworzElementy()
    def wys(self):
        pygame.draw.rect(self.main.screen,(0,0,0),self.okno)
        pygame.draw.rect(self.main.screen, (255, 0, 0), self.przyciskZamykania)
        pygame.draw.rect(self.main.screen, (128, 128, 128), self.gornyPasek)
        self.WyswietlElemnty()
        self.CzyKlikniety()
    def CzyKlikniety(self):
        mousePos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if mousePos[0]> 750 and mousePos[0]<780:
                if mousePos[1] > 51 and mousePos[1] < 81:
                    self.main.create_maps.otwarteOknoWyboru=False
    def UtworzElementy(self):
        pozycja = pygame.Vector2(self.pos.x+10,self.pos.y+50)
        for i in range(len(self.main.Teren.elements)):
            self.elementy.append(ElementyDoWyboru(self.main.Teren.elements[i],(pozycja.x,pozycja.y)))
            pozycja.x += 120
    def WyswietlElemnty(self):
        for i in self.elementy:
            i.Wyswietl()
class ElementyDoWyboru(object):
    def __init__(self,wlasciwosci,pos):
        self.main = wlasciwosci[0]
        self.img=wlasciwosci[1]
        self.dlugosc = wlasciwosci[2]
        self.szerokosc = wlasciwosci[3]
        self.dlugoscPola = 100
        self.szerokoscPola =100
        self.pos = pygame.Vector2(pos)
        self.pole = pygame.Rect(self.pos.x,self.pos.y,self.dlugoscPola,self.szerokoscPola)
        self.mnoznik = 90/self.dlugosc
        self.ZmianaWielkosci(self.mnoznik)
    def ZmianaWielkosci(self, mnoznik):
        self.img = pygame.transform.rotozoom(self.img, 0, mnoznik)
    def Wyswietl(self):
        pygame.draw.rect(self.main.screen,(128,128,128),self.pole)
        self.main.screen.blit(self.img, (self.pos.x+5, self.pos.y+self.szerokoscPola/2))
        self.CzyNajechany()
    def CzyNajechany(self):
        mousePos = pygame.mouse.get_pos()
        if mousePos[0] > self.pos.x and mousePos[0] < self.pos.x+self.dlugosc and mousePos[1] > self.pos.y and mousePos[1] < self.pos.y+self.szerokosc:
            if self.mnoznik == 90/self.dlugosc:
                self.mnoznik=self.szerokosc/90
                self.ZmianaWielkosci(self.mnoznik)
        elif self.mnoznik == self.szerokosc/90:
            self.mnoznik=90/self.dlugosc
            self.ZmianaWielkosci(self.mnoznik)
