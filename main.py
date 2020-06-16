import pygame, math, asset
from scene_test import Scene_test
from teren import Teren
from player import Player
from create_maps import Create_maps
from scene import Scene
import maps
from GUI import GUI
import pkg_resources.py2_warn

class main(object):
    def __init__(self):
        pygame.init()

        self.set_window()
        self.max_tps = 60
        self.Teren = Teren(self)
        self.Player=Player(self)
        self.GUI =GUI(self)
        self.CzyKreatorOtworzony = False
        #self.scena =  Scene_test(self)
        self.create_maps = Create_maps(self)
        #self.create_maps.main_loop()
        self.scena = Scene(self,"sekret")
        self.scena.main_loop()
    def set_window(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Przez czas")
    def IsCollision(self,pos1,pos2,wymaganaodleglosc):
        odleglosc = math.sqrt((math.pow(pos1.x-pos2.x,2)+math.pow(pos1.y-pos2.y,2)))
        if odleglosc <= wymaganaodleglosc:
            return True
        else:
            return False
main()