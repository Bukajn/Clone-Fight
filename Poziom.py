import pygame,copy
from scene import Scene
class Poziom():
    def __init__(self,main,mapa,styl):
        self.main =main
        self.scena = Scene(self.main,"",styl,self)
        self.scena.WczytajMape(mapa)
        self.obiektyDoKontrolowania=[]
        self.przesuniecie=0
    def UstawWlasciwosc(self):
        self.obiektyDoKontrolowania = []
        for i in self.main.Teren.pods:
            try:
                if i:
                    self.obiektyDoKontrolowania.append(i)
            except:
                pass
    def DodajdoTeren(self):
        self.main.Teren.pods.append(self)
        self.Zmienpolozenie(-self.przesuniecie)
        self.UstawWlasciwosci()
    def Przesuniecie(self):
        self.przesuniecie = self.main.Teren.przesuniecie
    def main_loop(self):
        self.DodajdoTeren()
        while True:
            self.scena.main_loop()
    def checkIsItToWys(self):
        return True
    def Zmienpolozenie(self,speed):
        for i in range(len(self.obiekty)):
            if type(self.obiekty[i]) == list:
                self.obiekty[i][0] = self.obiekty[i][0].move(speed,0)
            else:
                self.obiekty[i].Przesun(speed)
class PrzedmiotInteraktywny():
    def __init__(self,main,img,imgO,img2,imgO2,pos,akcja1,akcja2,sound1,sound2):
        self.main = main
        self.img=pygame.image.load(img)
        self.imgO = pygame.image.load(imgO)
        self.img2 = pygame.image.load(img2)
        self.imgO2=pygame.image.load(imgO2)
        self.pos=pygame.Vector2(pos)
        self.akcja1 =akcja1
        self.akcja2 = akcja2
        self.sound1 = pygame.mixer.Sound(sound1)
        self.sound2 = pygame.mixer.Sound(sound2)
        rect = self.img.get_rect()
        self.Rozmiar = pygame.Vector2(rect[2],rect[3])
        self.stan1=True

        self.wczesniejszyKlik=0
    def wys(self):
        if self.stan1:
            self.main.screen.blit(self.img,self.pos)
        else:
            self.main.screen.blit(self.img2, self.pos)
        self.CzyNajechany()
    def Przesun(self,droga):
        self.pos.x+=droga
    def CzyNajechany(self):
        mousePos = pygame.mouse.get_pos()
        if mousePos[0] > self.pos.x and mousePos[0] < self.pos.x + self.Rozmiar.x:
            if mousePos[1] > self.pos.y and mousePos[1] < self.pos.y + self.Rozmiar.y:
                if self.stan1:
                    self.main.screen.blit(self.imgO,self.pos)

                else:
                    self.main.screen.blit(self.imgO2, self.pos)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_e] and keys[pygame.K_e]!=self.wczesniejszyKlik[pygame.K_e]:
                   if self.stan1:
                        self.stan1=False
                        rect = self.img2.get_rect()
                        self.Rozmiar = pygame.Vector2(rect[2], rect[3])
                        self.akcja1()
                        self.sound1.play()

                   else:
                        self.stan1=True
                        rect = self.img.get_rect()
                        self.Rozmiar = pygame.Vector2(rect[2], rect[3])
                        self.akcja2()
                        self.sound2.play()
                self.wczesniejszyKlik = pygame.key.get_pressed()
