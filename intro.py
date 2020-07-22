import pygame, sys
import  asset
class Intro():
    def __init__(self,main):
        self.main = main
        self.rozmiar=0
        self.font = pygame.font.Font(asset.czcionkaRoboto, 0)
        self.napis = self.font.render("Twórca:", True, (255, 255, 255))
        self.napis2 = self.font.render("Jakub Nowak", True, (255, 255, 255))
        self.napis3 = self.font.render("Dźwięki z Zapsplat.com", True, (255, 255, 255))
        self.etap=0
        self.zegar=pygame.time.Clock()
        self.CzasMiniety=0
    def main_loop(self):
        self.running=True
        while self.running:
            self.main.screen.fill((0,0,0))
            self.check_events()
            self.wys()
            self.fabula()
            pygame.display.update()
    def fabula(self):
        if self.etap==0 or self.etap==3:
            if self.rozmiar<20:
                if self.CzasMiniety<0.05:
                    self.CzasMiniety+=self.zegar.tick()/1000
                else:
                    self.CzasMiniety=0
                    self.ZmianaCzcionki(1)
            else:
                self.zegar.tick()
                self.etap+=1
        elif self.etap==1 or self.etap==4 or self.etap==6:
            if self.CzasMiniety<3:
                self.CzasMiniety += self.zegar.tick() / 1000
            else:
                self.etap+=1
        elif self.etap==2 or self.etap==5:
            if self.rozmiar>0:
                if self.CzasMiniety<0.05:
                    self.CzasMiniety+=self.zegar.tick()/1000
                else:
                    self.CzasMiniety=0
                    self.ZmianaCzcionki(-1)
            else:
                self.zegar.tick()
                self.etap+=1
        elif self.etap==7:
            self.running=False

    def ZmianaCzcionki(self,ile):

        self.rozmiar+=ile
        self.font = pygame.font.Font(asset.czcionkaRoboto, self.rozmiar)
        self.napis = self.font.render("Twórca", True, (255, 255, 255))
        self.napis2 = self.font.render("Jakub Nowak", True, (255, 255, 255))
        self.napis3 = self.font.render("Dźwięki z Zapsplat.com", True, (255, 255, 255))
    def wys(self):
        if self.etap<=2:
            self.wysNapis(self.napis,-40)
            self.wysNapis(self.napis2, 0)
        elif self.etap<=5:
            self.wysNapis(self.napis3, 0)
    def wysNapis(self,napis,y):
        rect = napis.get_rect()
        #self.main.screen.blit(napis,pygame.Vector2(0,0))
        self.main.screen.blit(napis,pygame.Vector2(400-(rect[2]/2),300-rect[3]/2+y))
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()