import  pygame, asset
from button import Przycisk
class OknoPodwojnegoWyboru():
    def __init__(self,main,text,akcjaNegatywna,akcjapozytywna):
        self.main=main
        self.text =text
        self.akcjanegatywna = akcjaNegatywna
        self.akcjapozytywna=akcjapozytywna
        self.font = pygame.font.Font(asset.czcionkaRoboto, 20)
        self.napis = self.font.render(self.text, True, (0, 0, 0))
        self.Pole=pygame.Rect(200,200,400,200)
        self.PrzyciskNie = Przycisk(self.main,"    Nie",(80,20),(240,360),(255,0,0),20,self.Nie,True,(0,0,0),(200,0,0))
        self.PrzyciskTak = Przycisk(self.main, "    Tak", (80, 20), (480, 360), (0, 255, 0), 20, self.Tak, True,(0, 0, 0), (0, 200, 0))
    def wys(self):
        pygame.draw.rect(self.main.screen,(152,0,153),self.Pole)
        self.main.screen.blit(self.napis,pygame.Vector2(200,220))
        self.PrzyciskNie.Wys()
        self.PrzyciskTak.Wys()
    def Nie(self):
        self.akcjanegatywna()
    def Tak(self):
        self.akcjapozytywna()