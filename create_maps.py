import pygame
from okno_wyboru import OknoWyboru
class Create_maps(object):
    def __init__(self,main):
        self.main=main
        self.font=pygame.font.Font("freesansbold.ttf",32)
        self.napis= self.font.render("Tworzenie mapy",True,(0,0,0))
        self.stan = "pojedynczy"
        self.informacja = self.font.render(self.stan,True,(0,0,0))
        self.obiekt=None
        self.OknoWyboru=OknoWyboru(self.main)
    def main_loop(self):
        self.running = True
        self.obiektyKlikniete = []
        self.otwarteOknoWyboru = False
        while self.running:
            self.main.screen.fill((100, 150, 255))
            self.check_events()
            self.main.Teren.wys()
            self.main.Player.wys()
            self.main.screen.blit(self.napis,(0,0))
            self.main.screen.blit(self.informacja, (500, 0))

            if self.otwarteOknoWyboru:
                self.OknoWyboru.wys()
            else:
                self.Poruszanie()
            pygame.display.update()
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.main.Player.pos.y = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_COMMA:
                if self.stan == "pojedynczy":
                    self.stan = "ciagly"
                else:
                    self.stan = "pojedynczy"
                self.informacja = self.font.render(self.stan, True, (0, 0, 0))
        if pygame.mouse.get_pressed()[2]:
            self.otwarteOknoWyboru=True
    def Poruszanie(self):
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