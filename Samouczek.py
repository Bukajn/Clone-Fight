import pygame,asset
from Poziom import Poziom
from Poziom import PrzedmiotInteraktywny
from Poziom import PoleDialogowe
from Poziom import Cel
from Poziom import Tlo
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
                                              asset.soundDoor,asset.soundDoor,czyaktywny=False)
        self.Bed =  PrzedmiotInteraktywny(self.main,
                                              asset.imgBed,asset.imgBedObramowka,
                                              asset.imgBed,asset.imgBedObramowka,
                                              (140,231),
                                              self.PolozSie,self.PolozSie,
                                              asset.soundBed,asset.soundBed,czyaktywny=False)
        self.Telefon = PrzedmiotInteraktywny(self.main,
                                             asset.imgPhone, asset.imgPhoneObramowka,
                                             asset.imgPhone,asset.imgPhoneObramowka,
                                             (627,45),
                                             self.OdbierzTelefon,self.OdbierzTelefon,
                                             odleglosc=150,czyaktywny=False)
        self.ZnakAutobusowy = PrzedmiotInteraktywny(self.main,
                                                    asset.imgZnakAutobusowy,asset.imgZnakAutobusowyObramowka,
                                                    asset.imgZnakAutobusowy,asset.imgZnakAutobusowyObramowka,
                                                    (3400,195),
                                                    self.PrzywołajAutobus,self.PrzywołajAutobus)
        self.autobus=None
        self.cel = Cel(self.main)
        self.obiekty = [[pygame.Rect(-2, 311, 802, 402),self.DomColour],[pygame.Rect(-2, -73, 802, 102),self.DomColour],[pygame.Rect(698, 0, 107, 211),self.DomColour],
                        [pygame.Rect(-2, 0, 107, 311),self.DomColour],[pygame.Rect(488, 149, 210, 32),self.DomColour],[pygame.Rect(105,311,605,10),self.PodlogaColour],
                        [pygame.Rect(488, 149, 210, 10), self.PodlogaColour],[pygame.Rect(613,94, 80, 55), (99, 63, 8)],
                        self.Drzwi,
                        self.Bed,
                        self.Telefon,
                        self.ZnakAutobusowy,
                        self.cel
                        ]#[pygame.Rect(700, 211, 10, 100),(99, 63, 8)]

        super().__init__(main,self.mapa,self.styl)

        self.UstawWlasciwosci()

        self.CzyGraczSiePolozyl=False
        self.OdebranyTelefon =False
        self.tlo = Tlo(self.main, asset.imgTloSamouczek)
        self.phoneRinging =pygame.mixer.Sound(asset.soundPhone)
        self.zegar = pygame.time.Clock()
        self.CzasMiniety =0

        self.etap=15
        self.Odblokuj()
    def Odblokuj(self):
        self.Bed.czyAktywny=True
        self.Telefon.czyAktywny=True
        self.Drzwi.czyAktywny=True

    def UstawWlasciwosci(self):
        super().UstawWlasciwosc()
        #niewidzialnosc i szerokosc
        self.obiektyDoKontrolowania[0].CzyWyswietlac = False
        self.obiektyDoKontrolowania[0].d=10
        self.obiektyDoKontrolowania[1].pojscieNaskos(pygame.Vector2(2607.5,466),pygame.Vector2(2607.5,295))

        #self.obiektyDoKontrolowania[3].pojscieNaskos(pygame.Vector2(147,254),pygame.Vector2(147,154))

    def OtworzDrzwi(self):
        self.obiektyDoKontrolowania[0].CzyKolizja=False
    def ZamknijDrzwi(self):
        self.obiektyDoKontrolowania[0].CzyKolizja = True

    def PolozSie(self):
        self.main.Player.CzydzialaGrawitacja =False
        self.CzyGraczSiePolozyl=True
        ileprzesunacTeren = 324 - self.Bed.pos.x
        self.main.Teren.Ruch(ileprzesunacTeren)
        self.main.Player.ZmianaWprawo()
        self.main.Player.img = pygame.transform.rotozoom(self.main.Player.img,90,1)
        self.main.Player.pos.y = 218
    def OdbierzTelefon(self):
        self.OdebranyTelefon = True
    def PrzywołajAutobus(self):

        if self.autobus in self.main.Teren.pods:
            self.main.Teren.pods.remove(self.autobus)

        self.autobus = self.main.Teren.UtworzElement(1,[self.main.Teren.elements[1],self.ZnakAutobusowy.pos+pygame.Vector2(130,110)],czyZwrocicElement=True)
        self.autobus.UstawMotyw(2)
        self.autobus.pojscieNaskos(self.ZnakAutobusowy.pos+pygame.Vector2(1040,110),self.ZnakAutobusowy.pos+pygame.Vector2(1040,110))
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
                                                "Teraz nauczmy cię skakać",
                                               akcjaKoncowa=self.ZwiekszEtapzResetem, czySkipAktywny=True)
        elif self.etap==4:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 440), "",
                                                "Kliknij Spacje by skoczyć",
                                               akcjaKoncowa=self.ZwiekszEtap, czySkipAktywny=False)
        elif self.etap==5:
            self.main.Player.CzyMoznaSkoczyc = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.ZwiekszEtap()
                self.poleDialogowe=None
        elif self.etap==6:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 440), "",
                                                "Z niektórymi przedmiotami możesz wejść w interakcje. Są to przedmioty, które podczas najechania na nich myszką, mają białą obwódkę ",
                                               70,akcjaKoncowa=self.ZwiekszEtapzResetem, czySkipAktywny=True)
        elif self.etap==7:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 440), "",
                                                "By wejść w interakcje z przedmiotem musisz na niego najechać myszką i kliknąć przycisk 'e'",
                                               70,akcjaKoncowa=self.ZwiekszEtapzResetem, czySkipAktywny=True)
        elif self.etap==8:
            if self.poleDialogowe == None:

                self.poleDialogowe = PoleDialogowe(self.main, (10, 440), "",
                                                "Połóż się na łóżku",
                                               70,akcjaKoncowa=self.ZwiekszEtapzResetemPolozeniaSie, czySkipAktywny=False)

        elif self.etap==9:
            self.Bed.czyAktywny = True
            if self.CzyGraczSiePolozyl:
                self.poleDialogowe=None
                self.ZwiekszEtap()
                self.zegar.tick()

        elif self.etap==10:
            if self.CzasMiniety<5:
                self.CzasMiniety+= self.zegar.tick()/1000
            else:
                self.Telefon.czyAktywny=True
                self.cel.UstawNowyCel(self.Telefon.pos, "Odbierz telefon")
                self.ZwiekszEtap()
                self.CzasMiniety=3.1
                self.zegar.tick()
                self.poleDialogowe = PoleDialogowe(self.main, (10, 440), "",
                                                   "By wejść w interakcje z niektórymi przedmiotami musisz być wystarczająco blisko nich",
                                                   72, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==11:
            if self.CzasMiniety>3:
                self.phoneRinging.play()
                self.CzasMiniety=0
            else:
                self.CzasMiniety+=self.zegar.tick()/1000

        elif self.etap==12:
            if self.poleDialogowe ==None:
                self.OdebranyTelefon = False
                self.poleDialogowe = PoleDialogowe(self.main, (10, 440), "",
                              "Odbierz telefon",
                              70)
            if self.CzasMiniety>3:
                self.phoneRinging.play()
                self.CzasMiniety=0
            else:
                self.CzasMiniety+=self.zegar.tick()/1000
            if self.OdebranyTelefon == True:
                self.phoneRinging.set_volume(0)
                self.ZwiekszEtap()
                self.poleDialogowe = PoleDialogowe(self.main, (10, 440), "Doktor Brown:",
                                                   "Cześć. Mam nadzieje, że jesteś pełen sił. Koniecznie musisz coś zobaczyć. Przyjdź do laboratorium.",
                                                   73,akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==13:
            self.Drzwi.czyAktywny=True
        elif self.etap==14:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 440), "",
                              "Jeśli chcesz sprawdzić aktualny cel oraz zobaczyć pobliskie przedmioty interaktywne przytrzymaj klawisz 'r'",
                              70)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                self.ZwiekszEtapzResetem()
        elif self.etap==15:
            self.main.Teren.Ruch(-2800)
            self.ZwiekszEtap()
    def wys(self):
        for i in self.obiekty:
            if type(i) == list:
                if type(i[0]) == pygame.Rect:
                    pygame.draw.rect(self.main.screen,i[1],i[0])
            else:
                i.wys()
        if self.poleDialogowe!=None:
            self.poleDialogowe.wys()
    def ZwiekszEtapzResetemPolozeniaSie(self):
        self.ZwiekszEtap()
        self.CzyGraczSiePolozyl=False
