import pygame, sys, asset
from button import Przycisk
class StartMenu():
    def __init__(self,main,mapa):

        self.main = main
        self.mapa = mapa
        self.main.create_maps.OknoWyboru.Wczytaj(self.mapa)
        self.main.Player.pos.y = 2000
        self.speed=1
        self.clock=pygame.time.Clock()
        self.delta=0.0
        self.max_tps=60
        self.main.StartMenuOtworzone=True
        self.tytul = pygame.image.load(asset.imgTytul)
        self.PrzyciskStart=Przycisk(self.main,"         Start",(200,30),(301,250),(255,255,255),30,self.Start,False,(153,0,153),(153, 51, 153))
        self.PrzyciskPowrot = Przycisk(self.main, "Powrót", (100, 20), (0, 0), (153, 0, 153), 20,self.Powrot, True, (0, 0, 0), (153, 51, 153))
        self.GornyPasek = pygame.Rect(0,0,800,20)
        self.stan =0
    def main_loop(self):
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
                elif self.stan==1:
                    pygame.draw.rect(self.main.screen, (153, 0, 153), self.GornyPasek)
                    self.PrzyciskPowrot.Wys()
                pygame.draw.line(self.main.screen, (50, 50, 50), pygame.Vector2(400, 0), pygame.Vector2(400, 600))
                pygame.display.update()
                if len(self.main.Teren.towys)<=1:
                    self.main.create_maps.OknoWyboru.Wczytaj(self.mapa)
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
                pygame.quit()
                sys.exit()
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