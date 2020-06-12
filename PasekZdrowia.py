import pygame
import decimal
class PasekZdrowia():
    def __init__(self,main,GUI):
        self.main=main
        self.GUI=GUI
        self.pos=pygame.Vector2(self.GUI.pos.x+10,self.GUI.pos.y+10)
        self.krawedzie=self.krawedzie = pygame.Rect(self.pos.x,self.pos.y,250,30)
        self.tlo = pygame.Rect(self.pos.x + 5, self.pos.y + 5, 240, 20)
        self.pasek = pygame.Rect(self.pos.x + 5, self.pos.y + 5, 0, 20)
        self.hpdododania=0
    def wys(self):
        pygame.draw.rect(self.main.screen, (0, 0, 0), self.krawedzie)
        pygame.draw.rect(self.main.screen, self.GUI.colour, self.tlo)
        if self.main.Player.hp-self.hpdododania>0:
            pygame.draw.rect(self.main.screen, (255, 0, 0), self.pasek)
        self.AnimacjaPaska()
    def AnimacjaPaska(self):
        self.speed = 2
        self.speed = int(self.hpdododania / 2)
        if self.speed < 0:
            self.speed *= -1
        if 0 <= self.speed < 2:
            self.speed = 2
        if self.speed > 10:
            self.speed = 10

        for i in range(self.speed):
            if self.hpdododania > 0:
                self.hpdododania -= 0.01
                self.hpdododania = float(decimal.Decimal(str(self.hpdododania)).quantize(decimal.Decimal('0.00')))
            elif self.hpdododania < 0 and (self.main.Player.hp - self.hpdododania)/self.main.Player.max_hp>0:
                self.hpdododania += 0.01
                self.hpdododania = float(decimal.Decimal(str(self.hpdododania)).quantize(decimal.Decimal('0.00')))

        self.pasek = pygame.Rect(self.pos.x + 5, self.pos.y + 5,((self.main.Player.hp - self.hpdododania) / self.main.Player.max_hp) * 240, 20)