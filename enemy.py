import pygame, random, decimal
import asset
from Postac import Postac
class Enemy(Postac):
    def __init__(self,wlasciwosci,pos,max_hp=30,mocStrzalu=10):
        self.pos = pygame.Vector2(pos)
        super().__init__(wlasciwosci[0])

        self.max_hp=max_hp
        self.hp=self.max_hp
        self.mnoznik=1.5

        self.orginalimgRight=[asset.imgWrogPrawo,self.mnoznik]
        self.imgRight=pygame.image.load(self.orginalimgRight[0]).convert_alpha()
        self.imgRight=pygame.transform.rotozoom(self.imgRight,0,self.orginalimgRight[1])

        self.orginalimgLeft=[asset.imgWrogLewo,self.mnoznik]
        self.imgLeft=pygame.image.load(self.orginalimgLeft[0]).convert_alpha()
        self.imgLeft=pygame.transform.rotozoom(self.imgLeft,0,self.orginalimgLeft[1])

        self.orginalRightReka = [asset.imgWrogRekaRight,self.mnoznik]
        self.RightReka=pygame.image.load(self.orginalRightReka[0]).convert_alpha()
        self.RightReka=pygame.transform.rotozoom(self.RightReka,0,self.orginalRightReka[1])

        self.orginalLeftReka = [asset.imgWrogRekaLeft, self.mnoznik]
        self.LeftReka = pygame.image.load(self.orginalLeftReka[0]).convert_alpha()
        self.LeftReka = pygame.transform.rotozoom(self.LeftReka, 0, self.orginalLeftReka[1])

        self.szerokosc=wlasciwosci[2]*1.5
        self.img = self.imgRight
        self.imgReka=self.RightReka

        self.orginalstrzala=[asset.imgStrzalaWrog,1]
        self.imgstrzala=pygame.image.load(self.orginalstrzala[0]).convert_alpha()
        self.imgstrzala=pygame.transform.rotozoom(self.imgstrzala,0,self.orginalstrzala[1])



        self.podazajzamysza = False
        self.numerElementu=3
        self.cooldown=1
        self.celStrzalu = "player"
        self.punktkierunkowyStrzlu=pygame.Vector2(self.main.Player.pos.x+self.main.Player.szerokosc/2,self.main.Player.pos.y+self.main.Player.szerokosc/2)
        self.PasekZdrowia = pygame.Rect(self.pos.x,self.pos.y,self.szerokosc,5)
        self.hpdododania=0

        #self.orginalshootsound = [asset.soundWrogStrzal,0.1]
        #self.shootsound = pygame.mixer.Sound(self.orginalshootsound[0])
        self.shootsound = self.main.relugacjaDzwiekow.evilshootsound
        #self.shootsound.set_volume(self.orginalshootsound[1])


        self.jumpSound = self.main.relugacjaDzwiekow.soundJump

        self.mocStrzalu = mocStrzalu
        self.wysSkoku = 150
        self.speedGravitation = 0.005
        self.speedJump = -0.8


        self.wlasciwosciDozmiany = [["powiekszenie", "Max_hp", self.max_hp, 1],["powiekszenie", "Siła ataku", self.mocStrzalu, 1]]
        self.speed.x=0.5
        self.CzyMozeSpascPonizej600 = False
        self.czydzialaAi=True
        self.czywyswietlaccPasekZrowia=True

        #animacja
        self.predkoscAnimacji =0.05
        self.klatkiWPrawoOrginal = [asset.imgEnemyRight1,asset.imgEnemyRight2,asset.imgEnemyRight3,asset.imgEnemyRight4,asset.imgEnemyRight5,asset.imgEnemyRight6]
        self.klatkiWPrawo = [pygame.transform.rotozoom(pygame.image.load(x), 0, 1.5) for x in self.klatkiWPrawoOrginal]

        self.klatkiWLewoOrginal = [asset.imgEnemyLeft1,asset.imgEnemyLeft2,asset.imgEnemyLeft3,asset.imgEnemyLeft4,asset.imgEnemyLeft5,asset.imgEnemyLeft6]
        self.klatkiWLewo = [pygame.transform.rotozoom(pygame.image.load(x), 0, 1.5) for x in self.klatkiWLewoOrginal]
    def __str__(self):
        return ("|" + str(self.numerElementu) + ",(" + str(self.pos.x) + ";" + str(self.pos.y) + ")" + "%")
    def wys(self):
        if self.main.CzyKreatorOtworzony==False:
            self.main.screen.blit(self.img,self.pos)

            self.wys2()

            self.AnimacjaPaska()
            if self.hp - self.hpdododania>0 and self.main.StartMenuOtworzone==False and self.czywyswietlaccPasekZrowia:
                pygame.draw.rect(self.main.screen,(0,255,0),self.PasekZdrowia)
            elif self.main.StartMenuOtworzone==False and self.czywyswietlaccPasekZrowia:
                self.Smierc()
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
    def wys2(self):
        if self.czyWyswietlac:
            #for i in range(self.Zegar()):
            self.Physik()
            self.Ruch()
            if self.czasUplyniety < self.cooldown:
                self.czasUplyniety += self.cooldownZegar.tick() / 1000
                self.strzel = False
            else:
                self.cooldownZegar.tick()
                if self.strzel:
                    self.strzel = False
                    self.czasUplyniety = 0
                    self.Strzał()
                    self.shootsound.play()
            #self.Ruch()

    def Ruch(self):
        super().Ruch()
        if self.main.StartMenuOtworzone==False and self.czydzialaAi:
            self.AI()
    def AI(self):
        self.LewoBlokada=False
        self.PrawoBlokada=False
        if self.main.IsCollision(self.pos,self.main.Player.pos,800):
            self.strzel=True
            if self.pos.x-self.main.Player.pos.x>10 and self.ruch=="prawo":
                self.ZmianaWLewo()
            elif self.pos.x-self.main.Player.pos.x<-10 and self.ruch=="lewo":
                self.ZmianaWprawo()
            if self.main.IsCollision(self.pos,self.main.Player.pos,200)==False:
                    if self.ruch=="prawo" and self.pos.x!=self.main.Player.pos.x:
                        self.animacja=True
                        self.Przemieszczenie(self.speed.x)
                    elif self.ruch=="lewo"and self.pos.x!=self.main.Player.pos.x:
                        self.animacja = True
                        self.Przemieszczenie(-self.speed.x)
            else:
                self.animacja=False
    def Przemieszczenie(self,speed):
        if self.main.Teren.CollisionNextTo("right", self.szerokosc, self.pos, self)==None and self.ruch=="lewo" and self.LewoBlokada==False:
            self.pos.x+=speed
        elif self.main.Teren.CollisionNextTo("left", self.szerokosc, self.pos, self)==None and self.ruch=="prawo" and self.PrawoBlokada==False:
            self.pos.x += speed
        elif self.state==0 and self.ruch=="lewo" and self.LewoBlokada==False or self.state==0 and self.ruch=="prawo" and self.PrawoBlokada==False:
            self.skocz=True
    # funkcje do poprawnego wyświetlania
    def checkIsItToWys(self):
        #return True
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
        if 0 <= self.speedAnimacji < 20:
            self.speedAnimacji = 20


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
    def PrzygotujDoZapisu(self):
        self.img=None
        self.imgReka=None
        self.imgstrzala=None
        self.imgRight=None
        self.imgLeft=None
        self.RightReka=None
        self.LeftReka=None
        self.clock=None
        self.shootsound=None
        self.jumpSound=None
        self.cooldownZegar=None
        self.klatkiWPrawo=None
        self.klatkiWLewo=None
        self.zegarAnimacji=None
        # bez zapisu
        self.font = None
        self.napis = None
    def PoWczytaniu(self):
        self.orginalstrzala[0]=asset.imgStrzalaWrog
        self.orginalimgRight[0]=asset.imgWrogRekaLeft
        self.orginalRightReka[0]=asset.imgWrogRekaRight

        self.imgstrzala = pygame.image.load(self.orginalstrzala[0])
        self.imgstrzala = pygame.transform.rotozoom(self.imgstrzala, 0, self.orginalstrzala[1])

        self.imgRight=pygame.image.load(self.orginalimgRight[0])
        self.imgRight = pygame.transform.rotozoom(self.imgRight,0,self.orginalimgRight[1])
        #self.imgLeft=pygame.image.load(self.org)
        self.RightReka = pygame.image.load(self.orginalRightReka[0])
        self.RightReka = pygame.transform.rotozoom(self.RightReka, 0, self.orginalimgRight[1])
        #self.LeftReka=listadoprzywrocenia[6]
        self.clock=pygame.time.Clock()
        self.shootsound = self.main.relugacjaDzwiekow.evilshootsound
        self.jumpSound = self.main.relugacjaDzwiekow.soundJump

        self.cooldownZegar=pygame.time.Clock()

        self.zegarAnimacji=pygame.time.Clock()

        self.main.Teren.enemy.append(self)

        self.img = self.imgRight
        self.imgReka = self.RightReka
        self.__init__([self.main, self.orginalimgRight, self.szerokosc/1.5, self.szerokosc/1.5], self.pos, self.max_hp, self.mocStrzalu)
    def PrzyjmijWlasciwosci(self, wlasciwosci):
        self.max_hp = wlasciwosci[0]
        self.mocStrzalu = wlasciwosci[1]
        self.hp = self.max_hp
        self.wlasciwosciDozmiany = [["powiekszenie", "Max_hp", self.max_hp, 1],["powiekszenie", "Siła ataku", self.mocStrzalu, 1]]
    def __bool__(self):
        return False