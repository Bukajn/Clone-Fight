import pygame

class Podloze():
    def __init__(self, main, img, pos, dlugosc, s):
        self.main=main
        self.img=img
        self.pos=pos
        self.d =dlugosc
        self.szerokosc=s
    def wys(self):
        self.main.screen.blit(self.img, self.pos)

    def checkIsItToWys(self):
        if self.pos.x > -1000 and self.pos.x < 2000:
            return True
    def IsColision(self,pos):
        if self.pos.x-self.main.Player.szerokosc < pos.x <self.pos.x+self.d-15 and self.pos.y>=pos.y+self.main.Player.szerokosc:
            return self.pos.y-self.main.Player.szerokosc
    def IsCollisionNext(self,side):#kolizja dla scianki
        a=[]
        for i in range(int((self.pos.y+self.szerokosc) - (self.pos.y - (self.main.Player.szerokosc-2)))):
            if side == "right":
                if self.main.Player.pos.y<=self.pos.y+i+0.5-(self.main.Player.szerokosc-2) and self.main.Player.pos.y>=self.pos.y+i-0.5-(self.main.Player.szerokosc-2):
                    a.append(pygame.Vector2(self.pos.x+self.d,self.pos.y+i))

            elif side == "left":
                if self.main.Player.pos.y<=self.pos.y+i+0.5-(self.main.Player.szerokosc-2) and self.main.Player.pos.y>=self.pos.y+i-0.5-(self.main.Player.szerokosc-2):
                    a.append(pygame.Vector2(self.pos.x,self.pos.y+i))

        return a


