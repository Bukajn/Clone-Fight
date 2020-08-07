import pygame, asset

class OpisPoziomu():
    def __init__(self,main):
        self.main = main

        self.width=0
        self.heigth=0
        self.x=410
        self.y=0
        self.widthDocelowe=380
        self.heigthDocelowe=540
        self.xDocelowe=410
        self.yDocelowe=30
        self.pole = pygame.Rect(410,30,self.width,self.heigth) #self.pole = pygame.Rect(410,30,380,540)
        self.nazwaPoziomuText = "Początek"

        self.otworzony = False
        self.animacjaOtwierania = False
        self.animacjaZamykania = True

        self.procent = 0

        self.docelowawielkoscCzionki = 30
        self.Napisy(0)
        self.pos = pygame.Vector2(self.x,self.y)
    def wys(self):
        if self.pole[2] != 0:
            pygame.draw.rect(self.main.screen,(128,128,128),self.pole)
            self.main.screen.blit(self.nazwaPoziomu, self.pos + pygame.Vector2(5,5))
        if self.animacjaOtwierania ==True:
           self.animacjaOtwierania = self.Animacja(1,0.70,540,380)
        elif self.animacjaZamykania == True:
            self.animacjaZamykania = self.Animacja(-1,-0.70,0,0)
    def ZaczecieOtwierania(self):
        self.otworzony = True
        self.animacjaZamykania=False
        self.animacjaOtwierania = True

    def ZaczecieZamykania(self):
        self.otworzony = False
        self.animacjaOtwierania=False
        self.animacjaZamykania =True
    def Animacja(self,plusheight,pluswidht,heightcel,widthcel):
        #powiekszanieWidth = 0,70
        for i in range(20):

            if self.heigth!=heightcel:
                #zmiana wielkosci pola
                self.heigth+=plusheight
                self.width+=pluswidht

                #obliczenie pozycji
                self.y=self.yDocelowe + (self.heigthDocelowe-self.heigth)/2
                self.x = self.xDocelowe + (self.widthDocelowe - self.width) / 2

                #ustawienie rectu pola, procentw i poyscji
                self.pole = pygame.Rect(self.x, self.y, self.width, self.heigth)
                self.pos = pygame.Vector2(self.x, self.y)
                self.procent = (self.heigth / self.heigthDocelowe)
                self.Napisy(int(self.docelowawielkoscCzionki*self.procent))


            else:
                self.width=widthcel
                self.y=self.yDocelowe
                self.x=self.xDocelowe
                self.pole = pygame.Rect(self.x, self.y, self.width, self.heigth)
                self.pos = pygame.Vector2(self.x, self.y)
                self.procent = (self.heigth / self.heigthDocelowe) * 100
                return False

        return True
    def Napisy(self, wielkoscCzcionki):
        self.font = pygame.font.Font(asset.czcionkaRoboto, wielkoscCzcionki)
        self.nazwaPoziomu = self.font.render(self.nazwaPoziomuText, True, (0, 0, 0))