import pygame

class Promien():
    def __init__(self,main):
        self.main=main
        self.maxSzerokosc = 64 * (self.main.GUI.mana/self.main.GUI.max_mana)
        self.szerokosc=0
        self.maxDlugosc=400
        self.dlugosc=0
        self.promien = pygame.Rect(self.main.Player.pos.x+self.main.Player.szerokosc,self.main.Player.pos.y+self.main.Player.szerokosc/2-self.szerokosc/2,self.dlugosc,self.szerokosc)
        self.MaksymalnyCzasTrwania = 3
        self.czasTrwania = self.MaksymalnyCzasTrwania * (self.main.GUI.mana/self.main.GUI.max_mana)
        self.czasMiniety=0
        self.clock = pygame.time.Clock()
        self.Czasodostatniegozapisu=0
        self.ObrazeniaNasekunde=-20

        self.delta=0.0
        self.max_tps=60
        self.clock2 = pygame.time.Clock()
    def wys(self):
        # tworzenie promienia
        if self.main.Player.ruch =="prawo":
            self.pos=pygame.Vector2(self.main.Player.pos.x + self.main.Player.szerokosc,self.main.Player.pos.y + self.main.Player.szerokosc / 2 - self.szerokosc / 2)
            self.promien = pygame.Rect(self.pos.x,
                                   self.pos.y, self.dlugosc,
                                   self.szerokosc)

        else:
            self.pos = pygame.Vector2(self.main.Player.pos.x - self.dlugosc,self.main.Player.pos.y + self.main.Player.szerokosc / 2 - self.szerokosc / 2)
            self.promien = pygame.Rect(self.pos.x,
                                       self.pos.y,
                                       self.dlugosc,
                                       self.szerokosc)

        # obliczanie czasu
        self.czasMiniety+=self.clock.tick()/1000
        # sprawdzanie czy czas minął
        if self.czasMiniety>self.czasTrwania:
            if self.szerokosc>0:
                self.szerokosc-=1
            else:
                self.main.Player.promien=None
        else:
            if self.dlugosc<self.maxDlugosc:
                self.dlugosc+=5
            if self.szerokosc<self.maxSzerokosc:
                self.szerokosc+=1
        # rysowanie promieniu
        pygame.draw.rect(self.main.screen, (0, 0, 255), self.promien)
        #odejmowanie zycia
        self.OdejmowanieZycia()
    def OdejmowanieZycia(self):

       for i in range(self.Zegar()):
            if self.main.Player.ruch =="prawo":
                for i in self.main.Teren.enemy:
                    if self.pos.x + self.dlugosc > i.pos.x > self.pos.x:
                        if self.pos.y - i.szerokosc < i.pos.y < self.pos.y + self.szerokosc:
                            i.HPdoDodania(self.ObrazeniaNasekunde/self.max_tps)

            else:
                for i in self.main.Teren.enemy:
                    if self.pos.x+self.dlugosc >i.pos.x >self.pos.x:
                        if self.pos.y - i.szerokosc < i.pos.y < self.pos.y + self.szerokosc:
                            i.HPdoDodania(self.ObrazeniaNasekunde/self.max_tps)

    def Zegar(self):
        self.delta += self.clock2.tick() / 1000.0
        i = 0
        while self.delta > 1 / self.max_tps:
            i += 1
            self.delta -= 1 / self.max_tps
        return i