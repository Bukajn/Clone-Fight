import pygame
from podloze import Podloze
class Wyspa(Podloze):
    def __init__(self,wlasciwosci ,pos, mnoznik=1):
        super().__init__(wlasciwosci ,pos, mnoznik)
        self.numerElementu = 1
