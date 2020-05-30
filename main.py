import pygame
from scene_test import Scene_test
from teren import Teren
from player import Player
from create_maps import Create_maps

class main(object):
    def __init__(self):
        pygame.init()
        self.set_window()
        self.max_tps = 60
        self.Teren = Teren(self)
        self.Player=Player(self)
        self.scene = Scene_test(self)
        self.create_maps=Create_maps(self)
        #self.scene.main_loop()
        self.create_maps.main_loop()
    def set_window(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Przez czas")


main()