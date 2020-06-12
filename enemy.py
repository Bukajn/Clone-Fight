import pygame, random, decimal
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
        self.PasekZdrowia = pygame.Rect(self.pos.x,self.pos.y,self.szerokosc,5)
        self.max_hp=30
        self.hp=self.max_hp
        self.hpdododania=0
        self.shootsound = pygame.mixer.Sound(asset.soundWrogStrzal)
        self.shootsound.set_volume(0.1)
    def __str__(self):
        return ("|" + str(self.numerElementu) + ",(" + str(self.pos.x) + ";" + str(self.pos.y) + ")" + "%")
    def wys(self):
        if self.main.CzyKreatorOtworzony==False:
            super().wys()
            self.AnimacjaPaska()
            if self.hp - self.hpdododania>0:
                pygame.draw.rect(self.main.screen,(0,255,0),self.PasekZdrowia)
            else:
                self.Smierc()
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
        if not self in self.main.Teren.pods and self in self.main.Teren.enemy:
            self.main.Teren.enemy.remove(self)
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
    def HPdoDodania(self,ilosc):
        if self.hp+ilosc<self.max_hp:
            self.hp+=ilosc
            self.hpdododania +=ilosc
        else:
            self.hp = self.max_hp
            self.hpdododania+=self.max_hp-self.hp
    def AnimacjaPaska(self):
        self.speedAnimacji = 2
        self.speedAnimacji = int(self.hpdododania)
        if self.speedAnimacji < 0:
            self.speedAnimacji *= -1
        if 0 <= self.speedAnimacji < 2:
            self.speedAnimacji = 2
        if self.speedAnimacji> 10:
            self.speedAnimacji = 10

        for i in range(self.speedAnimacji):
            if self.hpdododania > 0:
                self.hpdododania -= 0.01
                self.hpdododania = float(decimal.Decimal(str(self.hpdododania)).quantize(decimal.Decimal('0.00')))
            elif self.hpdododania < 0 and (self.hp - self.hpdododania)/self.max_hp>0:
                self.hpdododania += 0.01
                self.hpdododania = float(decimal.Decimal(str(self.hpdododania)).quantize(decimal.Decimal('0.00')))

        self.PasekZdrowia = pygame.Rect(self.pos.x + 20, self.pos.y - 10, ((self.hp - self.hpdododania) / self.max_hp) * 56, 5)
    def Smierc(self):
        if self in self.main.Teren.pods and self in self.main.Teren.enemy:
            losowa = random.randint(0, 1)
            if losowa == 0:
                self.main.Teren.UtworzElement(2,[self.main.Teren.elements[2],(self.pos.x+self.szerokosc/2,self.pos.y+self.szerokosc/2)])
            else:
                self.main.Teren.UtworzElement(4,[self.main.Teren.elements[4],(self.pos.x+self.szerokosc/2,self.pos.y+self.szerokosc/2)])

            self.main.Teren.pods.remove(self)
            self.main.Teren.enemy.remove(self)
