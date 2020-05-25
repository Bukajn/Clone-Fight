import pygame

class Podloze():
    def __init__(self,main,img,pos,d,s):
        self.main=main
        self.img=img
        self.pos=pos
        self.d =d
        self.s=s
    def wys(self):
        self.main.screen.blit(self.img, self.pos)

    def checkIsItToWys(self):
        if self.pos.x > -1000 and self.pos.x < 2000:
            return True
    def IsColision(self,pos):
        if self.pos.x-20 < pos.x <self.pos.x+self.d-20 and self.pos.y>=pos.y+64:
            return self.pos.y-64
    def IsCollisionNextRight(self):#right
        a=[]
        #self.pos.x+self.d self.y+20
        for i in range(int((self.pos.y+self.s)-(self.pos.y-62))):
            if self.main.Player.pos.y<=self.pos.y+i+0.5-62 and self.main.Player.pos.y>=self.pos.y+i-0.5-62:
                a.append(pygame.Vector2(self.pos.x+self.d,self.pos.y+i))


        return a