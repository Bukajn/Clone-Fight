import pygame,asset
from Poziom import Poziom
from Poziom import PrzedmiotInteraktywny
from Poziom import PoleDialogowe
from Poziom import Cel
from Poziom import Tlo
from Poziom import Checkpoint
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
                                              asset.soundDoor,asset.soundDoor,czyaktywny=False,CzywykonacReset=True)
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
        self.Drzwi2 = PrzedmiotInteraktywny(self.main,
                                           asset.imgDrzwi, asset.imgDrzwiObramowka,
                                           asset.imgDrzwiOtwarte, asset.imgDrzwiOtwarteObramowka,
                                           (6606, 398),
                                           self.OtworzDrzwi2, self.ZamknijDrzwi2,
                                           asset.soundDoor, asset.soundDoor,CzywykonacReset=True)
        self.Profesor = PrzedmiotInteraktywny(self.main,
                                              asset.imgProfessor,asset.imgProfessorObramowka,
                                              asset.imgProfessor,asset.imgProfessorObramowka,
                                              (7106,405),
                                              self.ZwiekszEtap,self.ZwiekszEtap)
        self.Klononowator = PrzedmiotInteraktywny(self.main,
                                                 asset.imgKlonowator,asset.imgKlonowatorObramowka,
                                                 asset.imgKlonowator,asset.imgKlonowatorObramowka,
                                                 (6956, 301),
                                                  self.ZwiekszEtap,czyaktywny=False)
        self.Drzwi3 = PrzedmiotInteraktywny(self.main,
                                            asset.imgDrzwi, asset.imgDrzwiObramowka,
                                            asset.imgDrzwiOtwarte, asset.imgDrzwiOtwarteObramowka,
                                            (7507, 398),
                                            self.OtworzDrzwi3, self.ZamknijDrzwi3,
                                            asset.soundDoor, asset.soundDoor,czyaktywny=False,CzywykonacReset=True)
        self.wieza = PrzedmiotInteraktywny(self.main,
                                           asset.imgWieza,asset.imgwiezaObramowka,
                                           asset.imgWieza,asset.imgwiezaObramowka,
                                           (14200, 205),
                                           self.Koniec,self.Koniec)
        self.mur= [pygame.Rect(8109,370,102,128),(128,128,128)]
        self.autobus=None
        self.cel = Cel(self.main)
        self.CheckPoint = Checkpoint(self.main,self)
        self.tlo2 = Tlo(self.main, asset.imgTloSamouczek2)
        self.obiekty = [[pygame.Rect(-2, 311, 802, 402),self.DomColour],[pygame.Rect(-2, -73, 802, 102),self.DomColour],[pygame.Rect(698, 0, 107, 211),self.DomColour],
                        [pygame.Rect(-2, 0, 107, 311),self.DomColour],[pygame.Rect(488, 149, 210, 32),self.DomColour],[pygame.Rect(105,311,605,10),self.PodlogaColour],
                        [pygame.Rect(488, 149, 210, 10), self.PodlogaColour],[pygame.Rect(613,94, 80, 55), (99, 63, 8)],self.mur,
                        self.Drzwi,
                        self.Bed,
                        self.Telefon,
                        self.ZnakAutobusowy,
                        self.Drzwi2,
                        self.Profesor,
                        self.Klononowator,
                        self.Drzwi3,
                        self.wieza,
                        self.tlo2,
                        self.cel,
                        self.CheckPoint
                        ]#[pygame.Rect(700, 211, 10, 100),(99, 63, 8)]

        super().__init__(main,self.mapa,self.styl)
        self.nazwa="Samouczek"
        self.UstawWlasciwosci()

        self.CzyGraczSiePolozyl=False
        self.OdebranyTelefon =False

        self.phoneRinging =pygame.mixer.Sound(asset.soundPhone)
        self.zegar = pygame.time.Clock()
        self.CzasMiniety =0
        self.tlo = Tlo(self.main, asset.imgTloSamouczek)
        self.jablko = pygame.image.load(asset.imgJablko)
        self.soundKlonowator = pygame.mixer.Sound(asset.soundKlonowator)
        self.soundWin = pygame.mixer.Sound(asset.soundWin)
        self.DoktorNadawca ="Doktor Brown:"
        self.TyNadawca = "Ty:"
        self.KlonNadawca = "Twój klon:"
        self.etap=0
        #self.Odblokuj

    def Odblokuj(self):
        self.Bed.czyAktywny=True
        self.Telefon.czyAktywny=True
        self.Drzwi.czyAktywny=True

    def UstawWlasciwosci(self):
        super().UstawWlasciwosci()
        #niewidzialnosc i szerokosc
        self.obiektyDoKontrolowania[0].CzyWyswietlac = False
        self.obiektyDoKontrolowania[0].d=10
        self.obiektyDoKontrolowania[1].pojscieNaskos(pygame.Vector2(2607.5,466),pygame.Vector2(2607.5,295))
        self.obiektyDoKontrolowania[2].CzyWyswietlac = False
        self.obiektyDoKontrolowania[2].d = 5
        self.obiektyDoKontrolowania[3].CzyWyswietlac = False
        self.obiektyDoKontrolowania[3].d = 5
        self.obiektyDoKontrolowania[4].CzyWyswietlac = False
        self.obiektyDoKontrolowania[5].CzyWyswietlac = False
        self.obiektyDoKontrolowania[6].CzyWyswietlac = False

    def OtworzDrzwi(self):
        self.obiektyDoKontrolowania[0].CzyKolizja=False
    def ZamknijDrzwi(self):
        self.obiektyDoKontrolowania[0].CzyKolizja = True
    def OtworzDrzwi2(self):
        self.obiektyDoKontrolowania[2].CzyKolizja=False
    def ZamknijDrzwi2(self):
        self.obiektyDoKontrolowania[2].CzyKolizja = True
    def OtworzDrzwi3(self):
        self.obiektyDoKontrolowania[3].CzyKolizja=False
    def ZamknijDrzwi3(self):
        self.obiektyDoKontrolowania[3].CzyKolizja = True
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
            self.main.Player.czyMozeStrzelac=False
            self.main.Player.czyMozeWykonacPromien=False
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
                self.poleDialogowe = PoleDialogowe(self.main, (10, 440), self.DoktorNadawca,
                                                   "Cześć. Mam nadzieje, że jesteś pełen sił. Koniecznie musisz coś zobaczyć. Przyjdź do laboratorium.",
                                                   73,akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==13:
            pass
        elif self.etap==14:
            if self.poleDialogowe == None:
                self.cel.UstawNowyCel(self.Profesor.pos, "Pójdź do laboratorium")
                self.poleDialogowe = PoleDialogowe(self.main, (10, 440), "",
                              "Jeśli chcesz sprawdzić aktualny cel oraz zobaczyć pobliskie przedmioty interaktywne przytrzymaj klawisz 'r'",
                              70)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                self.poleDialogowe=None
                self.etap=14.1
        elif self.etap== 14.1:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 440), "",
                                                   "W określonych momentach tworzy się punkt kontrolny. Do tych punktów wracasz gdy, zginiesz. Podczas i stworzenia występuje następująca animacja.",
                                                   75,akcjaKoncowa=self.ZwiekszEtapLess,czySkipAktywny=True)
        elif self.etap==14.2:
            self.poleDialogowe=None
            self.CheckPoint.UstawCheckPoint(14.3)
            self.etap=14.3
        elif self.etap==14.3:
            self.etap=15
            self.Drzwi.czyAktywny = True
        elif self.etap==15:
            #self.main.Teren.Ruch(-5800)
            self.ZwiekszEtap()
        elif self.etap==16:
            if self.main.Player.pos.x>self.Drzwi2.pos.x:
                self.cel.pos.y= -100
                if self.Drzwi2.stan1==False:
                    self.Drzwi2.Zmiana()
                self.Drzwi2.czyAktywny=False
        elif self.etap ==17:
            self.Profesor.czyAktywny=False
            if self.poleDialogowe ==None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                               "Cześć. W końcu przyszedłeś",
                                               73, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                               czySkipAktywny=True)
        elif self.etap==18:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.TyNadawca,
                                               "Co chciałeś pokazać?",
                                               73, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                               czySkipAktywny=True)
        elif self.etap ==19:
            self.Profesor.pos.x-=1
            if self.Profesor.pos.x<self.Klononowator.pos.x-30:
                self.ZwiekszEtap()
        elif self.etap ==20:
            self.Profesor.pos.x += 1
            if self.Profesor.pos.x > self.Klononowator.pos.x + 300:
                self.ZwiekszEtap()
        elif self.etap==21:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                               "Patrz. 3..2..1.. Odpalam",
                                               73, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                               czySkipAktywny=True)
        elif self.etap==22:
            self.Klononowator.img = pygame.image.load(asset.imgKlonowatorUruchomiony)
            self.soundKlonowator.play()
            self.ZwiekszEtap()
            self.zegar.tick()
            self.CzasMiniety = 0
        elif self.etap==23:
            if self.CzasMiniety<3:
                self.soundKlonowator.play()
                self.CzasMiniety+= self.zegar.tick()/1000
            else:
                self.ZwiekszEtap()
        elif self.etap==24:
            self.Klononowator.img = pygame.image.load(asset.imgKlonowator)
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.TyNadawca,
                                               "Łał",
                                               73, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                               czySkipAktywny=True)
        elif self.etap==25:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                                   "To ja! To ja rozwiązałem problem głodu na świecie!",
                                                   73, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==26:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.TyNadawca,
                                                   "A mógłbym siebie sklonować?",
                                                   73, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==27:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                                   "Nie, nie, nie. Nie badałem tego, co oznacza, że jest to zbyt "
                                                   "niebezpieczne. Niewiadomo jak zadziała klonowanie na mózg",
                                                   75, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                    czySkipAktywny=True)
        elif self.etap==28:
            self.Profesor.pos.x -= 1
            if self.Profesor.pos.x < self.Klononowator.pos.x + 210:
                self.ZwiekszEtap()
        elif self.etap==29:
            self.Profesor.pos.x -= 1
            if self.Profesor.pos.x < self.Klononowator.pos.x -30:
                self.ZwiekszEtap()
        elif self.etap==30:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                                   "Zabieram te jabłka na badania. Zostań tu i niczego nie ruszaj. Za chwile wrócę",
                                                   79, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                    czySkipAktywny=True)
        elif self.etap ==31:
            self.Profesor.pos.x += 1
            if self.Profesor.pos.x > self.Klononowator.pos.x + 300:
                self.Profesor.Czywyswietla = False
                self.ZwiekszEtap()
        elif self.etap==32:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.TyNadawca,
                                                   "Mieć swojego klona to coś. By wykonywał za mnie wszystkie ciężkie zadania",
                                                   79, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                    czySkipAktywny=True)
        elif self.etap == 33:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.TyNadawca,
                                                   "Bym miał czas na różne fajne rzeczy. Na przykład... mógłbym ulepszać świat. To jest dobre. Co szkodzi spróbować?",
                                                   79, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==34:
            #self.main.Teren.Ruch(-5800)
            self.Klononowator.czyAktywny=True
            self.cel.UstawNowyCel(self.Klononowator.pos,"Sklonuj się")
            self.ZwiekszEtap()
        elif self.etap==35:
            pass
        elif self.etap == 36:
            self.Klononowator.czyAktywny = False
            self.main.Teren.czySterowanieAktywne=False
            self.main.Player.CzyMoznaSkoczyc=False
            if self.main.Player.pos.x>self.Klononowator.pos.x-40:
                self.ZwiekszEtap()
            else:
                self.ZwiekszEtap()
                self.ZwiekszEtap()
        elif self.etap == 37: #w przypadku gry gracz jest na prawo od klonowatora
            if self.main.Player.pos.x>self.Klononowator.pos.x-40:
                self.main.Player.ZmianaWLewo()
                self.main.Teren.Ruch(1)
            else:
                self.ZwiekszEtap()
                self.ZwiekszEtap()
        elif self.etap == 38:
            if self.main.Player.pos.x <= self.Klononowator.pos.x - 40:
                self.main.Player.ZmianaWprawo()
                self.main.Teren.Ruch(-1)
            else:
                self.ZwiekszEtap()
        elif self.etap == 39:
            self.main.Player.ZmianaWprawo()
            self.ZwiekszEtap()
        elif self.etap == 40:
            self.Klononowator.img2 = pygame.image.load(asset.imgKlonowatorUruchomiony)
            self.soundKlonowator.play()
            self.ZwiekszEtap()
            self.zegar.tick()
            self.CzasMiniety = 0
        elif self.etap == 41:

            if self.CzasMiniety < 3:
                self.soundKlonowator.play()
                self.CzasMiniety += self.zegar.tick() / 1000
            else:
                self.ZwiekszEtap()
        elif self.etap==42:
            self.Klononowator.img2 = pygame.image.load(asset.imgKlonowator)
            self.ZwiekszEtap()
        elif self.etap==43:
            self.mainEnemy = self.main.Teren.UtworzElement(3, [self.main.Teren.elements[3],
                                                             self.Klononowator.pos + pygame.Vector2(205, 0)],czyZwrocicElement=True)
            self.main.Teren.pods.append(self.mainEnemy)
            self.mainEnemy.czydzialaAi=False
            self.mainEnemy.czywyswietlaccPasekZrowia=False
            self.mainEnemy.ZmianaWLewo()
            self.ZwiekszEtap()
            self.CzasMiniety=0
            self.zegar.tick()
        elif self.etap==44:
            if self.CzasMiniety < 2:
                self.CzasMiniety += self.zegar.tick() / 1000
            else:
                self.ZwiekszEtap()
        elif self.etap==45:
            self.Profesor.Czywyswietla=True
            self.ZwiekszEtap()
        elif self.etap==46:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                                   "Okazuje się, że jabłka nie są w 100% indenty...",
                                                   79, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==47:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                                   "Coś ty zrobił!!!",
                                                   79, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==48:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.TyNadawca,
                                                   "Eee... Do odważnych świat należy?",
                                                   79, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==49:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                                   "Mówiłem, żebyś niczego nie dotykał",
                                                   79, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==50:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.TyNadawca,
                                                   "Przeprowadziłem eksperyment",
                                                   79, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==51:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                                   "Nie na tym polegają eskperymenty",
                                                   79, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==52:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.TyNadawca,
                                                   "Bym mógł pomagać większej ilości ludzi",
                                                   79, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==53:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.KlonNadawca,
                                                   "Kłamiesz",
                                                   79, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==54:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.TyNadawca,
                                                   "Kto to powiedział?",
                                                   79, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==55:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.KlonNadawca,
                                                   "Ja, kopia ciebie. Chciałeś mnie wykorzystywać. Chciałeś mieć swojego niewolnika. ",
                                                   80, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                  czySkipAktywny=True)
        elif self.etap==56:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.KlonNadawca,
                                                   "A to z pomaganiem ludziom to marna wymówka",
                                                   80, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==57:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.KlonNadawca,
                                                   "Wy ludzie jesteście tacy egoistyczni. Skoro już istnieję to uratuje ten świat od ludzi.",
                                                   80, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==58:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.KlonNadawca,
                                                   "Pożyczę sobie tę maszynę i z niej skorzystam. Przynajmniej tyle dobrego z niej będzie",
                                                   79, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)

        elif self.etap == 59:
            if self.poleDialogowe == None:
                self.Klononowator.Czywyswietla=False
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.KlonNadawca,
                                                   "Dowidzenia i ostrzegam,że nasze kolejne spotkanie nie będzie już takie miłe",
                                                   80, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap ==60:
            self.mainEnemy.pos.x+=2
            self.mainEnemy.ZmianaWprawo()
            if self.mainEnemy.pos.x>self.Klononowator.pos.x + 500:
                while self.mainEnemy in self.main.Teren.pods:
                    self.main.Teren.pods.remove(self.mainEnemy)
                self.ZwiekszEtap()
        elif self.etap ==61:
            #self.main.Teren.Ruch(-6200)
            self.ZwiekszEtap()
        elif self.etap ==62:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                                   "Musimy działać. Najpierw cię zbadam.",
                                                   80, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==63:
            self.zegar.tick()
            self.CzasMiniety=0
            self.main.Player.czyWyswietlac=False
            self.main.GUI.czywyswietlac=False
            self.ZwiekszEtap()
        elif self.etap==64:
            if self.CzasMiniety < 3:
                self.CzasMiniety += self.zegar.tick() / 1000
            else:
                self.ZwiekszEtap()
        elif self.etap==65:
            self.main.Player.czyWyswietlac = True


            self.main.GUI.czywyswietlac = True
            self.ZwiekszEtap()
        elif self.etap ==66:
            if self.poleDialogowe == None:
                self.Drzwi3.czyAktywny=True
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                                   "Twoje DNA uległo zmianie. Wyjaśnie ci po drodze. Teraz ruszaj zniszczyć swoje klony.",
                                                   78, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==67:
            self.main.Player.czyMozeStrzelac = True
            self.main.Player.CzyMoznaSkoczyc = True

            self.main.Teren.czySterowanieAktywne = True
            self.etap=67.1
            #self.main.Teren.Ruch(-7200)
        elif self.etap == 67.1:
            self.CheckPoint.UstawCheckPoint(67.2)
            self.etap = 67.2
        elif self.etap == 67.2:
            self.etap = 68
        elif self.etap==68:
            self.main.Teren.enemy[0].czydzialaAi=False
            self.main.Teren.enemy[0].ZmianaWLewo()
            self.wrog1 =self.main.Teren.enemy[0]
            self.wrogowie2 = self.main.Teren.enemy[1:4]
            for i in self.wrogowie2:
                i.czydzialaAi=False
            self.ZwiekszEtap()
        elif self.etap==69:

            if self.poleDialogowe ==None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                               "Twój klon stworzył kolejne klony do pomocy. Najwyraźniej poprawił w pewnym sensie maszyne, bo są mu w 100% posłuszne",
                                               75, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                               czySkipAktywny=True)
        elif self.etap==70:
            if self.poleDialogowe ==None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                               "Poprzez klonowanie zyskałeś moce. Na przykład możesz lewym przyciskiem myszy strzelać.",
                                               71, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                               czySkipAktywny=True)
        elif self.etap==71:
            self.cel.UstawNowyCel(self.wrog1.pos, "Zniszcz klona")
            self.ZwiekszEtap()
        elif self.etap==72:
            if not self.wrog1 in self.main.Teren.pods:
                self.cel.pos.y=-1000
                self.ZwiekszEtap()
        elif self.etap==73:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                                   "Z klonów wypadają apteczki (zielone kule) i mana (niebieskie kule)",
                                                   71, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap == 74:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                                   "Mana jest potrzebna do przeprowadzenia specjalnego ataku",
                                                   71, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==75:
            self.obiektyDoKontrolowania[4].CzyKolizja=False
            self.mur[0] = self.mur[0].move(801,0)
            self.ZwiekszEtap()
        elif self.etap==76:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                                   "Specjalny atak to promień. Jego siła jest zależna od ilości zebranej many. By go użyć należy wcisnąć prawy przycisk myszy.",
                                                   74, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==77:
            self.main.Player.czyMozeWykonacPromien=True
            self.cel.UstawNowyCel(self.wrogowie2[0].pos,"Zniszcz klony")
            self.ZwiekszEtap()
        elif self.etap==78:
            iloscWrogowPrzedmurem=0
            for i in self.main.Teren.enemy:
                if i.pos.x<self.mur[0][0]:
                    iloscWrogowPrzedmurem+=1
            if iloscWrogowPrzedmurem==0:
                self.ZwiekszEtap()
        elif self.etap==79:
            self.cel.pos.y=-1000
            self.etap=79.1
        elif self.etap == 79.1:
            self.CheckPoint.UstawCheckPoint(79.2)
            self.etap = 79.2
        elif self.etap ==79.2:
            self.etap = 80
        elif self.etap==80:
            if self.poleDialogowe == None:
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                                   "Pamiętaj, że klony też mogą cię atakować",
                                                   74, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)

        elif self.etap==81:
            self.cel.UstawNowyCel(self.main.Teren.enemy[0].pos,"Znisz klona")
            self.mur[0] = self.mur[0].move(800, 0)
            self.obiektyDoKontrolowania[5].CzyKolizja = False
            self.ZwiekszEtap()
        elif self.etap==82:
            iloscWrogowPrzedmurem = 0
            for i in self.main.Teren.enemy:
                if i.pos.x < self.mur[0][0]:
                    iloscWrogowPrzedmurem += 1
            if iloscWrogowPrzedmurem == 0:
                self.ZwiekszEtap()
        elif self.etap==83:

            if self.poleDialogowe == None:
                self.cel.UstawNowyCel(self.wieza.pos,"Dotrzyj do celu")
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                                   "To wszystko co musisz narazie wiedzeć. Dotrzyj do wyznaczonego punktu i niszcz klony. Powodenia",
                                                   72, akcjaKoncowa=self.ZwiekszEtapzResetem,
                                                   czySkipAktywny=True)
        elif self.etap==84:

            self.mur[0] = self.mur[0].move(0, -1000)
            self.obiektyDoKontrolowania[6].CzyKolizja = False
            self.etap=81.1
        elif self.etap == 81.1:
            self.CheckPoint.UstawCheckPoint(81.2)
            self.etap = 81.2
        elif self.etap == 81.2:
            self.obiektyDoKontrolowania[6].CzyKolizja = False
            self.etap = 85
        elif self.etap==85:
            if self.main.Player.pos.x>self.wieza.pos.x-400:
                self.ZwiekszEtap()

        elif self.etap==86:
            if self.poleDialogowe == None:
                self.cel.UstawNowyCel(self.wieza.pos,"Odpal wieże")
                self.poleDialogowe = PoleDialogowe(self.main, (10, 40), self.DoktorNadawca,
                                                   "Za każdym razem, na koniec poziomu musisz aktywować wieże ochronną. W ten sposób, na tym terenie już się pojawi żadan klon",
                                                   73)

        elif self.etap==87:
            self.soundWin.play()
            self.ZwiekszEtap()
        elif self.etap==88:
            if self.CzasMiniety<4:
                self.CzasMiniety+=self.zegar.tick()/1000
            else:
                self.ZwiekszEtap()
        elif self.etap==89:
            self.soundWin.play()
            self.wieza.img=pygame.image.load(asset.imgWiezaAktywowana)
            self.wieza.img2=pygame.image.load(asset.imgWiezaAktywowana)
            self.zegar.tick()
            self.CzasMiniety=0
            self.ZwiekszEtap()
        elif self.etap==90:
            if self.CzasMiniety<3:
                self.CzasMiniety+=self.zegar.tick()/1000
            else:
                self.running=False
        #linijki zapezbieeczjącze
        if self.etap<15:
            if self.main.Player.pos.y>400:
                self.main.Player.pos.y=100
    def Reset(self):
        self.poleDialogowe=None
    def Koniec(self):


        if self.main.Teren.enemy != []:
            self.poleDialogowe = PoleDialogowe(self.main, (10, 40), "",
                                                   "Na wybranym terenie znajdują się jeszcze klony. Zniszcz je.",
                                                   73, akcjaKoncowa=self.Reset,
                                                   czySkipAktywny=True)
        else:
            self.poleDialogowe=None
            self.wieza.czyAktywny=False
            self.zegar.tick()
            self.CzasMiniety=0
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
        if self.etap==20 or self.etap==21 or self.etap ==22 or self.etap==23 or self.etap==29:
            self.main.screen.blit(self.jablko, self.Klononowator.pos + pygame.Vector2(5, 178))
        if self.etap == 24 or self.etap==25 or self.etap==26 or self.etap==27 or self.etap==28:
            self.main.screen.blit(self.jablko, self.Klononowator.pos + pygame.Vector2(5, 178))
            self.main.screen.blit(self.jablko, self.Klononowator.pos + pygame.Vector2(240, 178))
        if self.etap == 64:
            pygame.draw.rect(self.main.screen,(0,0,0),pygame.Rect(0,0,800,600))
            self.font = pygame.font.Font(asset.czcionkaRoboto, 20)
            self.napis =self.font.render("Kilka godzin póżniej", True, (255, 255, 255))
            self.main.screen.blit(self.napis,(300,300))

    def ZwiekszEtapzResetemPolozeniaSie(self):
        self.ZwiekszEtap()
        self.CzyGraczSiePolozyl=False
