import pygame

class Paseknaladowania():
    def __init__(self,main,GUI,pos,cooldown):
        self.main=main
        self.GUI=GUI
        self.pos=pygame.Vector2(pos)
        self.krawedzie=pygame.Rect(self.pos.x,self.pos.y,200,10)
        self.tlo = pygame.Rect(self.pos.x+2,self.pos.y+2,196,6)
        self.naladowanie=pygame.Rect(self.pos.x+2,self.pos.y+2,196,6)
        self.dlugosc=0
        self.colour=(10, 50, 180)
        self.cooldown = cooldown
    def wys(self,czasuplyniety):
        pygame.draw.rect(self.main.screen,(0,0,0),self.krawedzie)
        pygame.draw.rect(self.main.screen, self.GUI.colour, self.tlo)
        pygame.draw.rect(self.main.screen, self.colour, self.naladowanie)

        self.dlugosc=(czasuplyniety/self.cooldown)*196

        if self.dlugosc<=196:
            self.colour = (0, 102, 204)
            self.naladowanie = pygame.Rect(self.pos.x + 2, self.pos.y + 2, self.dlugosc, 6)
        else:
            self.colour = (10, 50, 180)
            self.naladowanie = pygame.Rect(self.pos.x + 2, self.pos.y + 2, 196, 6)