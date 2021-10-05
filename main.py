import pygame
import random 
import time
from   Game      import game
from   monster   import Monstre
from   Projectile import projectile 
import tkinter  

pygame.init()
taille_screen = (1080,680)
screen = pygame.display.set_mode(taille_screen,pygame.DOUBLEBUF)


#definition icon
icone  = pygame.image.load('assets/button.png')
pygame.display.set_icon(icone)

#definition fond ecran
fond_ecran       = pygame.image.load('assets/bg.jpg')
fond_ecran_debut = pygame.image.load('assets/banner.png')
boutom_debut     = pygame.image.load('assets/button.png')
return_home      = pygame.image.load('assets/button.png')
fond_ecran_debut = pygame.transform.scale(fond_ecran_debut,(800,800))
boutom_debut     = pygame.transform.scale(boutom_debut,(200,90))
return_home      = pygame.transform.scale(return_home,(50,50))
game1            = game()
rect_buttom      = boutom_debut.get_rect()
rect_debut       = fond_ecran_debut.get_rect()
afficher         = True
clique_bouton    = False
i,j              = 0,0
nombre           = 0
time1            = time.time()
time2            = time.time()
projectile1      = projectile(game1.player1,game1)
toitoi = 2
while afficher:
    if not clique_bouton:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: afficher = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 420 and event.pos[0] <= 620:
                    if event.pos[1] >=520 and event.pos[1] <=610: clique_bouton = True
                 
        screen.blit(fond_ecran,(0,-210))
        screen.blit(fond_ecran_debut,(120,-100))
        screen.blit(boutom_debut,(420,520))
        pygame.display.flip()
    
    else :
        #gestion des evenement 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: afficher = False
            if event.type == pygame.KEYDOWN:
                game1.touches[event.key] = True
            elif event.type == pygame.KEYUP: game1.touches[event.key] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >1000 and event.pos[0]<1050:
                    if event.pos[1] >0 and event.pos[1] <=50 :
                        clique_bouton = False
                        game1 = game()

            
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_c: 
                    game1.player1.a_sauter = True  
                    game1.player1.nombre_saut +=1
                
                if event.key == pygame.K_SPACE:
                    if game1.player1.peux_lancer:
                        game1.player1.a_lancer = True
                        game1.player1.peux_lancer = False
                        projectile1 = game1.player1.lancer_prejectile()

        if game1.touches.get(pygame.K_RIGHT): game1.player1.avancer()
        if game1.touches.get(pygame.K_LEFT): game1.player1.reculer()
        
        if game1.player1.rect.y <=500 :
            if game1.player1.nombre_saut <=1:
                game1.player1.sauter() 
        
        screen.blit(fond_ecran,(0,-210))
        screen.blit(return_home,(1000,0))
        #aficher mon joueur
        #if len(game1.player1.tt_projectile) == 0 :
        if game1.player1.peux_lancer:
            screen.blit(game1.player1.image,game1.player1.rect)
        
        #affciher l'ensemble des projectile
        #game1.player1.tt_projectile.draw(screen)
        #affciher l'ensemble des projectile lances
        game1.player1.projectile_lances.draw(screen)
        
        
        #afficher les monstres
        # test pour supprimer les monstre morts
        if (time.time()-time1)>= 2:
            game1.cree_monstre()
            time1 = time.time()
        """
        #afficher les comets
        game1.tt_comets.draw(screen)

        #ajouter des comets
        if (time.time()-time2)>= 0.6:
            game1.cree_comet()
            time2 = time.time()
            nombre += 1
        """
        for monstre in game1.tt_monsters:
            #suppression du monstre en cas de collision
            if pygame.sprite.spritecollide(monstre ,game1.player1.tt_projectile,False,pygame.sprite.collide_mask):
                game1.tt_monsters.remove(monstre)
                game1.player1.tt_projectile.remove(projectile)
                print("monstre sup!")
            else:
                if i >= len(monstre.animation) :
                    i = 0
                    screen.blit(monstre.animation[i],monstre.rect)
                    i += 1
                else: 
                    screen.blit(monstre.animation[i],monstre.rect)
                    i+=1
             
        #lancer les monstres
        for zombi in game1.tt_monsters:
            zombi.deplacer()

        #lancer les comets
        for comet in game1.tt_comets:
            comet.attaquer()
        
        #lancer les projectile
        #for projectile in game1.player1.tt_projectile:
        if projectile1.est_lancer:
            if projectile1.j < 10 :
                screen.blit(game1.player1.animation_projectile[projectile1.j],game1.player1.rect) 
                projectile1.j +=1
            else :
                if projectile1.j == 10 : 
                    projectile1.est_lancer = False   
        else:
            if projectile1.j<24:
                projectile1.lancer()
                screen.blit(game1.player1.animation_projectile[projectile1.j],game1.player1.rect)
                projectile1.j+=1
            if projectile1.j == 24:
                game1.player1.peux_lancer = True
                game1.player1.projectile_lances.add(projectile1)    
                #game1.player1.tt_projectile.remove(projectile1)
            print(projectile1.j)        
            screen.blit(projectile1.image,projectile1.rect)
        for proj in game1.player1.projectile_lances:      
            proj.lancer()
        game1.player1.cree_bare_vie(screen)

     
        #print(game1.verifie_collision(game1.player1,game1.tt_monsters))
        pygame.display.flip()