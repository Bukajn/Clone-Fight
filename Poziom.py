import pygame, asset
from scene import Scene
class Poziom():
    def __init__(self,main,mapa,styl):
        self.main =main
        self.scena = Scene(self.main,"",styl,self)
        self.scena.WczytajMape(mapa)
        self.obiektyDoKontrolowania=[]
        self.przesuniecie=0
        self.poleDialogowe = None
        self.etap = 0
        self.tlo = None
        self.nazwa=None
        self.running=True
    def UstawWlasciwosci(self):
        self.obiektyDoKontrolowania = []
        for i in self.main.Teren.pods:
            try:
                if i:
                    self.obiektyDoKontrolowania.append(i)
            except:
                pass
    def __str__(self):
        return self.nazwa
    def DodajdoTeren(self):
        self.main.Teren.pods.append(self)
        self.Zmienpolozenie(-self.przesuniecie)
        self.UstawWlasciwosci()
    def Przesuniecie(self):
        self.przesuniecie = self.main.Teren.przesuniecie
    def main_loop(self):
        self.DodajdoTeren()
        while self.running:

            self.scena.main_loop()
            self.Fabula()
    def checkIsItToWys(self):
        return True
    def Zmienpolozenie(self,speed):
        for i in range(len(self.obiekty)):
            if type(self.obiekty[i]) == list:

                self.obiekty[i][0] = self.obiekty[i][0].move(speed,0)
            else:
                self.obiekty[i].Przesun(speed)
        if self.tlo!=None:
            self.tlo.Przesun(speed)
    def ZwiekszEtap(self):
        self.etap+=1

    def ZwiekszEtapLess(self):
        self.etap += 0.1
    def ZwiekszEtapzResetem(self):
        self.ZwiekszEtap()
        self.poleDialogowe=None
class PrzedmiotInteraktywny():
    def __init__(self,main,img,imgO,img2,imgO2,pos,akcja1=None,akcja2=None,sound1=None,sound2=None,odleglosc=999,czyaktywny=True,CzywykonacReset=False,):
        self.main = main
        self.img=pygame.image.load(img)
        self.imgO = pygame.image.load(imgO)
        self.img2 = pygame.image.load(img2)
        self.imgO2=pygame.image.load(imgO2)
        self.pos=pygame.Vector2(pos)
        self.odleglosc= odleglosc
        self.akcja1 =akcja1
        self.akcja2 = akcja2
        self.czyWykonacReset = CzywykonacReset
        self.Czywyswietla=True
        try:
            self.sound1 = pygame.mixer.Sound(sound1)
            self.sound1.set_volume(self.main.relugacjaDzwiekow.glownaGlosnosc)
            self.sound2 = pygame.mixer.Sound(sound2)
            self.sound2.set_volume(self.main.relugacjaDzwiekow.glownaGlosnosc)
        except:
            pass
        self.czyAktywny = czyaktywny
        rect = self.img.get_rect()
        self.Rozmiar = pygame.Vector2(rect[2],rect[3])
        self.stan1=True

        self.wczesniejszyKlik=pygame.key.get_pressed()
    def wys(self):
        if self.Czywyswietla:
            if self.stan1:
                self.main.screen.blit(self.img,self.pos)
            else:
                self.main.screen.blit(self.img2, self.pos)
            if self.main.IsCollision(self.pos,self.main.Player.pos,self.odleglosc) and self.czyAktywny:
                self.CzyNajechany()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r] and self.czyAktywny:
                if self.stan1:
                    self.main.screen.blit(self.imgO, self.pos)
                else:
                    self.main.screen.blit(self.imgO2, self.pos)
    def Przesun(self,droga):
        self.pos.x+=droga
    def CzyNajechany(self):
        mousePos = pygame.mouse.get_pos()
        if mousePos[0] > self.pos.x and mousePos[0] < self.pos.x + self.Rozmiar.x:
            if mousePos[1] > self.pos.y and mousePos[1] < self.pos.y + self.Rozmiar.y:
                if self.stan1:
                    self.main.screen.blit(self.imgO,self.pos)

                else:
                    self.main.screen.blit(self.imgO2, self.pos)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_e] and keys[pygame.K_e]!=self.wczesniejszyKlik[pygame.K_e]:
                   self.Zmiana()
                self.wczesniejszyKlik = pygame.key.get_pressed()
    def Zmiana(self):
        if self.stan1:
            self.stan1 = False
            rect = self.img2.get_rect()
            self.Rozmiar = pygame.Vector2(rect[2], rect[3])
            try:
                self.akcja1()
            except:
                pass
            try:
                self.sound1.play()
            except:
                pass

        else:
            self.stan1 = True
            rect = self.img.get_rect()
            self.Rozmiar = pygame.Vector2(rect[2], rect[3])
            try:
                self.akcja2()
            except:
                pass
            try:
                self.sound2.play()
            except:
                pass
    def reset(self,stan1):
        if self.czyWykonacReset:

            if stan1:
                self.stan1 = True
                self.akcja2()


            else:
                self.stan1 = False
                self.akcja1()

    def aktualnyStan(self):
        return self.stan1
