import pygame
import asset
from button import Przycisk
import pickle
class OknoWyboru(object):
    def __init__(self,main):
        self.main = main
        self.pos = pygame.Vector2(30,51)
        self.okno = pygame.Rect(self.pos.x,self.pos.y,750,500)
        self.przyciskZamykania = pygame.Rect(750,51,30,30)
        self.gornyPasek = pygame.Rect(30,51,720,30)
        self.elementy =[]
        self.PrzyciskZapisz = Przycisk(self.main,"Zapisz",(85,26),(self.pos.x+10,self.pos.y+2),(255,255,255),25,self.Zapisz)
        #self.PrzyciskWczytaj = Przycisk(self.main,"Wczytaj",(105,26),(self.pos.x+105,self.pos.y+2),(255,255,255),25,self.Wczytaj)
        self.UtworzElementy()
        #self.Zapisz()
        #self.Wczytaj()
    def wys(self):
        pygame.draw.rect(self.main.screen,(0,0,0),self.okno)
        pygame.draw.rect(self.main.screen, (255, 0, 0), self.przyciskZamykania)
        pygame.draw.rect(self.main.screen, (128, 128, 128), self.gornyPasek)
        self.PrzyciskZapisz.Wys()
        #self.PrzyciskWczytaj.Wys()
        self.WyswietlElemnty()
        self.CzyKlikniety()

    def CzyKlikniety(self):
        mousePos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if mousePos[0]> 750 and mousePos[0]<780:
                if mousePos[1] > 51 and mousePos[1] < 81:
                    self.main.create_maps.otwarteOknoWyboru=False
    def UtworzElementy(self):
        pozycja = pygame.Vector2(self.pos.x+10,self.pos.y+50)
        for i in range(len(self.main.Teren.elements)):
            self.elementy.append(ElementyDoWyboru(self.main.Teren.elements[i],(pozycja.x,pozycja.y),i))
            pozycja.x += 120
    def WyswietlElemnty(self):
        for i in self.elementy:
            i.Wyswietl()
    def Zapisz(self,mapa=""):
        if mapa =="":
            nazwamapy=self.main.create_maps.mapa
        else:
            nazwamapy=mapa
        print(nazwamapy)
        plikdoZapisu= open("assets/maps/"+nazwamapy+".obj","wb")

        for i in self.main.Teren.pods:
            try:
                #przygotowanie do zapisu
                i.PrzygotujDoZapisu()
                i.main = str(i.main)

                #zapis
                pickle.dump(i,plikdoZapisu)
                #Po zapisie
                i.main = self.main
                i.PoWczytaniu()
            except AttributeError:
                i.main = self.main
                pass
        plikdoZapisu.close()
    def Wczytaj(self,mapa="",tworzenieNowejMapy=False):
        """if mapa == "":
            mapa = input("Wprowadź mapę(wpisz n by anulować):")
            if mapa == "n":
                return
        self.main.Teren.pods = []
        mapa = mapa.replace("'","")
        ostatecznaMapa =[]
        for i in range(mapa.count("|")):
            element = mapa[mapa.index("|")+1:mapa.index("%")]
            mapa = mapa[mapa.index("%")+1:len(mapa)]
            zmienne = [int(element[0:element.index(",")]),(float(element[element.index("(")+1:element.index(";")]),float(element[element.index(";")+1:element.index(")")]))]
            ostatecznaMapa.append(zmienne)
        for i in range(len(ostatecznaMapa)):
            self.main.Teren.UtworzElement(ostatecznaMapa[i][0],(self.main.Teren.elements[ostatecznaMapa[i][0]],ostatecznaMapa[i][1]))
        self.main.create_maps.otwarteOknoWyboru=False"""

        nazwamapy = mapa
        try:
            plikdoOdczytu = open("assets/maps/" + nazwamapy + ".obj", "rb")
        except FileNotFoundError:
            if tworzenieNowejMapy:
                self.main.Teren.pods=[]
                self.main.Teren.enemy=[]
                self.main.Teren.przesuniecie=0
                return
            else:
                print("nie znaleziono pilku")
                return
        self.main.Teren.pods = []
        self.main.Teren.enemy = []
        self.main.Teren.przesuniecie = 0
        while True:
            try:
                obiektDoDodania = pickle.load(plikdoOdczytu)
                obiektDoDodania.main = self.main
                obiektDoDodania.PoWczytaniu()
                self.main.Teren.pods.append(obiektDoDodania)
            except EOFError:
                plikdoOdczytu.close()
                print("ZakonczenieWczytywania")
                return


class ElementyDoWyboru(object):
    def __init__(self,wlasciwosci,pos,numerElementu):
        self.main = wlasciwosci[0]
        self.img=pygame.image.load(wlasciwosci[1])
        self.dlugosc = wlasciwosci[2]
        self.szerokosc = wlasciwosci[2]
        self.numerElementu=numerElementu
        self.dlugoscPola = 100
        self.szerokoscPola =100
        self.pos = pygame.Vector2(pos)
        self.pole = pygame.Rect(self.pos.x,self.pos.y,self.dlugoscPola,self.szerokoscPola)
        self.zmiejszone = True
        self.zmiejszoneImg = pygame.transform.rotozoom(self.img,0,90/self.dlugosc)
        self.normalneImg = self.img
        self.img=self.zmiejszoneImg
        self.wczesniejszyKlik = None
    def Wyswietl(self):
        pygame.draw.rect(self.main.screen,(128,128,128),self.pole)
        self.main.screen.blit(self.img, (self.pos.x, self.pos.y+5))
        self.CzyNajechany()
    def CzyNajechany(self):
        mousePos = pygame.mouse.get_pos()
        if mousePos[0] > self.pos.x and mousePos[0] < self.pos.x+self.dlugoscPola and mousePos[1] > self.pos.y and mousePos[1] < self.pos.y+self.szerokoscPola:
            if self.zmiejszone == True:
                self.zmiejszone=False
                self.img = self.normalneImg
            self.CzyKlikniety()
        elif self.zmiejszone==False:
            self.zmiejszone=True
            self.img=self.zmiejszoneImg
    def CzyKlikniety(self):
        mouseClick = pygame.mouse.get_pressed()[0]
        if mouseClick:
            self.wczesniejszyKlik =1
        elif self.wczesniejszyKlik==1:
            self.main.create_maps.otwarteOknoWyboru=False
            self.wczesniejszyKlik = None
            self.StworzElement()


    def StworzElement(self):
        elementdododania = (self.main.Teren.elements[self.numerElementu],(0,0))
        self.main.Teren.UtworzElement(self.numerElementu,elementdododania,True)
