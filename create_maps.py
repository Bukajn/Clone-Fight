import pygame

class Create_maps(object):
    def __init__(self,main):
        self.main=main
        self.font=pygame.font.Font("freesansbold.ttf",32)
        self.napis= self.font.render("Tworzenie mapy",True,(0,0,0))
        self.stan = "pojedynczy"
        self.informacja = self.font.render(self.stan,True,(0,0,0))
        self.obiekt=None
    def main_loop(self):
        self.running = True
        while self.running:
            self.main.screen.fill((100, 150, 255))
            self.check_events()
            self.main.Teren.wys()
            self.main.Player.wys()
            self.main.screen.blit(self.napis,(0,0))
            self.main.screen.blit(self.informacja, (500, 0))
            if pygame.mouse.get_pressed()[0]:
                for i in self.main.Teren.towys:
                    if i.CzyKlikniety()!=None:
                        self.obiekt = i.CzyKlikniety()
            if self.obiekt!=None:
                self.obiekt.WysNapis()
                self.obiekt.Zmianapolozenia(self.stan)

            pygame.display.update()
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.main.Player.pos.y = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_COMMA:
                if self.stan == "pojedynczy":
                    self.stan = "ciagly"
                else:
                    self.stan = "pojedynczy"
                self.informacja = self.font.render(self.stan, True, (0, 0, 0))