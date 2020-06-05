import pygame
from okno_wyboru import OknoWyboru
import asset
import sys
class Create_maps(object):
    def __init__(self,main):
        self.main=main
        self.font=pygame.font.Font(asset.czcionkaRoboto,32)
        self.napis= self.font.render("Tworzenie mapy",True,(0,0,0))
        self.stan = "pojedynczy"
        self.informacja = self.font.render(self.stan,True,(0,0,0))
        self.obiekt=None
        self.CzyNapisyWlaczone=False
        self.OknoWyboru=OknoWyboru(self.main)
    def main_loop(self):
        self.main.CzyKreatorOtworzony = True
        self.running = True
        self.obiektyKlikniete = []
        self.otwarteOknoWyboru = False
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
            pygame.display.update()
        self.main.CzyKreatorOtworzony = False
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                self.running = False
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
                self.OknoWyboru.Wczytaj(self.main.scena.mapa)
        if pygame.mouse.get_pressed()[2]:
            self.otwarteOknoWyboru=True
    def Poruszanie(self):
        if self.CzyNapisyWlaczone:
            for i in self.main.Teren.towys:
                i.WysNapis((0, 0, 0))

        if pygame.mouse.get_pressed()[0]:
            self.obiektyKlikniete = []
            for i in self.main.Teren.towys:
                if i.CzyKlikniety() != None:
                    self.obiekt = i.CzyKlikniety()
                    self.obiektyKlikniete.append(self.obiekt)
        if self.obiektyKlikniete == []:
            self.obiekt = None

        if self.obiekt != None:
            self.obiekt.WysNapis((255, 0, 0))
            self.obiekt.Zmianapolozenia(self.stan)