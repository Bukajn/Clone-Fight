import pygame
from scene_test import Scene_test
from teren import Teren
from player import Player
class main(object):
    def __init__(self):
        pygame.init()
        self.set_window()
        self.max_tps = 60
        self.Teren = Teren(self)
        self.Player=Player(self)

        self.scene = Scene_test(self)
    def set_window(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Przez czas")


main()