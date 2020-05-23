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
        if self.pos.x < pos.x < self.pos.x+self.d and self.pos.y>=pos.y+64:

            return self.pos.y-64