class PoleDialogowe():
    def __init__(self,main,pos,nadawca,tekst,iloscznakow1=999,akcjaKoncowa=None,czySkipAktywny=None):
        self.main = main
        self.pos = pygame.Vector2(pos)
        self.nadawca=nadawca
        self.tekst = tekst
        self.koniec1linijki = iloscznakow1
        self.akcjaKoncowa = akcjaKoncowa
        self.czySkipAktywny = czySkipAktywny

        self.img=pygame.image.load(asset.imgPoleDialogowe)
        self.font = pygame.font.Font(asset.czcionkaRoboto, 20)
        self.font2 = pygame.font.Font(asset.czcionkaRoboto, 15)
        self.napis = self.font.render("", True, (0, 0, 0))
        self.napis2 = self.font.render("", True, (0, 0, 0))
        self.napisNadawca = self.font2.render(nadawca,True,(0,0,0))
        self.clock = pygame.time.Clock()
        self.czasMiniety=0
        self.cooldown=0.001 #0.05
        self.dlugoscWyswietlanegoTestu = 0
        self.aktualnalinijka=1
        self.NapisSkip = self.font.render("Q --->", True, (0, 0, 0))
        self.CzywyswietlacSkip=False
    def wys(self):
        self.NapisPoKolei()
        self.main.screen.blit(self.img, self.pos)
        self.main.screen.blit(self.napisNadawca, self.pos + pygame.Vector2(25, 10))
        self.main.screen.blit(self.napis,self.pos+pygame.Vector2(20,25))
        self.main.screen.blit(self.napis2, self.pos + pygame.Vector2(20, 50))

        if self.CzywyswietlacSkip:
            self.main.screen.blit(self.NapisSkip, self.pos + pygame.Vector2(700, 70))
    def NapisPoKolei(self):

        if self.dlugoscWyswietlanegoTestu < len(self.tekst):
            self.czasMiniety+=self.clock.tick()/1000
            if self.czasMiniety>self.cooldown:
                if self.aktualnalinijka ==1:
                    self.dlugoscWyswietlanegoTestu+=1
                    self.tekstdowyswietlenia = self.tekst[0:self.dlugoscWyswietlanegoTestu]
                    self.napis = self.font.render(self.tekstdowyswietlenia, True, (0, 0, 0))
                    self.czasMiniety=0
                    if self.dlugoscWyswietlanegoTestu== self.koniec1linijki:
                        self.aktualnalinijka=2
                elif self.aktualnalinijka==2:
                    self.dlugoscWyswietlanegoTestu += 1
                    self.tekstdowyswietlenia = self.tekst[self.koniec1linijki:self.dlugoscWyswietlanegoTestu]
                    self.napis2 = self.font.render(self.tekstdowyswietlenia, True, (0, 0, 0))
                    self.czasMiniety = 0
        else:
            if self.czySkipAktywny == False and self.akcjaKoncowa!=None:
                self.akcjaKoncowa()
                self.akcjaKoncowa=None
            elif self.czySkipAktywny and self.akcjaKoncowa!=None:
                self.CzywyswietlacSkip=True
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                    self.akcjaKoncowa()
                    self.akcjaKoncowa = None
