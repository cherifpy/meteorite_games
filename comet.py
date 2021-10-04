import pygame

class Comet(pygame.sprite.Sprite):
    
    def __init__(self,game):
        super().__init__()
        self.game      = game
        self.velocity  = 5
        self.image     = pygame.image.load('assets\comet.png') 
        self.rect      = self.image.get_rect()
        self.rect.x    = 540
        self.rect.y    = -70
        self.image     = pygame.transform.scale(self.image,(100,70))

    def attaquer(self):
        self.rect.y += self.velocity 
        if self.rect.y >680:
            self.game.tt_comets.remove(self)


    