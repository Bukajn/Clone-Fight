import pygame
from podloze import Podloze
class Teren(object):
    def __init__(self,main):
        self.main = main
        self.elements=[[self.main,pygame.image.load("assets/podłoga.png"),800,102],[self.main,pygame.image.load("assets/latajaca_wyspa.png"),102,32]]
        self.img = pygame.image.load("assets/podłoga.png")
        self.pods=[Podloze(self.elements[0],(0,500)),Podloze(self.elements[0],(802,420)),Podloze(self.elements[0],(-800,420)),Podloze(self.elements[1],(100,300))]
        self.towys=[]
        self.speed=8
        self.Left = 0
        self.Right = 0

        self.delta=0.0
        self.max_tps=main.max_tps
        self.clock=pygame.time.Clock()
    def wys(self):
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
    def CollisionWithUnderFloar(self):
        a = []
        for i in self.towys:
            x = i.IsCollisionUnder(self.main.Player.pos)
            if x != None:
                a.append(x)
        #print(a)
        if a != []:
            return max(a)
        else:
            return 0
    def Sterowanie(self):
        self.keys = pygame.key.get_pressed()
        self.Left = 0
        self.Right = 0

        if self.BlokadaRuchuLewo():
            self.Left=1
        if self.BlokadaRuchuPrawo():
            self.Right=1

        if self.keys[pygame.K_a]:

            if self.Left == 0:
                self.Ruch(self.speed)
                self.main.Player.ZmianaTex("assets/playerLeft.png")
        if self.keys[pygame.K_d]:

            if self.Right == 0:
                self.Ruch(-(self.speed))
                self.main.Player.ZmianaTex("assets/playerRight.png")
    def Ruch(self,speed):
        for i in self.pods:  # ruch
            i.pos.x += speed

    def BlokadaRuchuLewo(self):
        for i in self.towys:
            if i.IsCollisionNext("right"):
                return True
    def BlokadaRuchuPrawo(self):
        for i in self.towys:
            if i.IsCollisionNext("left"):
                return True

    def Zegar(self):
        self.delta+=self.clock.tick()/1000.0
        i=0
        while self.delta>1/self.max_tps:
            i+=1
            self.delta-=1/self.max_tps
        return i