import pygame, asset
from button import Przycisk
class PlanszUstawien():
    def __init__(self, main, pos):
        self.main = main
        self.pos = pygame.Vector2(pos)
        self.rect = pygame.Rect(self.pos.x,self.pos.y,800,580)

        self.font20 = pygame.font.Font(asset.czcionkaRoboto, 20)
        self.napisDzwieki = self.font20.render("Dźwięki", True, (0, 0, 0))
        self.regulacjaDzwiekiMain = Regulacja_Glosnosci(self.main,(20,50),self.main.relugacjaDzwiekow.glownaGlosnosc,
                                                        self.main.relugacjaDzwiekow.ZmianaGlownejGlosnosci,"Główny")
        self.regulacjaDzwiekuClick = Regulacja_Glosnosci(self.main, (20, 80), self.main.relugacjaDzwiekow.glosnoscClick,
                                                        self.main.relugacjaDzwiekow.ZmianaGlosnoscClick, "GUI",
                                                        self.main.relugacjaDzwiekow.soundclick)
        self.regulacjaDzwiekuJump = Regulacja_Glosnosci(self.main,(20,110),self.main.relugacjaDzwiekow.glosnoscJump,
                                                        self.main.relugacjaDzwiekow.ZmianaGlosnoscJump,"Skok",
                                                        self.main.relugacjaDzwiekow.soundJump)
        self.regulacjaDzwiekuShoot = Regulacja_Glosnosci(self.main, (20, 140), self.main.relugacjaDzwiekow.glosnoscStrzal,
                                                        self.main.relugacjaDzwiekow.ZmianaGlosnoscStrzal, "Walka",
                                                        self.main.relugacjaDzwiekow.shootsound)
        self.regulacjaDzwiekuMana = Regulacja_Glosnosci(self.main, (20, 170),
                                                         self.main.relugacjaDzwiekow.glosnoscMana,
                                                         self.main.relugacjaDzwiekow.ZmianaGlosnoscMana, "Zbieranie",
                                                         self.main.relugacjaDzwiekow.zbieraniesound)
    def wys(self):
        #pygame.draw.rect(self.main.screen,(100,100,100),self.rect)
        self.main.screen.blit(self.napisDzwieki,self.pos+pygame.Vector2(0,5))
        self.regulacjaDzwiekiMain.wys()
        self.regulacjaDzwiekuClick.wys()
        self.regulacjaDzwiekuJump.wys()
        self.regulacjaDzwiekuShoot.wys()
        self.regulacjaDzwiekuMana.wys()
        if self.main.relugacjaDzwiekow.zmiana:
            self.PrzypiszNoweDzwieki()
            self.main.relugacjaDzwiekow.zmiana=False
    def PrzypiszNoweDzwieki(self):
        self.regulacjaDzwiekiMain.dzwiek=self.main.relugacjaDzwiekow.soundclick

        self.main.Player.jumpSound =  self.main.relugacjaDzwiekow.soundJump
        self.main.Player.shootsound = self.main.relugacjaDzwiekow.shootsound
class Regulacja_Glosnosci():
    def __init__(self,main,pos,wartosc,akcja,tytul, dzwiek=None):
        self.main=main
        self.pos = pygame.Vector2(pos)
        self.akcja = akcja
        self.dzwiek = dzwiek

        self.ZmianaWartosci(wartosc)

        self.PrzyciskMinus = Przycisk(self.main, "  -", pygame.Vector2(30, 20), self.pos + pygame.Vector2(70, 0),
                                      (153, 0, 153), 15, self.Minus, textColour2=(153, 51, 153), czygracdzwiek=False)
        self.PrzyciskPlus = Przycisk(self.main, "  +", pygame.Vector2(30, 20), self.pos + pygame.Vector2(190, 0),
                                     (153, 0, 153), 15, self.Plus, textColour2=(153, 51, 153), czygracdzwiek=False)
        self.font15 = pygame.font.Font(asset.czcionkaRoboto, 15)
        self.napisDzwieki = self.font15.render(self.wartosc, True, (0, 0, 0))
        self.tytul = self.font15.render(tytul,True,(0,0,0))
        self.step=0.1
    def wys(self):
        self.PrzyciskPlus.Wys()
        self.main.screen.blit(self.tytul,self.pos+pygame.Vector2(0,2))
        self.main.screen.blit(self.napisDzwieki,self.pos+pygame.Vector2(130,0))
        self.PrzyciskMinus.Wys()
    def Plus(self):
        if float(self.wartosc[:-1])<100:
            self.ZmianaWartosci(self.akcja(self.step))
            self.napisDzwieki = self.font15.render(self.wartosc, True, (0, 0, 0))
            self.ZagrajDzwiek()
    def Minus(self):
        if float(self.wartosc[:-1])-self.step>=0:
            self.ZmianaWartosci(self.akcja(-self.step))
            self.napisDzwieki = self.font15.render(self.wartosc, True, (0, 0, 0))
        else:
            self.wartosc = (str(0)+"%")
            self.napisDzwieki = self.font15.render(self.wartosc, True, (0, 0, 0))
        self.ZagrajDzwiek()
    def ZagrajDzwiek(self):
        if self.dzwiek == None:
            pass
        else:
            self.dzwiek.play()
    def ZmianaWartosci(self,przystosowanie):
        przystosowanie = round(przystosowanie,3)
        przystosowanie *=100
        przystosowanie = str(przystosowanie)
        if przystosowanie.count(".") != 0:
            przystosowanie = przystosowanie[0:przystosowanie.index(".")]
        przystosowanie =przystosowanie+"%"

        self.wartosc = przystosowanie