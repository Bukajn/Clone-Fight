import pygame
from mana_coin import Mana_coin
class Apteczka(Mana_coin):
    def __init__(self,wlasciwosci,pos,mnoznik=1,iloscdodawanejMany=10):
        super().__init__(wlasciwosci,pos,mnoznik,iloscdodawanejMany)
        self.numerElementu=4
        self.iloscHP=self.iloscdodawanejMany

        self.miejscedocelowe=pygame.Vector2(263,579)
    def Dodaj(self):
        self.main.Player.HPdoDodania(self.iloscHP)