import pygame
import asset
import math
class Mana_coin(object):
    def __init__(self,wlasciwosci,pos):
        self.numerElementu = 2
        self.main = wlasciwosci[0]
        self.img = wlasciwosci[1]
        self.pos = pygame.Vector2(pos)

        self.dlugosc = wlasciwosci[2]
        self.szerokosc = wlasciwosci[3]

        self.pozycjaYgorna = self.pos.y
        self.pozycjaYdolna = self.pos.y + self.dlugosc/2
        self.kierunek = 'dol'
        self.speed =0.03
        self.speedNaSkos=None
        self.wczesniejszystanKreatora=0
        self.podazajzamysza = False

        self.RuchDoPaska = False
    def __str__(self):
        return ("|"+str(self.numerElementu)+",("+str(self.pos.x)+";"+str(self.pos.y)+")"+"%")
    def wys(self):
        self.main.screen.blit(self.img, self.pos)
        if self.podazajzamysza:
            self.pos = pygame.Vector2(pygame.mouse.get_pos())
        if self.podazajzamysza and pygame.mouse.get_pressed()[0]:
            self.pozycjaYgorna = self.pos.y
            self.pozycjaYdolna = self.pos.y + self.dlugosc / 2
            self.podazajzamysza=False

        if self.main.CzyKreatorOtworzony==False:

            self.ruch()
            self.wczesniejszystanKreatora = self.main.CzyKreatorOtworzony
        elif self.wczesniejszystanKreatora == False:
            self.wczesniejszystanKreatora=True
            self.pos.y = self.pozycjaYgorna
        self.SprawdzanieKolizy()
        if self.RuchDoPaska:
            self.pojscieNaskos(pygame.Vector2(504,548))
    def checkIsItToWys(self):
        if self.pos.x > -1000 and self.pos.x < 2000:
            return True
    def CzyKlikniety(self):
        mousePos = pygame.mouse.get_pos()
        if mousePos[0]> self.pos.x and mousePos[0]<self.pos.x+self.dlugosc:
            if mousePos[1] > self.pos.y and mousePos[1] < self.pos.y+self.szerokosc:
                return self
    def WysNapis(self,colour):
        self.font = pygame.font.Font(asset.czcionkaRoboto, 16)
        self.napis = self.font.render(str(self.pos), True, colour)
        self.main.screen.blit(self.napis, (self.pos.x + self.dlugosc / 2, self.pos.y + self.szerokosc / 2))
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
        self.pozycjaYgorna = self.pos.y
        self.pozycjaYdolna = self.pos.y + self.dlugosc / 2
        self.wczesniejszystan = self.keys
    def ruch(self):
        if self.RuchDoPaska == False:
            if self.pos.y<self.pozycjaYdolna and self.kierunek == 'dol':
                self.pos.y+=self.speed
            else:
                self.kierunek = "gora"
            if self.pos.y> self.pozycjaYgorna and self.kierunek=="gora":
                self.pos.y-=self.speed
            else:
                self.kierunek ="dol"


    def SprawdzanieKolizy(self):
        if self.main.IsCollision(pygame.Vector2(self.pos.x+self.dlugosc,self.pos.y+self.dlugosc),pygame.Vector2(self.main.Player.pos.x+self.main.Player.szerokosc,self.main.Player.pos.y+self.main.Player.szerokosc),80):
            self.RuchDoPaska=True

    def pojscieNaskos(self,pos):
        if self.speedNaSkos==None:
            self.speedNaSkos = 1
            odlegloscX = pos.x - self.pos.x
            odlegloscY = pos.y - self.pos.y
            odlegloscX = math.fabs(odlegloscX)
            odlegloscY = math.fabs(odlegloscY)
            if odlegloscX>odlegloscY:
                print("b")
                self.speedX = self.speedNaSkos
                self.speedY = odlegloscY/(odlegloscX/self.speedX)

            else:

                self.speedY=self.speedNaSkos
                self.speedX = odlegloscX/(odlegloscY/self.speedY)

            if pos.x - self.pos.x<0:
                self.speedX*=-1
            if pos.y - self.pos.y<0:
                self.speedY *= -1
        if pos.x-1<self.pos.x<pos.x+1 and pos.y-1<self.pos.y<pos.y+1:
            self.speedNaSkos=0
            if self in self.main.Teren.pods:
                self.main.Teren.pods.remove(self)
                self.main.GUI.pasekMany.DodawajMane(10)
        else:
            self.pos.x+=self.speedX
            self.pos.y+=self.speedY
    def Zmienpolozenie(self,x):
        if self.RuchDoPaska==False:
            self.pos.x+=x
