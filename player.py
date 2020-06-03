import pygame
from pygame import mixer
import  asset
class Player(object):
    def __init__(self,main):
        self.main = main
        self.img = pygame.image.load(asset.imgPlayerRight)
        self.jumpSound = mixer.Sound(asset.soundJump)
        #self.imgSkok = pygame.transform.rotozoom(self.imgSkok, 0, 1.5)
        self.szerokosc=64
        self.ZmianaWielkosci(1.5)
        self.pos = pygame.Vector2(336,0)#336
        self.state = 1 # 0=na ziemie 1=podczas spadania 2=podczas skoku
        self.speed = pygame.Vector2(0,0)
        self.speedGravitation=0.1
        self.speedJump=-8
        self.wysSkoku=100
        self.old_pos_y=0

        self.clock=pygame.time.Clock()
        self.delta=0.0
        self.max_tps=self.main.max_tps

        #

    def wys(self):
        for i in range(self.Zegar()):
            self.Physik()
            self.main.screen.blit(self.img, self.pos)
        self.main.screen.blit(self.img, self.pos)
    def Physik(self):

        height=self.main.Teren.ColisionWithFloar() #przyjęcie wysokości podłożą
        heightSufit=self.main.Teren.CollisionWithUnderFloar()#przyjęcie wysokości sufitu

        self.grawitacja(height,heightSufit)

        self.keys = pygame.key.get_pressed()

        self.jump(heightSufit)

        self.pos.y+=self.speed.y
        self.grawitacja(height,heightSufit)
        self.jump(heightSufit)
        self.wczesniejszekeys=self.keys
    def grawitacja(self,height,heightSufit):
        if self.pos.y < heightSufit:
            self.speed.y = 1
            self.state = 1
        if self.pos.y < height and self.state!=2:
            self.state=1
            self.speed.y += self.speedGravitation
        elif self.pos.y != self.old_pos_y and self.state == 1: # jest na ziemi
            self.speed.y=0
            self.state=0

            #self.ZmianaTex("assets/playerRight.png")
        if self.pos.y > height:
            self.pos.y = height
    def jump(self,heightSufit):
        if self.keys[pygame.K_SPACE] and self.state == 0 and self.keys[pygame.K_SPACE]!= self.wczesniejszekeys[pygame.K_SPACE]:
            #self.ZmianaTex(self.imgSkok)
            self.jumpSound.play()
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
        self.img = pygame.transform.rotozoom(self.img, 0, mnoznik)
        self.szerokosc*=mnoznik
    def ZmianaTex(self,texture):
        old_szerokosc=self.szerokosc
        self.szerokosc=64
        self.img = pygame.image.load(texture)
        self.ZmianaWielkosci(old_szerokosc/64)
    def Zegar(self):
        self.delta+=self.clock.tick()/1000.0
        i=0
        while self.delta>1/self.max_tps:
            i+=1
            self.delta-=1/self.max_tps
        return i