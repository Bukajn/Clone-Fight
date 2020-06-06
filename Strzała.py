import pygame
import asset
class Strzała(object):
    def __init__(self,main,pos):
        self.main = main
        self.pos = pos
    def wys(self):
        self.main.screen.blit(self,asset.imgManaCoin,self.pos)