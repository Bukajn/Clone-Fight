import pygame
import  asset

class RelugacjaDzwiekow():
    def __init__(self):
        self.zmiana=False

        self.glownaGlosnosc = 0.5
        self.glosnoscJump = 0.5
        self.glosnoscClick =1
        self.glosnoscStrzal = 0.4
        self.glosnoscMana = 0.5

        self.soundclick = pygame.mixer.Sound(asset.soundClick)
        self.soundJump = pygame.mixer.Sound(asset.soundJump)
        self.shootsound = pygame.mixer.Sound(asset.soundShoot)
        self.evilshootsound = pygame.mixer.Sound(asset.soundWrogStrzal)
        self.zbieraniesound = pygame.mixer.Sound(asset.zbieranieMana_coin)

        self.PrzystosowanieDziwekow()
    def PrzystosowanieDziwekow(self):
        self.soundclick.set_volume(self.glownaGlosnosc*self.glosnoscClick)
        self.soundJump.set_volume(self.glownaGlosnosc*self.glosnoscJump)
        self.shootsound.set_volume(self.glownaGlosnosc*self.glosnoscStrzal)
        self.evilshootsound.set_volume(self.glownaGlosnosc*self.glosnoscStrzal)
        self.zbieraniesound.set_volume(self.glownaGlosnosc*self.glosnoscMana)
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

    def ZmianaGlosnoscStrzal(self, a):
        self.glosnoscStrzal += a
        self.PrzystosowanieDziwekow()
        return self.glosnoscStrzal

    def ZmianaGlosnoscMana(self, a):
        self.glosnoscMana += a
        self.PrzystosowanieDziwekow()
        return self.glosnoscMana