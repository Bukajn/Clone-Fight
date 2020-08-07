import pygame
import asset
class Przycisk(object):
    def __init__(self,main,text,rozmiar,pos,colour,wielkoscfont,akcja,wyswietlanieTla=True,textColour=(0,0,0),textColour2=None,czygracdzwiek=True):
        self.main = main
        self.wielkoscfont=wielkoscfont
        self.font = pygame.font.Font(asset.czcionkaRoboto,self.wielkoscfont)
        self.Text = text
        self.dlugosc = rozmiar[0]
        self.szerokosc = rozmiar[1]
        self.pos= pygame.Vector2(pos)
        self.colour1=colour
        self.colour=colour
        self.przycisk = pygame.Rect(self.pos.x,self.pos.y,self.dlugosc,self.szerokosc)
        self.akcja=akcja
        self.wczesniejczyklik=pygame.mouse.get_pressed()
        self.WyswietlanieTla= wyswietlanieTla
        self.TextColour = textColour
        self.TextColour2=textColour2
        self.czyGracDzwiek = czygracdzwiek
        self.tekst = self.font.render(self.Text, True, self.TextColour)

        self.najechany = False
    def Wys(self):

        self.przycisk = pygame.Rect(self.pos.x, self.pos.y, self.dlugosc, self.szerokosc)

        if self.WyswietlanieTla:
            pygame.draw.rect(self.main.screen,self.colour,self.przycisk)
        self.main.screen.blit(self.tekst,(self.pos.x,self.pos.y))
        self.Czynajechany()
    def Czynajechany(self):
        mousePos = pygame.mouse.get_pos()
        if mousePos[0] > self.pos.x and mousePos[0] < self.pos.x + self.dlugosc and mousePos[1] > self.pos.y and mousePos[1] < self.pos.y + self.szerokosc:
            self.najechany=True
            if self.TextColour2 !=None:
                if self.WyswietlanieTla==False:
                    self.tekst = self.font.render(self.Text, True, self.TextColour2)
                else:
                    self.colour=self.TextColour2
            self.Czyklikniety()
        else:
            self.najechany = False
            if self.WyswietlanieTla == False:
                self.tekst = self.font.render(self.Text, True, self.TextColour)
            else:
                self.colour = self.colour1
    def Czyklikniety(self):
        if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pressed()[0] !=self.wczesniejczyklik[0]:
            if self.czyGracDzwiek:
                self.main.relugacjaDzwiekow.soundclick.play()
            self.akcja()
        self.wczesniejczyklik= pygame.mouse.get_pressed()