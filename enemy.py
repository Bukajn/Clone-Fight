import pygame, random
import asset
from Postac import Postac
class Enemy(Postac):
    def __init__(self,wlasciwosci,pos):
        super().__init__(wlasciwosci[0])
        self.imgRight=pygame.image.load(asset.imgWrogPrawo)
        self.imgRight=pygame.transform.rotozoom(self.imgRight,0,1.5)
        self.RightReka=pygame.image.load(asset.imgWrogRekaRight)
        self.RightReka=pygame.transform.rotozoom(self.RightReka,0,1.5)
        self.szerokosc=wlasciwosci[2]*1.5
        self.img = self.imgRight
        self.imgReka=self.RightReka
        self.imgstrzala=pygame.image.load(asset.imgStrzalaWrog)
        self.pos=pygame.Vector2(pos)
        self.podazajzamysza = False
        self.numerElementu=3
        self.cooldown=1
        self.celStrzalu = "player"
        self.punktkierunkowyStrzlu=pygame.Vector2(self.main.Player.pos.x+self.main.Player.szerokosc/2,self.main.Player.pos.y+self.main.Player.szerokosc/2)
    def __str__(self):
        return ("|" + str(self.numerElementu) + ",(" + str(self.pos.x) + ";" + str(self.pos.y) + ")" + "%")
    def wys(self):
        if self.main.CzyKreatorOtworzony==False:
            super().wys()
            if self.state==0:
                #self.skocz=True
                self.strzel=True
            if self.czasUplyniety < self.cooldown - 0.5:
                self.punktkierunkowyStrzlu = pygame.Vector2((self.main.Player.pos.x + self.main.Player.szerokosc / 2),(self.main.Player.pos.y + self.main.Player.szerokosc / 2))
            else:
                self.punktkierunkowyStrzlu = pygame.Vector2(self.punktkierunkowyStrzlu.x+random.randint(-10,10),self.punktkierunkowyStrzlu.y+random.randint(-10,10))
        else:
            self.main.screen.blit(self.img, self.pos)
            if self.podazajzamysza:
                self.pos=pygame.Vector2(pygame.mouse.get_pos())
            if self.podazajzamysza and pygame.mouse.get_pressed()[0]:
                self.podazajzamysza = False

    # funkcje do poprawnego wyświetlania
    def checkIsItToWys(self):
        if self.pos.x > -100 and self.pos.x < 800:
            return True
    def Zmienpolozenie(self,x):
        self.pos.x+=x
    def CzyKlikniety(self):
        mousePos = pygame.mouse.get_pos()
        if mousePos[0]> self.pos.x and mousePos[0]<self.pos.x+self.szerokosc:
            if mousePos[1] > self.pos.y and mousePos[1] < self.pos.y+self.szerokosc:
                return self
    def WysNapis(self,colour):
        self.font = pygame.font.Font(asset.czcionkaRoboto, 16)
        self.napis = self.font.render(str(self.pos), True, colour)
        self.main.screen.blit(self.napis,(self.pos.x+self.szerokosc/2,self.pos.y+self.szerokosc/2))
    def Zmianapolozenia(self,stan):

        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_UP] and (self.wczesniejszystan[pygame.K_UP] !=self.keys[pygame.K_UP] or  stan =="ciagly"):
            self.pos.y-=1
        if self.keys[pygame.K_DOWN] and (self.wczesniejszystan[pygame.K_DOWN] !=self.keys[pygame.K_DOWN]or  stan =="ciagly"):
            self.pos.y+=1
        if self.keys[pygame.K_RIGHT] and (self.wczesniejszystan[pygame.K_RIGHT] !=self.keys[pygame.K_RIGHT]or  stan =="ciagly"):
            self.pos.x+=1
        if self.keys[pygame.K_LEFT] and (self.wczesniejszystan[pygame.K_LEFT] !=self.keys[pygame.K_LEFT]or  stan =="ciagly"):
            self.pos.x-=1
        if self.keys[pygame.K_DELETE]:
            self.main.Teren.pods.remove(self)
            self.main.create_maps.obiekt = None
        self.wczesniejszystan = self.keys