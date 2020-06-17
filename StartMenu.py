import pygame, sys

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
    def main_loop(self):
        self.running = True
        while self.running:
            for i in range(self.Zegar()):
                self.main.screen.fill((100, 150, 255))
                self.check_events()
                self.main.Teren.wys()
                self.main.Teren.Ruch(self.speed)
                pygame.display.update()
                if len(self.main.Teren.towys)<=1:
                    self.main.create_maps.OknoWyboru.Wczytaj(self.mapa)
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.main.Player.pos.y = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                self.main.create_maps.main_loop()
    def Zegar(self):
        self.delta += self.clock.tick() / 1000.0
        i = 0
        while self.delta > 1 / self.max_tps:
            i += 1
            self.delta -= 1 / self.max_tps
        return i