import pygame

class Scene(object):
    def __init__(self,main,mapa):
        self.main = main
        self.mapa=mapa
        self.main.create_maps.OknoWyboru.Wczytaj(self.mapa)
    def main_loop(self):
        self.running = True
        while self.running:
            self.main.screen.fill((100, 150, 255))
            self.check_events()
            self.main.Teren.wys()
            self.main.Player.wys()
            self.main.GUI.wys()
            pygame.display.update()
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.main.Player.pos.y = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                self.main.create_maps.main_loop()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                self.main.create_maps.OknoWyboru.Wczytaj(self.mapa)