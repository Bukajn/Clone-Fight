import pygame,asset
from Poziom import Poziom
from Poziom import PrzedmiotInteraktywny
from Poziom import PoleDialogowe
class Samouczek(Poziom):
    def __init__(self,main):
        self.main= main
        self.mapa="samouczek"
        self.styl=2
        self.DomColour = (125, 161, 10)
        self.PodlogaColour = (255, 164, 107)
        self.Drzwi =PrzedmiotInteraktywny(self.main,
                                              asset.imgDrzwi,asset.imgDrzwiObramowka,
                                              asset.imgDrzwiOtwarte,asset.imgDrzwiOtwarteObramowka,
                                              (700,211),
                                              self.OtworzDrzwi,self.ZamknijDrzwi,
                                              asset.soundDoor,asset.soundDoor)
        self.Bed =  PrzedmiotInteraktywny(self.main,
                                              asset.imgBed,asset.imgBedObramowka,
                                              asset.imgBed,asset.imgBedObramowka,
                                              (140,231),
                                              self.PolozSie,self.PolozSie)
        self.Telefon = PrzedmiotInteraktywny(self.main,
                                             asset.imgPhone, asset.imgPhoneObramowka,
                                             asset.imgPhone,asset.imgPhoneObramowka,
                                             (627,45))
        self.obiekty = [[pygame.Rect(-2, 311, 802, 402),self.DomColour],[pygame.Rect(-2, -73, 802, 102),self.DomColour],[pygame.Rect(698, 0, 107, 211),self.DomColour],
                        [pygame.Rect(-2, 0, 107, 311),self.DomColour],[pygame.Rect(488, 149, 210, 32),self.DomColour],[pygame.Rect(105,311,605,10),self.PodlogaColour],
                        [pygame.Rect(488, 149, 210, 10), self.PodlogaColour],[pygame.Rect(613,94, 80, 55), (99, 63, 8)],
                        self.Drzwi,
                        self.Bed,
                        self.Telefon]#[pygame.Rect(700, 211, 10, 100),(99, 63, 8)]

        super().__init__(main,self.mapa,self.styl)

        self.UstawWlasciwosci()
        #self.etap=3
    def UstawWlasciwosci(self):
        super().UstawWlasciwosc()
        #niewidzialnosc i szerokosc
        self.obiektyDoKontrolowania[0].CzyWyswietlac = False
        self.obiektyDoKontrolowania[0].d=10

    def OtworzDrzwi(self):
        self.obiektyDoKontrolowania[0].CzyKolizja=False
    def ZamknijDrzwi(self):
        self.obiektyDoKontrolowania[0].CzyKolizja = True

    def PolozSie(self):
        self.main.Player.CzydzialaGrawitacja =False

        ileprzesunacTeren = 324 - self.Bed.pos.x
        self.main.Teren.Ruch(ileprzesunacTeren)
        self.main.Player.ZmianaWprawo()
        self.main.Player.img = pygame.transform.rotozoom(self.main.Player.img,90,1)
        self.main.Player.pos.y = 218
    def Fabula(self):
        if self.etap==0:
            self.PolozSie()
            self.main.Player.CzyMoznaSkoczyc=False
            self.main.Teren.czySterowanieAktywne=False
            self.etap+=1
        elif self.etap==1:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main,(10,440),"",
                                                   "Użyj klawiszy 'a' i 'd' do poruszania się w lewo i w prawo",akcjaKoncowa=self.ZwiekszEtap,czySkipAktywny=False)

        elif self.etap==2:
            self.main.Teren.czySterowanieAktywne=True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] or keys[pygame.K_d]:
                self.ZwiekszEtap()
                self.poleDialogowe=None
        elif self.etap==3:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 440), "",
                                                "Teraz nauczmy się skakać",
                                               akcjaKoncowa=self.ZwiekszEtapzResetem, czySkipAktywny=True)
        elif self.etap==4:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 440), "",
                                                "Klknij Spacje by skoczyć",
                                               akcjaKoncowa=self.ZwiekszEtap, czySkipAktywny=False)
        elif self.etap==5:
            self.main.Player.CzyMoznaSkoczyc = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.ZwiekszEtap()
        elif self.etap==6:
            self.poleDialogowe=None
    def wys(self):
        for i in self.obiekty:
            if type(i) == list:
                if type(i[0]) == pygame.Rect:
                    pygame.draw.rect(self.main.screen,i[1],i[0])
            else:
                i.wys()
        if self.poleDialogowe!=None:
            self.poleDialogowe.wys()