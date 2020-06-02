import pygame
import asset
class Przycisk(object):
    def __init__(self,main,text,rozmiar,pos,colour,wielkoscfont,akcja):
        self.main = main
        self.wielkoscfont=wielkoscfont
        self.font = pygame.font.Font(asset.czcionkaRoboto,self.wielkoscfont)
        self.tekst = self.font.render(text,True,(0,0,0))
        self.dlugosc = rozmiar[0]
        self.szerokosc = rozmiar[1]
        self.pos= pygame.Vector2(pos)
        self.colour=colour
        self.przycisk = pygame.Rect(self.pos.x,self.pos.y,self.dlugosc,self.szerokosc)
        self.akcja=akcja
        self.wczesniejczyklik=None
    def Wys(self):
        pygame.draw.rect(self.main.screen,self.colour,self.przycisk)
        self.main.screen.blit(self.tekst,(self.pos.x,self.pos.y))
        self.Czyklikniety()
    def Czyklikniety(self):
        mousePos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pressed()[0] !=self.wczesniejczyklik[0]:
            if mousePos[0] > self.pos.x and mousePos[0] < self.pos.x + self.dlugosc:
                if mousePos[1] > self.pos.y and mousePos[1] < self.pos.y + self.szerokosc:
                    self.akcja()
        self.wczesniejczyklik= pygame.mouse.get_pressed()