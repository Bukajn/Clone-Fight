import pygame,math
from pygame import mixer
import  asset
from Strzała import Strzała
import enemy

class Postac(object):
    def __init__(self,main):
        self.main = main

        self.RightReka = pygame.image.load(asset.imgRekaRight)
        self.LeftReka = pygame.image.load(asset.imgRekaLeft)
        self.imgRight=pygame.image.load(asset.imgPlayerRight)

        self.imgLeft=pygame.image.load(asset.imgPlayerLeft)
        self.imgstrzala=pygame.image.load(asset.imgStrzala)

        self.img = pygame.image.load(asset.imgPlayerRight)
        self.imgReka = self.RightReka
        self.jumpSound = self.main.relugacjaDzwiekow.soundJump
        self.shootsound= self.main.relugacjaDzwiekow.shootsound

        self.szerokosc=64


        #self.img = pygame.transform.rotate(self.img,45)

        self.posReka = self.pos
        self.state = 1 # 0=na ziemie 1=podczas spadania 2=podczas skoku
        self.speed = pygame.Vector2(0,0)
        self.speedGravitation=0.1
        self.speedJump=-8
        self.wysSkoku=150
        self.old_pos_y=0
        self.ruch = "prawo"

        self.clock=pygame.time.Clock()
        self.delta=0.0
        self.max_tps=self.main.max_tps

        self.OdlegloscRekiOdRoguPrawo = pygame.Vector2(37,31)

        self.OdlegloscRekiOdRoguLewo = pygame.Vector2(-27, -30)

        self.Rotate=0
        self.ZmianaWielkosci(1.5)

        #cooldown
        self.cooldownZegar = pygame.time.Clock()
        self.cooldown = 2
        self.czasUplyniety=0

        self.skocz=False
        self.keys = pygame.key.get_pressed()
        self.strzel=False
        self.celStrzalu=""
        self.punktkierunkowyStrzlu=None

        self.max_hp=100
        self.hp=self.max_hp

        self.mocStrzalu = 10

        self.CzyMozeSpascPonizej600=True
        self.wczesciejszyheiht=0
        self.CzydzialaGrawitacja=True
        self.czyMozeStrzelac=True
        self.czyWyswietlac=True
        #animacja
        self.animacja=False
        self.napraw=False
        self.zegarAnimacji = pygame.time.Clock()
        self.animacjaCzasMiniety=0
        self.klatkiWPrawo=[]
        self.klatkiWLewo=[]
        self.predkoscAnimacji=1
        self._numerKlatki=0
        self._kierunekAnimacji=True
    def wys(self):
        #print(pygame.mouse.get_pos())
        if self.czyWyswietlac:
            for i in range(self.Zegar()):
                self.Physik()
                self.Ruch()
                if self.czasUplyniety < self.cooldown:
                    self.czasUplyniety+= self.cooldownZegar.tick()/1000
                    self.strzel = False
                else:
                    self.cooldownZegar.tick()
                    if self.strzel and self.czyMozeStrzelac:
                        self.strzel= False
                        self.czasUplyniety = 0
                        self.Strzał()
                        self.shootsound.play()
            self.Ruch()
    def Ruch(self):
        if self.ruch=="prawo":
            self.RuchwPrawo()
        elif self.ruch =="lewo":
            self.RuchWlewo()
    def RuchwPrawo(self):
        mouse_x, mouse_y = self.punktkierunkowyStrzlu
        rel_x, rel_y = mouse_x - self.pos.x, mouse_y - self.pos.y
        self.Rotate = ((180 / math.pi) * math.atan2(rel_y, rel_x))-40
        self.PunktZaczepieniaRekiPrawo = pygame.Vector2(self.pos.x + (self.OdlegloscRekiOdRoguPrawo.x),self.pos.y + (self.OdlegloscRekiOdRoguPrawo.y))
        if self.animacja == True:
            self.animacjaChodu(self.klatkiWPrawo, self.predkoscAnimacji)
        elif self.napraw:
            self.img = self.imgRight
            self.napraw=False
        self.main.screen.blit(self.img, self.pos)
        rotate_reka, rect = self.ObrotPunktu(self.imgReka,self.Rotate,self.PunktZaczepieniaRekiPrawo,pygame.math.Vector2(-6,4))
        self.main.screen.blit(rotate_reka,rect)


    def RuchWlewo(self):
        mouse_x, mouse_y = self.punktkierunkowyStrzlu
        rel_x, rel_y = mouse_x - self.pos.x, mouse_y - self.pos.y
        self.Rotate = ((180 / math.pi) * math.atan2(rel_y, rel_x))+220
        self.PunktZaczepieniaRekiLewo = pygame.Vector2(self.pos.x + (-self.OdlegloscRekiOdRoguLewo.x),self.pos.y + (-self.OdlegloscRekiOdRoguLewo.y))
        if self.animacja == True:
            self.animacjaChodu(self.klatkiWLewo, self.predkoscAnimacji)
        elif self.napraw:
            self.img = self.imgLeft
            self.napraw=False
        self.main.screen.blit(self.img, self.pos)
        rotate_reka, rect = self.ObrotPunktu(self.imgReka, self.Rotate, self.PunktZaczepieniaRekiLewo,pygame.math.Vector2(6, 4))
        self.main.screen.blit(rotate_reka, rect)

    def animacjaChodu(self, klaltki, predkosc):
        if self.animacjaCzasMiniety < predkosc:
            self.animacjaCzasMiniety+= self.zegarAnimacji.tick()/1000
        else:
            self.animacjaCzasMiniety=0
            if self._kierunekAnimacji:
                self._numerKlatki+=1
            else:
                self._numerKlatki-=1

            #sprawdzenie czy nie zaszło poza zakres
            if self._numerKlatki> len(klaltki)-1:
                self._numerKlatki-=1
                self._kierunekAnimacji = False
            elif self._numerKlatki<0:
                self._numerKlatki+=1
                self._kierunekAnimacji=True


        self.img = klaltki[self._numerKlatki]
        self.napraw=True
    def Strzał(self):
        if self.main.CzyKreatorOtworzony==False and self.czyMozeStrzelac:
            self.main.Teren.pods.append(Strzała(self.main,(self.pos.x+self.szerokosc/2,self.pos.y+self.szerokosc/2),self.punktkierunkowyStrzlu,self.imgstrzala,self.celStrzalu,self.mocStrzalu))
        #(self.pos.x+self.szerokosc/2,self.pos.y+self.szerokosc/2-8)
    def ObrotPunktu(self,image, promien, pivot, przesuniecie):

        rotate_img = pygame.transform.rotozoom(image, -promien, 1)  # Rotate the image.
        rotated_offset = przesuniecie.rotate(promien)  # Rotate the offset vector.

        rect = rotate_img.get_rect(center=pivot+rotated_offset)
        return rotate_img,rect
    def Physik(self):

        height=self.main.Teren.ColisionWithFloar(self.pos,self.szerokosc) #przyjęcie wysokości podłoż
        if self.CzyMozeSpascPonizej600 ==False and height > 600 and self.wczesciejszyheiht!=0:
            height=self.wczesciejszyheiht
        heightSufit=self.main.Teren.CollisionWithUnderFloar(self.pos,self.szerokosc)#przyjęcie wysokości sufitu

        self.grawitacja(height,heightSufit)


        self.jump(heightSufit)

        self.pos.y+=self.speed.y
        self.grawitacja(height,heightSufit)
        self.jump(heightSufit)
        self.wczesciejszyheiht = height
    def grawitacja(self,height,heightSufit):
        if self.pos.y < heightSufit:
            self.speed.y = 1
            self.state = 1
        if self.pos.y < height and self.state!=2:
            self.state=1
            if self.CzydzialaGrawitacja:
                self.speed.y += self.speedGravitation
        elif self.pos.y != self.old_pos_y and self.state == 1: # jest na ziemi
            self.speed.y=0
            self.state=0


        if self.pos.y > height:
            self.pos.y = height
    def jump(self,heightSufit):
        if self.skocz and self.state == 0:
            self.skocz = False
            self.state = 2
            self.speed.y = self.speedJump
            self.posStart = self.pos.y
        if self.state == 2:
            if self.pos.y+self.szerokosc > self.old_pos_y - self.wysSkoku:
                if self.speed.y < -5:

                    self.speed.y += -(self.speed.y / (self.wysSkoku - (self.posStart - self.pos.y)))
            else:
                self.state = 1
            if self.pos.y<heightSufit:
                self.speed.y=0
                self.state=1
        elif self.state == 0:
            self.old_pos_y = self.pos.y+self.szerokosc
    def ZmianaWielkosci(self, mnoznik):
        self.imgRight = pygame.transform.rotozoom(self.imgRight, 0, mnoznik)
        self.imgLeft = pygame.transform.rotozoom(self.imgLeft, 0, mnoznik)
        self.RightReka= pygame.transform.rotozoom(self.RightReka, 0, mnoznik)
        self.LeftReka=pygame.transform.rotozoom(self.LeftReka, 0, mnoznik)

        self.img =pygame.transform.rotozoom(self.img,0,mnoznik)
        self.imgReka = pygame.transform.rotozoom(self.imgReka, 0, mnoznik)

        self.OdlegloscRekiOdRoguPrawo.x*=mnoznik
        self.OdlegloscRekiOdRoguPrawo.y *= mnoznik
        self.OdlegloscRekiOdRoguLewo.x *= mnoznik
        self.OdlegloscRekiOdRoguLewo.y *= mnoznik
        self.szerokosc*=mnoznik
    def ZmianaWprawo(self):
        self.ruch = "prawo"
        self.img = self.imgRight
        self.imgReka = self.RightReka
    def ZmianaWLewo(self):
        self.ruch = "lewo"
        self.img = self.imgLeft
        self.imgReka=self.LeftReka
    def Zegar(self):
        self.delta+=self.clock.tick()/1000.0
        i=0
        while self.delta>1/self.max_tps:
            i+=1
            self.delta-=1/self.max_tps
        return i
