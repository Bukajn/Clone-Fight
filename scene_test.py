import pygame


class Scene_test(object):
    def __init__(self,main):
        self.main = main

    def main_loop(self):
        self.main.CzyKreatorOtworzony=False
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
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.main.Player.pos.y = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                self.running=False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                print("debug")
