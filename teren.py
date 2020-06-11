import pygame
from podloze import Podloze
from wyspa import Wyspa
from mana_coin import Mana_coin
from enemy import  Enemy
import asset

class Teren(object):
    def __init__(self,main):
        self.main = main
        self.elements=[[self.main,pygame.image.load(asset.imgPodloze),800,102],[self.main,pygame.image.load(asset.imgLatajacaWyspa),102,32],[self.main,pygame.image.load(asset.imgManaCoin),32,32],[self.main,pygame.image.load(asset.imgWrogPrawo),64,64]]


        self.pods=[]
        self.enemy=[]
        self.towys=[]
        self.speed=8
        self.Left = 0
        self.Right = 0

        self.delta=0.0
        self.max_tps=main.max_tps
        self.clock=pygame.time.Clock()
    def UtworzElement(self,numerElementu,zmienne,podazamyszka=False):
        if numerElementu==0:
            elementdododania =Podloze(zmienne[0],zmienne[1])
        elif numerElementu==1:
            elementdododania = Wyspa(zmienne[0], zmienne[1])
        elif numerElementu==2:
            elementdododania = Mana_coin(zmienne[0], zmienne[1])
        elif numerElementu ==3:
            elementdododania=Enemy(zmienne[0],zmienne[1])
            self.enemy.append(elementdododania)
        self.pods.append(elementdododania)
        if podazamyszka:
            elementdododania.podazajzamysza=True

    def wys(self):
        for i in range(self.Zegar()):
            self.towys = []
            for i in self.pods:
                if i.checkIsItToWys():
                    self.towys.append(i)

            self.Sterowanie()
            for i in self.towys:
                i.wys()
            #self.ColisionWithFloar()
        for i in self.towys:
            i.wys()
        #self.ColisionWithFloar()

    def ColisionWithFloar(self,pozycjaObiektu,szerokoscObiektu):
        a=[]
        for i in self.towys:
            try:
                x = i.IsColision(pozycjaObiektu,szerokoscObiektu)
            except AttributeError:
                x=None
            if x != None:
                a.append(x)

        if a!=[]:
            return min(a)
        else:
            return 900
    def CollisionWithUnderFloar(self,pozycjaObiektu,szerokoscObiektu):
        a = []
        for i in self.towys:
            try:
                x = i.IsCollisionUnder(pozycjaObiektu,szerokoscObiektu)
            except AttributeError:
                x=None
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

        if self.CollisionNextTo("right",self.main.Player.szerokosc,self.main.Player.pos,self):
            self.Left=1
        if self.CollisionNextTo("left",self.main.Player.szerokosc,self.main.Player.pos,self):
            self.Right=1

        if self.keys[pygame.K_a]:

            if self.Left == 0:
                self.Ruch(self.speed)

                self.main.Player.ZmianaWLewo()
        if self.keys[pygame.K_d]:

            if self.Right == 0:
                self.Ruch(-(self.speed))

                self.main.Player.ZmianaWprawo()
    def Ruch(self,speed):
        for i in self.pods:  # ruch
            i.Zmienpolozenie(speed)
    def CollisionNextTo(self,side,szerokosc,pos,obiektwywołujący):
        for i in self.towys:
            try:
                if i.IsCollisionNext(side,szerokosc,pos,obiektwywołujący):
                    return True
            except AttributeError:
                pass
    def Zegar(self):
        self.delta+=self.clock.tick()/1000.0
        i=0
        while self.delta>1/self.max_tps:
            i+=1
            self.delta-=1/self.max_tps
        return i