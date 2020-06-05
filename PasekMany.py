import pygame
import decimal
class PasekMany(object):
    def __init__(self,main,GUI):
        self.main = main
        self.GUI = GUI
        self.pos = pygame.Vector2(self.GUI.pos.x+500,self.GUI.pos.y+10)
        self.krawedzie = pygame.Rect(self.pos.x,self.pos.y,250,30)
        self.tlo = pygame.Rect(self.pos.x+5, self.pos.y+5, 240, 20)
        self.pasek = pygame.Rect(self.pos.x+5, self.pos.y+5, 0, 20)
        #self.pasekdododania = pygame.Rect(self.pos.x+5, self.pos.y+5, 0, 20)
        self.manaDoDodania=0.0
    def wys(self):
        pygame.draw.rect(self.main.screen,(0,0,0),self.krawedzie)
        pygame.draw.rect(self.main.screen,self.GUI.colour, self.tlo)

        pygame.draw.rect(self.main.screen, (0,0,255), self.pasek)
        #pygame.draw.rect(self.main.screen,(255,255,255),self.pasekdododania)
        self.AnimacjaPaska()

    def AnimacjaPaska(self):
        self.speed = 2
        self.speed = int(self.manaDoDodania/2)
        if self.speed<0:
            self.speed*=-1
        if 0<=self.speed <2:
            self.speed=2
        if self.speed>10:
            self.speed=10

        for i in range(self.speed):
            if self.manaDoDodania>0:
                self.manaDoDodania-=0.01
                self.manaDoDodania=float(decimal.Decimal(str(self.manaDoDodania)).quantize(decimal.Decimal('0.00')))
            elif self.manaDoDodania<0:
                self.manaDoDodania += 0.01
                self.manaDoDodania = float(decimal.Decimal(str(self.manaDoDodania)).quantize(decimal.Decimal('0.00')))
        #print(self.manaDoDodania)

        self.pasek = pygame.Rect(self.pos.x + 5, self.pos.y + 5, ((self.GUI.mana-self.manaDoDodania) / self.GUI.max_mana) * 240, 20)
    def DodawajMane(self,ilosc):
        self.GUI.mana+=ilosc

        if self.GUI.mana>self.GUI.max_mana:
            self.GUI.mana =self.GUI.max_mana
        elif self.GUI.mana<0:
            self.GUI.mana =0
        else:
            self.manaDoDodania += ilosc
    def NaprawBladReprezantacyjny(self,pierwsza,druga):
        return float(decimal.Decimal(str(pierwsza)).quantize(decimal.Decimal(str(druga))))


