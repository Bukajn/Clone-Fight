import pygame
from mana_coin import Mana_coin
class Apteczka(Mana_coin):
    def __init__(self,wlasciwosci,pos):
        super().__init__(wlasciwosci,pos)
        self.numerElementu=4
        self.iloscHP=10

        self.miejscedocelowe=pygame.Vector2(263,579)
    def Dodaj(self):
        self.main.Player.HPdoDodania(self.iloscHP)