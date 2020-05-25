import pygame

class Player(object):
    def __init__(self,main):
        self.main = main
        self.img = pygame.image.load("assets/original.png")
        self.pos = pygame.Vector2(336,0)
        self.state = 1 # 0=na ziemie 1=podczas spadania 2=podczas skoku
        self.speed = pygame.Vector2(0,0)
        self.speedGravitation=0.005
        self.speedJump=-2
        self.wysSkoku=200
        self.old_pos_y=0
    def wys(self):
        self.Physik()
        self.main.screen.blit(self.img, self.pos)
    def Physik(self):

        height=self.main.Teren.ColisionWithFloar() #przyjęcie wysokości podłożą
        self.grawitacja(height)

        self.keys = pygame.key.get_pressed()
        self.jump()

        self.pos.y+=self.speed.y
        self.grawitacja(height)
    def grawitacja(self,height):
        if self.pos.y < height and self.speed!=2:
            self.speed.y += self.speedGravitation
        elif self.pos.y != self.old_pos_y: # jest na ziemi
            self.speed.y=0
            self.state=0
        if self.pos.y > height:
            self.pos.y = height
    def jump(self):
        if self.keys[pygame.K_SPACE] and self.state == 0:
            self.state = 2
            self.speed.y = self.speedJump
            self.posStart = self.pos.y
        if self.state == 2:
            if self.pos.y > self.old_pos_y - self.wysSkoku:
                if self.speed.y < -0.01:

                    self.speed.y += -(self.speed.y / (self.wysSkoku - (self.posStart - self.pos.y)))
            else:
                self.state = 1
        elif self.state == 0:
            self.old_pos_y = self.pos.y
