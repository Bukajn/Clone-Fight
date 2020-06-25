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
    def UstawWlasciwosc(self):
        self.obiektyDoKontrolowania = []
        for i in self.main.Teren.pods:
            try:
                if i:
                    self.obiektyDoKontrolowania.append(i)
            except:
                pass
    def DodajdoTeren(self):
        self.main.Teren.pods.append(self)
        self.Zmienpolozenie(-self.przesuniecie)
        self.UstawWlasciwosci()
    def Przesuniecie(self):
        self.przesuniecie = self.main.Teren.przesuniecie
    def main_loop(self):
        self.DodajdoTeren()
        while True:
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
    def ZwiekszEtap(self):
        self.etap+=1
    def ZwiekszEtapzResetem(self):
        self.ZwiekszEtap()
        self.poleDialogowe=None
class PrzedmiotInteraktywny():
    def __init__(self,main,img,imgO,img2,imgO2,pos,akcja1=None,akcja2=None,sound1=None,sound2=None):
        self.main = main
        self.img=pygame.image.load(img)
        self.imgO = pygame.image.load(imgO)
        self.img2 = pygame.image.load(img2)
        self.imgO2=pygame.image.load(imgO2)
        self.pos=pygame.Vector2(pos)
        self.akcja1 =akcja1
        self.akcja2 = akcja2
        try:
            self.sound1 = pygame.mixer.Sound(sound1)
            self.sound2 = pygame.mixer.Sound(sound2)
        except:
            pass
        rect = self.img.get_rect()
        self.Rozmiar = pygame.Vector2(rect[2],rect[3])
        self.stan1=True

        self.wczesniejszyKlik=pygame.key.get_pressed()
    def wys(self):
        if self.stan1:
            self.main.screen.blit(self.img,self.pos)
        else:
            self.main.screen.blit(self.img2, self.pos)
        self.CzyNajechany()
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
                   if self.stan1:
                        self.stan1=False
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
                        self.stan1=True
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
                self.wczesniejszyKlik = pygame.key.get_pressed()
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
        self.napis = self.font.render("", True, (0, 0, 0))
        self.napis2 = self.font.render("", True, (0, 0, 0))
        self.clock = pygame.time.Clock()
        self.czasMiniety=0
        self.cooldown=0.05 #0.05
        self.dlugoscWyswietlanegoTestu = 0
        self.aktualnalinijka=1
        self.NapisSkip = self.font.render("Q --->", True, (0, 0, 0))
        self.CzywyswietlacSkip=False
    def wys(self):
        self.NapisPoKolei()
        self.main.screen.blit(self.img, self.pos)
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
                    self.tekstdowyswietlenia = self.tekst[self.koniec1linijki:self.dlugoscWyswietlanegoTestu-self.koniec1linijki]
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

