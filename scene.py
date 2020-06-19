import pygame, sys
from OknoPodwojnegoWyboru import OknoPodwojnegoWyboru
class Scene(object):
    def __init__(self,main,mapa):
        self.main = main
        self.mapa=mapa
        self.oknowyboru=None
    def WczytajMape(self,mapa):
        self.mapa=mapa
        self.main.create_maps.OknoWyboru.Wczytaj(self.mapa)
        self.main.Player.pos.y = 0
    def main_loop(self):
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
            pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.oknowyboru=OknoPodwojnegoWyboru(self.main,"                Czy napewno chcesz wyjść?",self.ZamknijOknoWyboru,self.ZamknijScene)
    def ZamknijOknoWyboru(self):
        self.oknowyboru=None
    def ZamknijScene(self):
        self.oknowyboru = None
        self.main.StartScena.main_loop()



