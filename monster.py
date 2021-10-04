import pygame


class Monstre(pygame.sprite.Sprite):
    def __init__(self,game,player):
        super().__init__()
        self.game         = game
        self.player       = player
        self.vie          = 100
        self.vie_actuelle = 100
        self.atacke       = 5
        self.image        = pygame.image.load('assets/mummy.png')
        self.velocity     = 10
        self.rect         = self.image.get_rect()
        self.rect.x       = 1000
        self.rect.y       = 540
        self.velocity     = 0.1
        self.animation    = [pygame.image.load('assets/mummy/mummy1.png'),
        pygame.image.load('assets/mummy/mummy2.png'),
        pygame.image.load('assets/mummy/mummy3.png'),
        pygame.image.load('assets/mummy/mummy4.png'),
        pygame.image.load('assets/mummy/mummy5.png'),
        pygame.image.load('assets/mummy/mummy6.png'),
        pygame.image.load('assets/mummy/mummy7.png'),
        pygame.image.load('assets/mummy/mummy8.png'),
        pygame.image.load('assets/mummy/mummy9.png'),
        pygame.image.load('assets/mummy/mummy10.png'),
        pygame.image.load('assets/mummy/mummy11.png'),
        pygame.image.load('assets/mummy/mummy12.png'),
        pygame.image.load('assets/mummy/mummy13.png'),
        pygame.image.load('assets/mummy/mummy14.png'),
        pygame.image.load('assets/mummy/mummy15.png'),
        pygame.image.load('assets/mummy/mummy16.png'),
        pygame.image.load('assets/mummy/mummy17.png'),
        pygame.image.load('assets/mummy/mummy18.png'),
        pygame.image.load('assets/mummy/mummy19.png'),
        pygame.image.load('assets/mummy/mummy20.png'),
        pygame.image.load('assets/mummy/mummy21.png'),
        pygame.image.load('assets/mummy/mummy22.png'),
        pygame.image.load('assets/mummy/mummy23.png'),
        pygame.image.load('assets/mummy/mummy24.png')] 


    def deplacer(self):
        if not self.game.verifie_collision(self,self.game.tt_player):
            self.rect.x -= self.velocity

        if self.rect.x < 0 :
            self.remove()
            print("monstre sup!!")
    
    
    def blesse(self):
        return self.game.verifie_collision(self,self.game.tt_player) #:
            #self.game.tt_monsters.remove(self)
            #print("montre sup!")
            

