import pygame,math
import asset
from OknoZmianyWlasciwosci import Powiekszanie
class Podloze():
    def __init__(self,wlasciwosci,pos,mnoznik=1,Czykontrolowanie=0):
        self.numerElementu = 0
        self.mnoznik = mnoznik
        self.main=wlasciwosci[0]
        self.orginalImg = wlasciwosci[1]
        self.img = pygame.image.load(self.orginalImg)
        self.img = pygame.transform.rotozoom(self.img, 0, self.mnoznik)

        self.pos=pygame.Vector2(pos)
        self.d =wlasciwosci[2]
        self.orginald = self.d
        self.szerokosc=wlasciwosci[3]
        self.orginalszerokosc = self.szerokosc

        self.podazajzamysza=False

        self.CzyKontronlowane =Czykontrolowanie

        self.CzyWyswietlac =True
        self.CzyKolizja=True

        self.speed = None
        self.ruchnaskos=False
        self.pos1=0
        self.pos2=0
        self.wymaganaSpeed=0.1
        self.wlasciwosciDozmiany=[["powiekszenie","Rozmiar",self.mnoznik,0.5],["powiekszenie","Kontrolowanie",self.CzyKontronlowane,1]]
    #def __str__(self):
        # return ("|"+str(self.numerElementu)+",("+str(self.pos.x)+";"+str(self.pos.y)+")"+"%")
    def wys(self):
        if self.CzyWyswietlac:
            self.main.screen.blit(self.img, self.pos)
        if self.podazajzamysza:
            self.pos = pygame.Vector2(pygame.mouse.get_pos())
        if self.podazajzamysza and pygame.mouse.get_pressed()[0]:
            self.podazajzamysza=False

        if self.ruchnaskos:
            self.pojscieNaskos(self.pos1,self.pos2)
    def checkIsItToWys(self):
        if self.pos.x > 0-self.d and self.pos.x < 800:
            return True
    def IsColision(self,pos,szerokosc=0):#kolizcja dla powierzchni
        if self.CzyKolizja:
            if self.pos.x-szerokosc < pos.x <self.pos.x+self.d-15 and self.pos.y>=pos.y+szerokosc:
                return self.pos.y-szerokosc
    def IsCollisionUnder(self,pos,szerokosc=0):
        if self.CzyKolizja:
            if self.pos.x-szerokosc < pos.x <self.pos.x+self.d-15 and self.pos.y+self.szerokosc<pos.y:
                #print(self.pos.y+self.szerokosc)
                return self.pos.y+self.szerokosc
    def IsCollisionNext(self,side,szerokosc,pos,obiektwywołujący):#kolizja dla scianki
        if self.CzyKolizja and self.ruchnaskos==False:
            for i in range(int((self.pos.y+self.szerokosc) - (self.pos.y - (szerokosc-2)))):
                if side == "right":
                    if pos.y<=self.pos.y+i+0.5-(szerokosc-2) and pos.y>=self.pos.y+i-0.5-(szerokosc-2):
                        a=self.pos.x+self.d
                        if 0 > pos.x + 14 - a > -20:
                            y = (0.5 - (pos.x + 14 - a))
                            a -= y
                            try:
                                obiektwywołujący.Ruch(-y)
                            except:
                                pass
                        if 0 < pos.x - a + 14 < 20:  # sprawdzenie czy zachodzi kolizja
                            return True


                elif side == "left":
                    if pos.y<=self.pos.y+i+0.5-(szerokosc-2) and pos.y>=self.pos.y+i-0.5-(szerokosc-2):
                        a=self.pos.x
                        if 0 > a - (pos.x + szerokosc - 14) > -20:
                            y = (0.5 - (a - (pos.x + szerokosc - 14)))
                            a += y
                            try:
                                obiektwywołujący.Ruch(y)
                            except:
                                pass
                        if 0 < a - (pos.x + szerokosc-14) < 20:  # sprawdzenie czy zachodzi kolizja
                            return True
    def CzyKlikniety(self):
        mousePos = pygame.mouse.get_pos()
        if mousePos[0]> self.pos.x and mousePos[0]<self.pos.x+self.d:
            if mousePos[1] > self.pos.y and mousePos[1] < self.pos.y+self.szerokosc:
                return self
    def WysNapis(self,colour):
        self.font = pygame.font.Font(asset.czcionkaRoboto, 16)
        self.napis = self.font.render(str(self.pos), True, colour)
        self.main.screen.blit(self.napis,(self.pos.x+self.d/2,self.pos.y+self.szerokosc/2))
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
    def Zmienpolozenie(self,x):
        self.pos.x+=x
        try:
            self.pos1.x+=x
            self.pos2.x+=x
        except:
            pass
    def PrzygotujDoZapisu(self):
        self.img=None
        #bez zapisu
        self.font=None
        self.napis=None
    def PoWczytaniu(self):
        self.img = pygame.image.load(self.orginalImg)
        self.img = pygame.transform.rotozoom(self.img, 0, self.mnoznik)
        self.__init__([self.main,self.orginalImg,self.d,self.szerokosc],self.pos,self.mnoznik,self.CzyKontronlowane)
    def PrzyjmijWlasciwosci(self,wlasciwosci):
        self.mnoznik = wlasciwosci[0]
        self.CzyKontronlowane=wlasciwosci[1]
        self.wlasciwosciDozmiany = [["powiekszenie", "Rozmiar", self.mnoznik, 0.5],["powiekszenie","Kontrowanie",self.CzyKontronlowane,1]]
        self.ZmienWielkosc()
    def ZmienWielkosc(self):
        self.img = pygame.transform.rotozoom(pygame.image.load(self.orginalImg), 0, self.mnoznik)
        self.d=self.orginald*self.mnoznik
        self.szerokosc=self.orginalszerokosc*self.mnoznik
    def UstawMotyw(self,styl):
        if styl ==1:
            self.img = pygame.image.load(asset.imgPodloze)
        elif styl ==2:
            self.img = pygame.image.load(asset.imgPodlozeM2)
    def __bool__(self):
        if self.CzyKontronlowane==1:
            return True
        return False
    def pojscieNaskos(self,pos1,pos2):

        self.ruchnaskos=True

        if self.speed==None:
            try:

                if self.posP == self.pos1:
                    self.posP =self.pos2
                else:

                    self.posP=self.pos1
            except:
                self.posP = pos1
                self.pos1 = pos1
                self.pos2 = pos2
            self.speed =self.wymaganaSpeed
            odlegloscX = self.posP.x - self.pos.x
            odlegloscY = self.posP.y - self.pos.y
            odlegloscX = math.fabs(odlegloscX)
            odlegloscY = math.fabs(odlegloscY)
            if odlegloscX>odlegloscY:
                self.speedX = self.speed
                try:
                    self.speedY = odlegloscY/(odlegloscX/self.speedX)
                except ZeroDivisionError:
                    self.speedY=0
            else:

                self.speedY=self.speed
                try:
                    self.speedX = odlegloscX/(odlegloscY/self.speedY)
                except ZeroDivisionError:
                    self.speedX=0
            if self.posP.x - self.pos.x<0:
                self.speedX*=-1
            if self.posP.y - self.pos.y<0:
                self.speedY *= -1

        if self.posP.x - 1 < self.pos.x < self.posP.x + 1 and self.posP.y - 1 < self.pos.y < self.posP.y + 1:
            self.speed=None
        else:

            self.pos.x+=self.speedX
            self.pos.y+=self.speedY

            if self.pos.x - self.main.Player.szerokosc < self.main.Player.pos.x < self.pos.x + self.d - 15 and -1<self.pos.y-(self.main.Player.pos.y + self.main.Player.szerokosc)<1 and self.speedY<0:
                self.main.Player.CzydzialaGrawitacja=False
                self.main.Player.pos.y-= self.speed
                self.main.Player.state = 0
            elif self.pos.x - self.main.Player.szerokosc < self.main.Player.pos.x < self.pos.x + self.d - 15 and self.pos.y>self.main.Player.pos.y+self.main.Player.szerokosc:
                self.main.Player.CzydzialaGrawitacja = True
                if -1<self.pos.y-(self.main.Player.pos.y + self.main.Player.szerokosc)<1 and self.speedY>0:
                    self.main.Player.state=0
            if self.pos.x - self.main.Player.szerokosc < self.main.Player.pos.x < self.pos.x + self.d - 15 and -1<self.pos.y-(self.main.Player.pos.y + self.main.Player.szerokosc)<1:
                if self.speedX>0:
                    self.speedX = 1
                    self.main.Teren.Ruch(-self.speedX)
                elif self.speedX<0:
                    self.speedX = 1
                    self.main.Teren.Ruch(self.speedX)
