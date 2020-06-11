import pygame

class PasekZdrowia():
    def __init__(self,main,GUI):
        self.main=main
        self.GUI=GUI
        self.pos=pygame.Vector2(self.GUI.pos.x+10,self.GUI.pos.y+10)
        self.krawedzie=self.krawedzie = pygame.Rect(self.pos.x,self.pos.y,250,30)
    def wys(self):
        pygame.draw.rect(self.main.screen, (0, 0, 0), self.krawedzie)