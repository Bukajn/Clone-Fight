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
        self.napisCeleDodatkoweText = "Cele dodatkowe"

        self.nazwaPoziomuText = "Początek"
        self.miniatura = pygame.image.load(asset.imgMiniaturaSamouczek)
        self.opisText=["Doktora znam od zawsze. Na początku jako sąsiada z","góry, potem jako nauczyciela fizyki, a teraz jako",
                       "przyjaciela. Od zawsze miał szalone pomysły. Raz omal","nie wysadził szkoły. Pewnego razu jeden z jego szalonych",
                       "pomysłow miał uratować świat. Niestety wszystko","zepsułem. Ale zacznę od początku. Pewnego ranka",
                       "zadzwonił telefon..."]


        self.opis=[]

        self.otworzony = False
        self.animacjaOtwierania = False
        self.animacjaZamykania = True

        self.procent = 0

        self.docelowawielkoscCzionki = 30
        self.Napisy()
        self.pos = pygame.Vector2(self.x,self.y)
    def wys(self):
        if self.pole[2] != 0:
            pygame.draw.rect(self.main.screen,(128,128,128),self.pole)
            self.main.screen.blit(self.nazwaPoziomu, self.pos + pygame.Vector2(5*self.procent,5*self.procent))
            pygame.draw.line(self.main.screen,(0,0,0),self.pos + pygame.Vector2((5*self.procent),(40*self.procent)),
                             self.pos + pygame.Vector2((370*self.procent),(40*self.procent)))
            self.main.screen.blit(pygame.transform.scale(self.miniatura,(int(370*self.procent),int(141*self.procent))),
                                  self.pos+pygame.Vector2(5*self.procent,50*self.procent))
            for i in range(len(self.opis)):
                self.main.screen.blit(self.opis[i],self.pos + pygame.Vector2(5*self.procent,(200+15*i)*self.procent))

            self.main.screen.blit(self.napisCeleDodatkowe, self.pos + pygame.Vector2(5 * self.procent, 400 * self.procent))
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
        for i in range(30):

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
                self.Napisy()


            else:
                self.width=widthcel
                self.y=self.yDocelowe
                self.x=self.xDocelowe
                self.pole = pygame.Rect(self.x, self.y, self.width, self.heigth)
                self.pos = pygame.Vector2(self.x, self.y)
                self.procent = (self.heigth / self.heigthDocelowe)
                return False

        return True
    def Napisy(self):
        self.font30 = pygame.font.Font(asset.czcionkaRoboto, int(30*self.procent))
        self.font20 = pygame.font.Font(asset.czcionkaRoboto, int(20 * self.procent))
        self.font14 = pygame.font.Font(asset.czcionkaRoboto, int(14 * self.procent))
        self.nazwaPoziomu = self.font30.render(self.nazwaPoziomuText, True, (0, 0, 0))
        self.napisCeleDodatkowe = self.font20.render(self.napisCeleDodatkoweText, True, (0,0,0))
        self.opis=[]
        for i in self.opisText:
            self.opis.append(self.font14.render(i,True,(0,0,0)))