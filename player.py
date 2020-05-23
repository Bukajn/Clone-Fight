import pygame

class Player(object):
    def __init__(self,main):
        self.main = main
        self.img = pygame.image.load("assets/original.png")
        self.pos = pygame.Vector2(300,0)
    def wys(self):
        self.Physik()
        self.main.screen.blit(self.img, self.pos)
    def Physik(self):
        self.height=self.main.Teren.ColisionWithFloar()
        if self.height != None:
            if self.pos.y < self.height:
                self.pos.y += 5
            if self.pos.y > self.height:
                self.pos.y= self.height