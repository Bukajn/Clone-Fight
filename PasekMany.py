import pygame
class PasekMany(object):
    def __init__(self,main,GUI):
        self.main = main
        self.GUI = GUI
        self.pos = pygame.Vector2(self.GUI.pos.x+500,self.GUI.pos.y+10)
        self.krawedzie = pygame.Rect(self.pos.x,self.pos.y,250,30)
        self.tlo = pygame.Rect(self.pos.x+5, self.pos.y+5, 240, 20)
        self.pasek = pygame.Rect(self.pos.x+5, self.pos.y+5, 0, 20)
        #self.pasekdododania = pygame.Rect(self.pos.x+5, self.pos.y+5, 0, 20)

    def wys(self):
        pygame.draw.rect(self.main.screen,(0,0,0),self.krawedzie)
        pygame.draw.rect(self.main.screen,self.GUI.colour, self.tlo)
        if self.GUI.mana!=0:
            pygame.draw.rect(self.main.screen, (0,0,255), self.pasek)
        #pygame.draw.rect(self.main.screen,(255,255,255),self.pasekdododania)
        self.DodawanieMany()


    def DodawanieMany(self):
        self.speed =0.01
        for i in range(2):
            if self.GUI.manadoDodania >0 and self.GUI.mana<self.GUI.max_mana:
                self.GUI.manadoDodania-=self.speed
                self.GUI.mana+=self.speed
            elif self.GUI.manadoDodania >0 and self.GUI.mana>self.GUI.max_mana:
                self.GUI.manadoDodania=0
            if self.GUI.manadoDodania <0 and self.GUI.mana>0:
                self.GUI.manadoDodania+=self.speed
                self.GUI.mana-=self.speed
            elif self.GUI.manadoDodania <0 and self.GUI.mana<0:
                self.GUI.manadoDodania = 0

            self.pasek = pygame.Rect(self.pos.x + 5, self.pos.y + 5, (self.GUI.mana/self.GUI.max_mana)*240, 20)


