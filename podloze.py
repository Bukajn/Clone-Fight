import pygame
import asset
class Podloze():
    def __init__(self,wlasciwosci ,pos):
        self.numerElementu = 0
        self.main=wlasciwosci[0]
        self.img=wlasciwosci[1]
        self.pos=pygame.Vector2(pos)
        self.d =wlasciwosci[2]
        self.szerokosc=wlasciwosci[3]
        self.podazajzamysza=False
    def __str__(self):
        return ("|"+str(self.numerElementu)+",("+str(self.pos.x)+";"+str(self.pos.y)+")"+"%")
    def wys(self):
        self.main.screen.blit(self.img, self.pos)
        if self.podazajzamysza:
            self.pos = pygame.Vector2(pygame.mouse.get_pos())
        if self.podazajzamysza and pygame.mouse.get_pressed()[0]:
            self.podazajzamysza=False
    def checkIsItToWys(self):
        if self.pos.x > -1000 and self.pos.x < 800:
            return True
    def IsColision(self,pos,szerokosc=0):#kolizcja dla powierzchni
        if self.pos.x-szerokosc < pos.x <self.pos.x+self.d-15 and self.pos.y>=pos.y+szerokosc:
            return self.pos.y-szerokosc
    def IsCollisionUnder(self,pos,szerokosc=0):

        if self.pos.x-szerokosc < pos.x <self.pos.x+self.d-15 and self.pos.y+self.szerokosc<pos.y:
            #print(self.pos.y+self.szerokosc)
            return self.pos.y+self.szerokosc
    def IsCollisionNext(self,side,szerokosc,pos,obiektwywołujący):#kolizja dla scianki
        for i in range(int((self.pos.y+self.szerokosc) - (self.pos.y - (szerokosc-2)))):
            if side == "right":
                if pos.y<=self.pos.y+i+0.5-(szerokosc-2) and pos.y>=self.pos.y+i-0.5-(szerokosc-2):
                    a=self.pos.x+self.d
                    if 0 > pos.x + 14 - a > -20:
                        y = (0.5 - (self.main.Player.pos.x + 14 - a))
                        a -= y
                        try:
                            obiektwywołujący.Ruch(-y)
                        except:
                            pass
                    if 0 < pos.x - a + 14 < 20:  # sprawdzenie czy zachodzi kolizja
                        return True


            elif side == "left":
                if pos.y<=self.pos.y+i+0.5-(szerokosc-2) and pos.y>=self.pos.y+i-0.5-(szerokosc-2):
                    a=self.pos.x
                    if 0 > a - (pos.x + szerokosc - 14) > -20:
                        y = (0.5 - (a - (pos.x + szerokosc - 14)))
                        a += y
                        try:
                            obiektwywołujący.Ruch(y)
                        except:
                            pass
                    if 0 < a - (pos.x + szerokosc-14) < 20:  # sprawdzenie czy zachodzi kolizja
                        return True
    def CzyKlikniety(self):
        mousePos = pygame.mouse.get_pos()
        if mousePos[0]> self.pos.x and mousePos[0]<self.pos.x+self.d:
            if mousePos[1] > self.pos.y and mousePos[1] < self.pos.y+self.szerokosc:
                return self
    def WysNapis(self,colour):
        self.font = pygame.font.Font(asset.czcionkaRoboto, 16)
        self.napis = self.font.render(str(self.pos), True, colour)
        self.main.screen.blit(self.napis,(self.pos.x+self.d/2,self.pos.y+self.szerokosc/2))
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
        self.wczesniejszystan = self.keys
    def Zmienpolozenie(self,x):
        self.pos.x+=x


