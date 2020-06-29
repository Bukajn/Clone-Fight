import pygame, sys
from OknoPodwojnegoWyboru import OknoPodwojnegoWyboru
class Scene(object):
    def __init__(self,main,mapa,styl,poziom=None):
        self.main = main
        self.styl = styl
        self.mapa=mapa
        self.oknowyboru=None
        self.oknoSmierci = OknoPodwojnegoWyboru(self.main,"                         Przegrałeś",self.ZamknijScene,self.Odrodz,"  Odródź","   Menu")
        self.poziom=poziom


        self.niesmiertelnosc=True

    def WczytajMape(self,mapa):
        self.mapa=mapa
        self.main.create_maps.OknoWyboru.Wczytaj(self.mapa)
        self.main.Teren.UstawMotyw(self.styl)
        self.main.Player.pos.y = 0
        self.main.Player.hp=self.main.Player.max_hp
        self.main.GUI.mana=0
    def main_loop(self):

        if self.poziom == None:
            self.main.StartMenuOtworzone = False
            self.running = True
            while self.running:
                self.main.screen.fill((100, 150, 255))
                self.check_events()
                self.main.Teren.wys()
                self.main.Player.wys()
                self.main.GUI.wys()
                if self.oknowyboru!=None:
                    self.main.StartMenuOtworzone=True
                    self.oknowyboru.wys()
                else:
                    self.main.StartMenuOtworzone = False
                if self.main.Player.hp-self.main.GUI.pasekZdrowia.hpdododania <=0 and self.niesmiertelnosc == False:
                    self.main.StartMenuOtworzone = True
                    self.oknoSmierci.wys()
                pygame.display.update()
        else:
            self.main.screen.fill((100, 150, 255))
            self.check_events()
            self.main.Teren.wys()
            self.main.Player.wys()
            self.main.GUI.wys()
            if self.oknowyboru != None:
                self.main.StartMenuOtworzone = True
                self.oknowyboru.wys()
            else:
                self.main.StartMenuOtworzone = False
            if self.main.Player.hp - self.main.GUI.pasekZdrowia.hpdododania <= 0 and self.niesmiertelnosc == False:
                self.main.StartMenuOtworzone = True
                self.oknoSmierci.wys()
            pygame.display.update()
    def Odrodz(self):
        self.poziom.Przesuniecie()
        self.WczytajMape(self.mapa)
        if self.poziom!=None:
           self.poziom.DodajdoTeren()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.oknowyboru=OknoPodwojnegoWyboru(self.main,"                Czy napewno chcesz wyjść?",self.ZamknijOknoWyboru,self.ZamknijScene,"    Tak","    Nie")
            #tymcasowe
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.main.Teren.Ruch(-800)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.main.Teren.Ruch(800)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                self.main.Player.pos.y = 0
    def ZamknijOknoWyboru(self):
        self.oknowyboru=None
    def ZamknijScene(self):
        self.oknowyboru = None
        self.main.StartScena.main_loop()



