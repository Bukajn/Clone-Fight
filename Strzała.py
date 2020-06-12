import pygame
import asset
import math
class Strzała(object):
    def __init__(self,main,pos,kierunek,img,cel):
        self.main = main
        self.pos = pygame.Vector2(pos)
        self.pozadanaPozycja = self.pos
        self.kierunek = pygame.Vector2(kierunek)
        self.img = img
        self.szerokosc=15
        self.speed=None
        self.speedY=0
        self.iloscOdbic=0
        self.maxodbic=1
        self.clock = pygame.time.Clock()
        self.delta=0.0
        self.max_tps=60
        self.widoczny =True
        self.cel =cel
    def wys(self):

        for i in range(self.Zegar()):
            wysokoscSufitu = self.main.Teren.CollisionWithUnderFloar(self.pos+(0,7.5), self.szerokosc)#granica wysokosci
            wysokoscPodloza=self.main.Teren.ColisionWithFloar(self.pos,self.szerokosc)
            self.pojscieNaskos(self.kierunek)
            self.SprawdzanieKolizji(wysokoscSufitu,wysokoscPodloza)

            if self.iloscOdbic>self.maxodbic:
                self.Usun()
            self.pos.x = self.pozadanaPozycja.x
            self.main.screen.blit(self.img, self.pos)
        self.main.screen.blit(self.img, self.pos)

    def SprawdzanieKolizji(self,wysokoscsufitu,wysokoscPodloza):
        if self.pos.y<=wysokoscsufitu and self.speedY<0 or self.pos.y>=wysokoscPodloza and self.speedY>0:
            self.speedY*=-1
            self.iloscOdbic+=1

        elif self.main.Teren.CollisionNextTo("left",self.szerokosc,self.pos,self) or self.main.Teren.CollisionNextTo("right",self.szerokosc,self.pos,self):
            self.speedX*=-1
            self.iloscOdbic += 1
        if self.cel=="player":
            self.KolizjaZgraczem()
        elif self.cel=="enemy":
            self.KolizjaZwrogiem()
    def KolizjaZgraczem(self):
        if self.main.IsCollision(pygame.Vector2(self.pos.x+self.szerokosc/2,self.pos.y+self.szerokosc/2),pygame.Vector2(self.main.Player.pos.x+self.main.Player.szerokosc/2,self.main.Player.pos.y+self.main.Player.szerokosc/2),40):
            self.main.Player.HPdoDodania(-10)
            self.Usun()
    def KolizjaZwrogiem(self):
        for i in self.main.Teren.enemy:
            if self.main.IsCollision(pygame.Vector2(self.pos.x+self.szerokosc/2,self.pos.y+self.szerokosc/2),pygame.Vector2(i.pos.x+i.szerokosc/2,i.pos.y+i.szerokosc/2),40):
                i.HPdoDodania(-10)
                self.Usun()
    def Zmienpolozenie(self,x):
        self.pozadanaPozycja.x+=x
    def checkIsItToWys(self):
        if self.pos.x > -1000 and self.pos.x < 800:
            return True
        else:
            self.Usun()
    def pojscieNaskos(self,pos):
        if self.speed==None:
            self.speed =10
            odlegloscX = pos.x - (self.pos.x+ 7.5)
            odlegloscY = pos.y - (self.pos.y+ 7.5)
            odlegloscX = math.fabs(odlegloscX)
            odlegloscY = math.fabs(odlegloscY)
            if odlegloscX>odlegloscY:
                self.speedX = self.speed
                self.speedY = odlegloscY/(odlegloscX/self.speedX)
            else:

                self.speedY=self.speed
                self.speedX = odlegloscX/(odlegloscY/self.speedY)

            if pos.x - self.pos.x<0:
                self.speedX*=-1
            if pos.y - self.pos.y<0:
                self.speedY *= -1

        self.pozadanaPozycja.x+=self.speedX
        self.pos.y+=self.speedY

    def Usun(self):
        if self in self.main.Teren.pods:
            self.main.Teren.pods.remove(self)
    def Zegar(self):
        self.delta+=self.clock.tick()/1000.0
        i=0
        while self.delta>1/self.max_tps:
            i+=1
            self.delta-=1/self.max_tps
        return i
