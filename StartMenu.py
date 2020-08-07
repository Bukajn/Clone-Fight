import pygame, sys, asset
from button import Przycisk
from scene import Scene
from  PlanszUstawien import PlanszUstawien
from OpisPoziomu import OpisPoziomu
class StartMenu():
    def __init__(self,main,mapa):

        self.main = main
        self.mapa = mapa

        self.main.Player.pos.y = 2000
        self.speed=1
        self.clock=pygame.time.Clock()
        self.delta=0.0
        self.max_tps=60
        self.main.StartMenuOtworzone=True
        self.tytul = pygame.image.load(asset.imgTytul)
        self.PrzyciskStart=Przycisk(self.main,"         Start",(200,30),(301,250),(255,255,255),30,self.Start,False,(153,0,153),(153, 51, 153))
        self.PrzyciskEdytor = Przycisk(self.main, "         Edytor", (200, 30), (294, 320), (255, 255, 255), 30,self.Edytor, False, (153, 0, 153), (153, 51, 153))
        self.PrzyciskUstawienia = Przycisk(self.main, "     Ustawienia", (200, 30), (294, 285), (255, 255, 255), 30,
                                       self.Ustawienia, False, (153, 0, 153), (153, 51, 153))
        self.PrzyciskPowrot = Przycisk(self.main, "Powrót", (100, 20), (0, 0), (153, 0, 153), 20,self.Powrot, True, (0, 0, 0), (153, 51, 153))
        self.PrzyciskNowaMapa = Przycisk(self.main, "Nowa mapa", (110, 20), (690, 580), (128, 128, 128), 20,self.OtworzPustyEdytor, True, (0, 0, 0), (100, 100, 100))
        self.GornyPasek = pygame.Rect(0,0,800,20)
        self.stan =0

        self.PoleUstawienia = PlanszUstawien(self.main,(0,20))

        self.UtworzMapyDowyboru()
        self.UtworzMapyDowyboru2()

    def main_loop(self):
        self.main.aktualnyPoziom=None
        self.main.StartMenuOtworzone = True
        self.main.Player.pos.y = 2000
        self.main.create_maps.OknoWyboru.Wczytaj(self.mapa)
        self.running = True
        while self.running:
            for i in range(self.Zegar()):
                self.main.screen.fill((100, 150, 255))
                self.check_events()
                self.main.Teren.wys()
                self.main.Teren.Ruch(self.speed)
                if self.stan==0:
                    self.main.screen.blit(self.tytul,pygame.Vector2(20,10))
                    self.PrzyciskStart.Wys()
                    self.PrzyciskUstawienia.Wys()
                    self.PrzyciskEdytor.Wys()#Przcisk do edytora wyswietlany
                elif self.stan==1:
                    pygame.draw.rect(self.main.screen, (153, 0, 153), self.GornyPasek)
                    self.PrzyciskPowrot.Wys()
                    for i in self.Elementy2:
                        i.wys()
                elif self.stan==2:
                    pygame.draw.rect(self.main.screen, (153, 0, 153), self.GornyPasek)
                    self.PrzyciskPowrot.Wys()
                    for i in self.Elementy:
                        i.wys()
                    self.PrzyciskNowaMapa.Wys()
                elif self.stan==3:
                    pygame.draw.rect(self.main.screen, (153, 0, 153), self.GornyPasek)
                    self.PrzyciskPowrot.Wys()
                    self.PoleUstawienia.wys()
                #pygame.draw.line(self.main.screen, (50, 50, 50), pygame.Vector2(400, 0), pygame.Vector2(400, 600))
                pygame.display.update()
                if len(self.main.Teren.towys)<=1:
                    self.main.create_maps.OknoWyboru.Wczytaj(self.mapa)
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.Powrot()
    def Zegar(self):
        self.delta += self.clock.tick() / 1000.0
        i = 0
        while self.delta > 1 / self.max_tps:
            i += 1
            self.delta -= 1 / self.max_tps
        return i
    def Start(self):
        self.stan=1
    def Powrot(self):
        self.stan=0
    def Edytor(self):
        self.stan=2
    def Ustawienia(self):
        self.stan=3
    def UtworzMapyDowyboru(self):
        self.Elementy =[]
        y=30
        for i in range(len(self.main.mapy)):
            self.Elementy.append(WyborMapa(self.main,self,(0,y),self.main.mapy[i]))
            y+=25

    def UtworzMapyDowyboru2(self):
        self.Elementy2 = []
        y = 30
        for i in range(len(self.main.poziomy)):
            self.Elementy2.append(WyborMapa(self.main, self, (0, y), self.main.poziomy[i]))
            y += 25
    def OtworzPustyEdytor(self):
        nazwanowejmapy=input("Podaj nazwe nowej mapy:")
        self.main.StartMenuOtworzone=False
        self.main.create_maps.WczytajMape(nazwanowejmapy,True)
        self.main.create_maps.main_loop()
    def OtworzScene(self,mapa):
        self.main.StartMenuOtworzone = False
        self.main.scena.WczytajMape(mapa)
        self.main.scena.main_loop()
    def OtworzScene2(self,poziom):
        self.main.StartMenuOtworzone = False
        poziom = poziom(self.main)
        self.main.aktualnyPoziom=poziom
        poziom.main_loop()
        self.running=False
    def OtworzEdytor(self,mapa):
        self.main.StartMenuOtworzone=False
        self.main.create_maps.WczytajMape(mapa)
        self.main.create_maps.main_loop()
class WyborMapa():
    def __init__(self,main,menu,pos,nazwamapy,argumenty=None):
        self.main = main
        self.menu=menu
        self.pos=pygame.Vector2(pos)
        self.nazwamapy = nazwamapy
        self.opisPoziomu = OpisPoziomu(self.main)
        if type(self.nazwamapy)!= str:
            self.poziom=self.nazwamapy
            self.nazwamapy=str(self.poziom(self.main))

        self.pole = Przycisk(self.main,self.nazwamapy,(400,20),(self.pos.x,self.pos.y),(128,128,128),20,self.JestWybrany,True,(0,0,0),(100,100,100))
    def wys(self):
        self.pole.Wys()
        self.opisPoziomu.wys()
        if self.pole.najechany ==True and self.menu.stan ==1: #
            self.JestNajechany()
        elif self.menu.stan==1 and self.opisPoziomu.otworzony ==True:
            self.opisPoziomu.ZaczecieZamykania()
    def JestWybrany(self):
        if self.menu.stan==1:
            self.menu.OtworzScene2(self.poziom)
        elif self.menu.stan==2:
            self.menu.OtworzEdytor(self.nazwamapy)
    def JestNajechany(self):
        if self.opisPoziomu.otworzony==False:
            self.opisPoziomu.ZaczecieOtwierania()


