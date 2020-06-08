import pygame
import asset
import math
class Strzała(object):
    def __init__(self,main,pos,kierunek):
        self.main = main
        self.pos = pygame.Vector2(pos)
        self.kierunek = pygame.Vector2(kierunek)
        self.img = pygame.image.load(asset.imgStrzala)
        self.szerokosc=15
        self.speed=None
        self.speedY=0
        self.iloscOdbic=0
        self.maxodbic=1
    def wys(self):
        wysokoscSufitu = self.main.Teren.CollisionWithUnderFloar(self.pos, self.szerokosc)#granica wysokosci
        wysokoscPodloza=self.main.Teren.ColisionWithFloar(self.pos,self.szerokosc)
        self.main.screen.blit(self.img,self.pos)
        self.pojscieNaskos(self.kierunek)
        self.SprawdzanieKolizji(wysokoscSufitu,wysokoscPodloza)
        if self.iloscOdbic>self.maxodbic:
            self.Usun()
    def SprawdzanieKolizji(self,wysokoscsufitu,wysokoscPodloza):
        if self.pos.y<=wysokoscsufitu or self.pos.y>=wysokoscPodloza:
            self.speedY*=-1
            self.iloscOdbic+=1
            #self.Usun()
        if self.main.Teren.CollisionNextTo("left",self.szerokosc,self.pos,self):
            self.speedX*=-1
            self.iloscOdbic += 1
        if self.main.Teren.CollisionNextTo("right",self.szerokosc,self.pos,self):
            self.speedX*=-1
            self.iloscOdbic += 1
    def Zmienpolozenie(self,x):
        self.pos.x+=x
    def checkIsItToWys(self):
        if self.pos.x > -1000 and self.pos.x < 2000:
            return True
    def pojscieNaskos(self,pos):
        if self.speed==None:
            self.speed =3
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

        self.pos.x+=self.speedX
        self.pos.y+=self.speedY

    def Usun(self):
        if self in self.main.Teren.pods:
            self.main.Teren.pods.remove(self)
