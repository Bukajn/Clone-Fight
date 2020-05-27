import pygame
from podloze import Podloze
class Teren(object):
    def __init__(self,main):
        self.img = pygame.image.load("assets/podłoga.png")
        self.main = main
        self.pods=[Podloze(main, self.img, pygame.Vector2(-1, 500),800,102),Podloze(main, self.img, pygame.Vector2(800, 420),800,102),Podloze(main, self.img, pygame.Vector2(-802, 420),800,102)]
        self.towys=[]
        self.speed=8
        self.Left = 0
        self.Right = 0

        self.delta=0.0
        self.max_tps=main.max_tps
        self.clock=pygame.time.Clock()
    def wys(self):
        if self.main.Player.state!=0:
            self.speed=6
        else:
            self.speed=8
        for i in range(self.Zegar()):
            self.towys = []
            for i in self.pods:
                if i.checkIsItToWys():
                    self.towys.append(i)
            self.Sterowanie()
            for i in self.towys:
                i.wys()
            self.ColisionWithFloar()
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

        self.BlokadaRuchuLewo()
        self.BlokadaRuchuPrawo()
        if self.keys[pygame.K_a]:

            if self.Left == 0:
                for i in self.pods:#ruch
                    i.pos.x+=self.speed
                self.main.Player.ZmianaTex("assets/playerLeft.png")
        if self.keys[pygame.K_d]:

            if self.Right == 0:
                for i in self.pods:
                    i.pos.x -= self.speed
                self.main.Player.ZmianaTex("assets/playerRight.png")
    def BlokadaRuchuLewo(self):
        a = []
        x = None
        self.Left = 0
        for i in self.towys:
            x = i.IsCollisionNext("right")  # pobranie wartości punktów
        if x != None:
            for i in x:
                a.append(i)
        if a != []:
            for i in a:
                if 0> self.main.Player.pos.x+14-i.x>-20:
                    y=(0.5-(self.main.Player.pos.x+14-i.x))
                    i.x -= y
                    for b in self.pods:  # ruch
                        b.pos.x -= y
                if 0 < self.main.Player.pos.x-i.x+14 < 1:  # sprawdzenie czy zachodzi kolizja
                    self.Left = 1


    def BlokadaRuchuPrawo(self):
        a=[]
        self.Right=0
        x=None
        for i in self.towys:
            a = []
            x = i.IsCollisionNext("left")  # pobranie wartości punktów
        if x != None:
            for i in x:
                a.append(i)
        if a != []:
            if 0 > i.x - (self.main.Player.pos.x+self.main.Player.szerokosc-14)>-20 :
                y = (0.5 - (i.x-(self.main.Player.pos.x +self.main.Player.szerokosc-14)))
                i.x += y
                for b in self.pods:  # ruch
                    b.pos.x += y
            if 0 < i.x - (self.main.Player.pos.x+self.main.Player.szerokosc-14)  < 1:  # sprawdzenie czy zachodzi kolizja
                self.Right = 1
    def Zegar(self):
        self.delta+=self.clock.tick()/1000.0
        i=0
        while self.delta>1/self.max_tps:
            i+=1
            self.delta-=1/self.max_tps
        return i