class Cel():
    def __init__(self,main):
        self.main = main
        self.pos =pygame.Vector2(0,-100)
        self.font = pygame.font.Font(asset.czcionkaRoboto, 15)
        self.napis = self.font.render("", True, (0, 0, 0))
        self.rect = self.napis.get_rect()
        self.zegar = pygame.time.Clock()
        self.orginalnapozycjaX=None
        self.CzasMiniety=0
        self.cooldown=3
    def UstawNowyCel(self,pos,text):
        self.pos = pygame.Vector2(pos)
        self.orginalnapozycjaX = self.pos.x
        self.napis = self.font.render(text, True, (0, 0, 0))
        self.rect = self.napis.get_rect()

        self.CzasMiniety=0
        self.zegar.tick()
    def wys(self):
        if self.orginalnapozycjaX!=None:
            if self.orginalnapozycjaX>780:
                self.pos.x=780
            else:
                self.pos.x =self.orginalnapozycjaX
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r] or self.CzasMiniety<self.cooldown:
            pygame.draw.circle(self.main.screen,(225, 255, 0),(int(self.pos.x),int(self.pos.y)),10)
            pygame.draw.circle(self.main.screen, (225, 0, 0), (int(self.pos.x), int(self.pos.y)), 5)
            pygame.draw.rect(self.main.screen,(255,0,0),pygame.Rect(self.pos.x-(self.rect[2]+13),self.pos.y-10,self.rect[2]+2,20))
            self.main.screen.blit(self.napis,self.pos-pygame.Vector2(self.rect[2]+12,10))
            if self.CzasMiniety<self.cooldown:
                self.CzasMiniety += self.zegar.tick()/1000
    def Przesun(self, droga):
        self.pos.x += droga
        if self.orginalnapozycjaX!=None:
            self.orginalnapozycjaX+=droga
class Tlo():
    def __init__(self,main,img):
        self.main = main
        self.img = pygame.image.load(img).convert_alpha()
        self.pos= pygame.Vector2(7,0)
    def wys(self):
        self.main.screen.blit(self.img,self.pos)
    def Przesun(self,droga):
        if droga != 0:
            self.pos.x+=droga
    def checkIsItToWys(self):
        return True
class Checkpoint():
    def __init__(self,main,poziom):
        self.main = main
        self.poziom = poziom

        self.czyWyswietlac=False
        self.zegar = pygame.time.Clock()
        self.CzasMiniety = 0
        self.Stany=[]
    def UstawCheckPoint(self,etap):

        self.czyWyswietlac = True
        self.zegar.tick()
        self.CzasMiniety = 0

        self.etap = etap
        self.przesuniecie = self.main.Teren.przesuniecie
        self.posPlayerY=self.main.Player.pos.y

        self.hpPlayer=self.main.Player.hp
        self.manaPlayer= self.main.GUI.mana
        self.main.create_maps.OknoWyboru.Zapisz("CheckPoint")
        self.Stany = []
        for i in self.poziom.obiekty:
            try:
                self.Stany.append(i.aktualnyStan())
            except:
                self.Stany.append(None)
        self.CofnijDoCheckPointa()
    def CofnijDoCheckPointa(self):
        a = -(self.main.Teren.przesuniecie-self.przesuniecie)
        if a ==0:
            self.main.Teren.Ruch(a)
        else:
            self.main.Teren.Ruch(-(self.main.Teren.przesuniecie))

        self.main.aktualnyPoziom.scena.WczytajMape("CheckPoint")
        self.main.Teren.pods.append(self.poziom)
        self.main.aktualnyPoziom.UstawWlasciwosci()
        self.main.Player.pos.y = self.posPlayerY
        self.main.Player.hp = self.hpPlayer
        self.main.GUI.mana = self.manaPlayer
        for i in range(len(self.poziom.obiekty)):
            try:
                self.poziom.obiekty[i].reset(self.Stany[i])
            except:
                pass
        self.poziom.etap=self.etap

    def wys(self):

        if self.czyWyswietlac:
            pygame.draw.rect(self.main.screen,(255,255,0),pygame.Rect(0,0,800,600))
            self.CzasMiniety+=self.zegar.tick()/1000
            if self.CzasMiniety>1:
                self.czyWyswietlac=False
    def Przesun(self,x):
        pass