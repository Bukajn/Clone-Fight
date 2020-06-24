import pygame
from okno_wyboru import OknoWyboru
import asset
import sys
from OknoZmianyWlasciwosci import Okno
from OknoPodwojnegoWyboru import OknoPodwojnegoWyboru
class Create_maps(object):
    def __init__(self,main):
        self.main=main
        self.mapa=None
        self.font=pygame.font.Font(asset.czcionkaRoboto,32)
        self.napis= self.font.render("Tworzenie mapy",True,(0,0,0))
        self.stan = "pojedynczy"
        self.informacja = self.font.render(self.stan,True,(0,0,0))
        self.obiekt=None
        self.CzyNapisyWlaczone=False
        self.OknoWyboru=OknoWyboru(self.main)
        self.oknowlasciwosci=None
        self.oknowyboru=None
    def WczytajMape(self,mapa,czytworzonajestnowamapa=False):
        self.mapa = mapa
        self.OknoWyboru.Wczytaj(self.mapa,czytworzonajestnowamapa)
    def main_loop(self):
        self.main.CzyKreatorOtworzony = True
        self.running = True
        self.obiektyKlikniete = []
        self.otwarteOknoWyboru = False
        self.main.Player.pos.y = 0

        while self.running:
            self.main.screen.fill((100, 150, 255))
            self.check_events()
            self.main.Teren.wys()
            self.main.Player.wys()
            self.main.GUI.wys()
            self.main.screen.blit(self.napis,(0,0))
            self.main.screen.blit(self.informacja, (500, 0))
            if self.otwarteOknoWyboru:
                self.OknoWyboru.wys()
            else:
                self.Poruszanie()
                self.oknowlasciwosciZarzadzanie()
            if self.oknowyboru != None:
                self.main.StartMenuOtworzone = True
                self.oknowyboru.wys()
            else:
                self.main.StartMenuOtworzone = False
            pygame.display.update()
        self.main.CzyKreatorOtworzony = False
    def oknowlasciwosciZarzadzanie(self):
        if self.oknowlasciwosci ==None and self.obiekt != None or self.oknowlasciwosci !=None and self.obiekt != None and self.oknowlasciwosci.obiekt != self.obiekt:
            self.oknowlasciwosci = Okno(self.main,self.obiekt)
        if self.oknowlasciwosci != None:
            self.oknowlasciwosci.wys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.main.Player.pos.y = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_COMMA:
                if self.stan == "pojedynczy":
                    self.stan = "ciagly"
                else:
                    self.stan = "pojedynczy"
                self.informacja = self.font.render(self.stan, True, (0, 0, 0))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                if self.CzyNapisyWlaczone ==True:
                    self.CzyNapisyWlaczone=False
                else:
                    self.CzyNapisyWlaczone=True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_MINUS:
                self.main.GUI.pasekMany.DodawajMane(-100)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_PLUS:
                self.main.GUI.pasekMany.DodawajMane(100)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:

                self.OknoWyboru.Wczytaj(self.mapa)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                self.main.scenaTestowa.main_loop()
                self.main.CzyKreatorOtworzony = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.oknowyboru = OknoPodwojnegoWyboru(self.main, "                Czy napewno chcesz wyjść?",
                                                       self.ZamknijOknoWyboru, self.ZamknijScene, "    Tak", "    Nie")
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                self.main.Teren.Ruch(-self.main.Teren.przesuniecie)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                self.main.Player.pos.y=800
        if pygame.mouse.get_pressed()[2]:
            self.otwarteOknoWyboru=True
    def ZamknijOknoWyboru(self):
        self.oknowyboru=None
    def ZamknijScene(self):
        self.oknowyboru = None
        self.main.CzyKreatorOtworzony=False
        self.main.StartScena.main_loop()
    def Poruszanie(self):
        if self.CzyNapisyWlaczone:
            for i in self.main.Teren.towys:
                i.WysNapis((0, 0, 0))
        if self.oknowlasciwosci!=None and self.oknowlasciwosci.Czynajechany()==False or self.oknowlasciwosci==None:
            if pygame.mouse.get_pressed()[0]:
                self.obiektyKlikniete = []
                for i in self.main.Teren.towys:
                    try:
                        if i.CzyKlikniety() != None:
                            self.obiekt = i.CzyKlikniety()
                            self.obiektyKlikniete.append(self.obiekt)
                    except:
                        pass
            if self.obiektyKlikniete == []:
                self.obiekt = None

        if self.obiekt != None:
            self.obiekt.WysNapis((255, 0, 0))
            self.obiekt.Zmianapolozenia(self.stan)
