import pygame
import pygame.key
import pygame.font
import sys
from pygame.time import delay
import random

pygame.init()

RUNNING=True

longueur=1000
largeur=666
couleur=[255,255,255]

screen = pygame.display.set_mode([longueur,largeur])

pygame.key.set_repeat(10, 10)

def quitter():
    global RUNNING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# or event.type==KEYDOWN(K_ESCAPE):
            RUNNING=False
            pygame.display.quit()
            sys.exit()


def fct_boutton(rectangle):
    global afficher
    mouse = pygame.mouse.get_pressed()
    if mouse[0]: # UP
        mouse_pos = pygame.mouse.get_pos()
         
        if rectangle.collidepoint(mouse_pos):
            print('Cliqué sur:', rectangle)
            afficher = jeu

def retour_menu():
    global afficher
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                afficher=menu

def menu():
    global afficher
    
    boutton=pygame.draw.rect(screen,(255,255,255),pygame.Rect(255,400, 490, 100))
    
    police = pygame.font.Font("police.ttf",40)
    police_titre = pygame.font.Font("police.ttf", 200)
    
    texte = police.render(("APPUYER POUR JOUER"), False, (0,0,0))     
    titre = police_titre.render(("PONG"), False, (255,255,255))
    
    screen.blit(texte, (265,430))
    screen.blit(titre, (210,75))
    
    fct_boutton(boutton)
    
def jeu():
    global afficher
    score1=0
    score2=0
    s1=str(score1)
    s2=str(score2)
    lst=[s1," ",":"," ",s2]
    xballe=500 # abcisse du centre de la balle
    yballe=333 # ordonnée du centre de la balle
    rballe=20  # rayon de la balle
    vxballe=12   #vitesse dans la direction des x positifs
    vyballe=16  # vitesse dans la direction des y positifs
    
    police = pygame.font.Font("police.ttf", 128)
    police_chrono = pygame.font.Font("police.ttf",50)
    chrono=0
        
    phrase="".join(lst)
    police = pygame.font.Font("police.ttf", 128)
    texte = police.render((phrase), True, (255, 255, 255))
    
    raquette_x=0
    raquette2_x=longueur-20
    raquette_y=largeur/2
    raquette2_y=largeur/2
    raquette_h=100
    raquette_l=20
    deplacement=10
    marge = 2*rballe
    
    pygame.key.set_repeat(10, 10)
    
    
    while chrono<20:
        chrono=chrono+(35/1000)
        chrono2=str(round((chrono),2))
        screen.fill([0,0,0])
        lst=[s1," ",":"," ",s2]
        phrase="".join(lst)
        
        texte = police.render((phrase), True, (255, 255, 255))
        textes = police_chrono.render((chrono2),True,(255,255,255))    
    
        balle = pygame.draw.circle(screen, couleur, [xballe,yballe], rballe, 0)
        raquette1 = pygame.draw.rect(screen, couleur, [raquette_x,raquette_y,raquette_l,raquette_h])
        raquette2 = pygame.draw.rect(screen, couleur, [raquette2_x,raquette2_y,raquette_l,raquette_h])
    
        screen.blit(texte,(longueur/2-130,30))
        screen.blit(textes,(longueur/2-10,2))
    
        xballe=xballe+vxballe
        yballe=yballe+vyballe
    
        #collision avec les murs, ajout des points et redémarrage de la balle après une petite pause
        if xballe+rballe > longueur:
            vxballe= -vxballe
            score1=score1+1
            vxballe=0
            vyballe=0
            xballe=500
            yballe=333
            if random.randint(1,2) == 1:
                vxballe = 12
                vyballe = 16
            else:
                vxballe = -12
                vyballe = -16
    
        if xballe-rballe < 0:
            vxballe= -vxballe
            score2=score2+1 
            vxballe=0
            vyballe=0
            xballe=500
            yballe=333
            if random.randint(1,2) == 1:
                vxballe = 12
                vyballe = 16
            else:
                vxballe = -12
                vyballe = -16
    
        if yballe+rballe > largeur:
            vyballe= -vyballe        
        if yballe-rballe < 0:
            vyballe= -vyballe
        s1=str(score1)
        s2=str(score2)   
    
        pygame.display.flip()
        pygame.time.delay(15)
    
    
        #collision entre le bord droit de la raquette de gauche (uniquement) et la balle (plus une marge)
        if xballe-rballe < raquette_x + raquette_l  and yballe > raquette_y - marge and yballe  < raquette_y + raquette_h + marge:
            vxballe = -vxballe
    
        #collision entre le bord gauche de la raquette de droite (uniquement) et la balle (plus une marge)
        if xballe + rballe > raquette2_x and yballe > raquette2_y - marge and yballe  < raquette2_y + raquette_h + marge:
            vxballe = -vxballe
    
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
    
            if event.type==pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_w]:
                    if raquette_y>0:
                        raquette_y=raquette_y-deplacement
                if pygame.key.get_pressed()[pygame.K_s]:
                    if raquette_y+raquette_h<largeur:
                        raquette_y=raquette_y+deplacement
                if pygame.key.get_pressed()[pygame.K_UP]:
                    if raquette2_y>0:
                        raquette2_y=raquette2_y-deplacement
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    if raquette2_y+raquette_h<largeur:
                        raquette2_y=raquette2_y+deplacement
    screen.fill([0,0,0])
    chrono2=0
    while chrono2<10:
        quitter()
        
        police = pygame.font.Font("police.ttf",40)
        
        if score1 > score2:
            texte2 = police.render(("VICTOIRE DU JOUEUR 1"),False,(255,255,255))
            screen.blit(texte2,(longueur/2-100,largeur/2))
        if score2 > score1:
            texte2 = police.render(("VICTOIRE DU JOUEUR 2"),False,(255,255,255))
            screen.blit(texte2,(longueur/2-100,largeur/2))
        if score1 == score2:
            texte2 = police.render(("EGALITE"),False,(255,255,255))    
            screen.blit(texte2,(longueur/2-100,largeur/2))
            
        screen.blit(texte2,(longueur/2-100,largeur/2))
        delay(100)
        chrono2=chrono2+0.1
    
afficher = menu
 
def boucle_principale():
    while RUNNING:
        screen.fill((0,0,0))
        
        quitter()

        afficher()
        pygame.display.update()
    pygame.quit()
  
boucle_principale()     