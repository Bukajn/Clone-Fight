import pygame
import  asset

class RelugacjaDzwiekow():
    def __init__(self):
        self.zmiana=False

        self.glownaGlosnosc = 0.5
        self.glosnoscJump = 0.5
        self.glosnoscClick =1

        self.soundclick = pygame.mixer.Sound(asset.soundClick)
        self.soundJump = pygame.mixer.Sound(asset.soundJump)

        self.PrzystosowanieDziwekow()
    def PrzystosowanieDziwekow(self):
        self.soundclick.set_volume(self.glownaGlosnosc*self.glosnoscClick)
        self.soundJump.set_volume(self.glownaGlosnosc*self.glosnoscJump)
    def ZmianaGlownejGlosnosci(self, a):
        self.glownaGlosnosc += a
        self.PrzystosowanieDziwekow()
        return self.glownaGlosnosc
    def ZmianaGlosnoscJump(self,a):
        self.glosnoscJump +=a
        self.PrzystosowanieDziwekow()
        return self.glosnoscJump

    def ZmianaGlosnoscClick(self, a):
        self.glosnoscClick += a
        self.PrzystosowanieDziwekow()
        return self.glosnoscClick