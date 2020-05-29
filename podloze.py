import pygame

class Podloze():
    def __init__(self,wlasciwosci ,pos):
        self.main=wlasciwosci[0]
        self.img=wlasciwosci[1]
        self.pos=pygame.Vector2(pos)
        self.d =wlasciwosci[2]
        self.szerokosc=wlasciwosci[3]
    def wys(self):
        self.main.screen.blit(self.img, self.pos)

    def checkIsItToWys(self):
        if self.pos.x > -1000 and self.pos.x < 2000:
            return True
    def IsColision(self,pos):#kolizcja dla powierzchni
        if self.pos.x-self.main.Player.szerokosc < pos.x <self.pos.x+self.d-15 and self.pos.y>=pos.y+self.main.Player.szerokosc:
            return self.pos.y-self.main.Player.szerokosc
    def IsCollisionUnder(self,pos):

        if self.pos.x-self.main.Player.szerokosc < pos.x <self.pos.x+self.d-15 and self.pos.y+self.szerokosc<pos.y:
            #print(self.pos.y+self.szerokosc)
            return self.pos.y+self.szerokosc
    def IsCollisionNext(self,side):#kolizja dla scianki
        for i in range(int((self.pos.y+self.szerokosc) - (self.pos.y - (self.main.Player.szerokosc-2)))):
            if side == "right":
                if self.main.Player.pos.y<=self.pos.y+i+0.5-(self.main.Player.szerokosc-2) and self.main.Player.pos.y>=self.pos.y+i-0.5-(self.main.Player.szerokosc-2):
                    a=self.pos.x+self.d
                    if 0 > self.main.Player.pos.x + 14 - a > -20:
                        y = (0.5 - (self.main.Player.pos.x + 14 - a))
                        a -= y
                        self.main.Teren.Ruch(-y)
                    if 0 < self.main.Player.pos.x - a + 14 < 1:  # sprawdzenie czy zachodzi kolizja
                        return True


            elif side == "left":
                if self.main.Player.pos.y<=self.pos.y+i+0.5-(self.main.Player.szerokosc-2) and self.main.Player.pos.y>=self.pos.y+i-0.5-(self.main.Player.szerokosc-2):
                    a=self.pos.x
                    if 0 > a - (self.main.Player.pos.x + self.main.Player.szerokosc - 14) > -20:
                        y = (0.5 - (a - (self.main.Player.pos.x + self.main.Player.szerokosc - 14)))
                        a += y
                        self.main.Teren.Ruch(y)
                    if 0 < a - (self.main.Player.pos.x + self.main.Player.szerokosc - 14) < 1:  # sprawdzenie czy zachodzi kolizja
                        return True
    def CzyKlikniety(self):
        mousePos = pygame.mouse.get_pos()
        if mousePos[0]> self.pos.x and mousePos[0]<self.pos.x+self.d:
            if mousePos[1] > self.pos.y and mousePos[1] < self.pos.y+self.szerokosc:
                return self
    def WysNapis(self):
        self.font = pygame.font.Font("freesansbold.ttf", 16)
        self.napis = self.font.render(str(self.pos), True, (0, 0, 0))
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

        self.wczesniejszystan = self.keys


