import pygame
from podloze import Podloze
class Teren(object):
    def __init__(self,main):
        self.img = pygame.image.load("assets/podłoga.png")
        self.main = main
        self.pods=[Podloze(main, self.img, pygame.Vector2(-1, 500),800,102),Podloze(main, self.img, pygame.Vector2(1000, 500),800,102)]
        self.towys=[]
        self.speed=2
    def wys(self):
        self.Sterowanie()
        self.towys = []
        for i in self.pods:
            if i.checkIsItToWys():
                self.towys.append(i)
        for i in self.towys:
            i.wys()
        self.ColisionWithFloar()
    def ColisionWithFloar(self):
        a=[]
        for i in self.towys:
            x = i.IsColision(self.main.Player.pos)
            if x != None:
                a.append(x)

        if a!=[]:
            return min(a)
        else:
            return 900
    def Sterowanie(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_a]:
            for i in self.pods:
                i.pos.x+=self.speed
        if self.keys[pygame.K_d]:
            for i in self.pods:
                i.pos.x -= self.speed