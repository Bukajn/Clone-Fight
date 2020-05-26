import pygame
from podloze import Podloze
class Teren(object):
    def __init__(self,main):
        self.img = pygame.image.load("assets/podłoga.png")
        self.main = main
        self.pods=[Podloze(main, self.img, pygame.Vector2(-1, 500),800,102),Podloze(main, self.img, pygame.Vector2(800, 480),800,102),Podloze(main, self.img, pygame.Vector2(-802, 420),800,102)]
        self.towys=[]
        self.speed=2
    def wys(self):

        self.towys = []
        for i in self.pods:
            if i.checkIsItToWys():
                self.towys.append(i)
        self.Sterowanie()
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
        self.Left=0
        self.Right=0
        self.BlokadaRuchuLewo()
        self.BlokadaRuchuPrawo()
        if self.keys[pygame.K_a]:

            if self.Left == 0:
                for i in self.pods:#ruch
                    i.pos.x+=self.speed

        if self.keys[pygame.K_d]:

            if self.Right == 0:
                for i in self.pods:
                    i.pos.x -= self.speed
    def BlokadaRuchuLewo(self):
        a = []
        x = None
        for i in self.towys:
            x = i.IsCollisionNext("right")  # pobranie wartości punktów
        if x != None:
            for i in x:
                a.append(i)
        if a != []:
            for i in a:
                if i.x > self.main.Player.pos.x and 0 < i.x - self.main.Player.pos.x < 20:  # sprawdzenie czy zachodzi kolizja
                    self.Left = 1
                    for b in self.pods:  # ruch
                        b.pos.x -= i.x - (1 + self.main.Player.pos.x)
    def BlokadaRuchuPrawo(self):
        a=[]
        for i in self.towys:
            a = []
            x = i.IsCollisionNext("left")  # pobranie wartości punktów
        if x != None:
            for i in x:
                a.append(i)
        if a != []:
            for i in a:
                if i.x < self.main.Player.pos.x + 64 and 0 < (self.main.Player.pos.x + 64) - i.x < 30:  # sprawdzenie czy zachodzi kolizja
                    self.Right = 1
                    for b in self.pods:  # ruch
                        b.pos.x += (-1 + self.main.Player.pos.x+64)-i.x