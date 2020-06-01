import pygame

class Mana_coin(object):
    def __init__(self,wlasciwosci,pos):
        self.name = "Mana_coin"
        self.numerElementu = 2
        self.main = wlasciwosci[0]
        self.img = wlasciwosci[1]
        self.pos = pygame.Vector2(pos)

        self.dlugosc = wlasciwosci[2]
        self.szerokosc = wlasciwosci[3]

        self.pozycjaYgorna = self.pos.y
        self.pozycjaYdolna = self.pos.y + self.dlugosc/2
        self.kierunek = 'dol'
        self.speed =0.03
        self.wczesniejszystanKreatora=0
        self.podazajzamysza = False
    def __str__(self):
        return ("|"+str(self.numerElementu)+",("+str(self.pos.x)+";"+str(self.pos.y)+")"+"%")
    def wys(self):
        self.main.screen.blit(self.img, self.pos)
        if self.podazajzamysza:
            self.pos = pygame.Vector2(pygame.mouse.get_pos())
        if self.podazajzamysza and pygame.mouse.get_pressed()[0]:
            self.pozycjaYgorna = self.pos.y
            self.pozycjaYdolna = self.pos.y + self.dlugosc / 2
            self.podazajzamysza=False

        if self.main.CzyKreatorOtworzony==False:
            self.ruch()
            self.wczesniejszystanKreatora = self.main.CzyKreatorOtworzony
        elif self.wczesniejszystanKreatora == False:
            self.wczesniejszystanKreatora=True
            self.pos.y = self.pozycjaYgorna
    def checkIsItToWys(self):
        if self.pos.x > -1000 and self.pos.x < 2000:
            return True
    def CzyKlikniety(self):
        mousePos = pygame.mouse.get_pos()
        if mousePos[0]> self.pos.x and mousePos[0]<self.pos.x+self.dlugosc:
            if mousePos[1] > self.pos.y and mousePos[1] < self.pos.y+self.szerokosc:
                return self
    def WysNapis(self,colour):
        self.font = pygame.font.Font("freesansbold.ttf", 16)
        self.napis = self.font.render(str(self.pos), True, colour)
        self.main.screen.blit(self.napis, (self.pos.x + self.dlugosc / 2, self.pos.y + self.szerokosc / 2))
    def Zmianapolozenia(self,stan):

        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_UP] and (self.wczesniejszystan[pygame.K_UP] !=self.keys[pygame.K_UP] or  stan =="ciagly"):
            self.pos.y-=1
        if self.keys[pygame.K_DOWN] and (self.wczesniejszystan[pygame.K_DOWN] !=self.keys[pygame.K_DOWN]or  stan =="ciagly"):
            self.pos.y+=1
        if self.keys[pygame.K_RIGHT] and (self.wczesniejszystan[pygame.K_RIGHT] !=self.keys[pygame.K_RIGHT]or  stan =="ciagly"):
            self.pos.x+=1
        if self.keys[pygame.K_LEFT] and (self.wczesniejszystan[pygame.K_LEFT] !=self.keys[pygame.K_LEFT]or  stan =="ciagly"):
            self.pos.x-=1
        if self.keys[pygame.K_DELETE]:
            self.main.Teren.pods.remove(self)
            self.main.create_maps.obiekt = None
        self.pozycjaYgorna = self.pos.y
        self.pozycjaYdolna = self.pos.y + self.dlugosc / 2
        self.wczesniejszystan = self.keys
    def ruch(self):
        if self.pos.y<self.pozycjaYdolna and self.kierunek == 'dol':
            self.pos.y+=self.speed
        else:
            self.kierunek = "gora"
        if self.pos.y> self.pozycjaYgorna and self.kierunek=="gora":
            self.pos.y-=self.speed
        else:
            self.kierunek ="dol"