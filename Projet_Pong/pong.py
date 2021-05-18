import pygame
import pygame.key
import pygame.font
from pygame.time import delay

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
        if event.type == pygame.QUIT:
            RUNNING=False


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
    boutton=pygame.draw.rect(screen,(255,255,255),pygame.Rect(255,400, 490, 100))
    
    police = pygame.font.Font("police.ttf",40)
    police_titre = pygame.font.Font("police.ttf", 200)
    
    texte = police.render(("APPUYER POUR JOUER"), False, (0,0,0))     
    titre = police_titre.render(("PONG"), False, (255,255,255))
    
    screen.blit(texte, (265,430))
    screen.blit(titre, (210,75))
    
    fct_boutton(boutton)
    
def jeu():
    longueur=1000
    largeur=666
    couleur=[255,255,255]
    
    xballe=500 # abcisse du centre de la balle
    yballe=333 # ordonnée du centre de la balle
    rballe=20  # rayon de la balle
    vxballe=15   #vitesse dans la direction des x positifs
    vyballe=24  # vitesse dans la direction des y positifs


    raquette_x=30
    raquette2_x=longueur-30
    raquette_y=largeur/2
    raquette2_y=largeur/2
    raquette_h=100
    raquette_l=20
    deplacement=10
    marge = 2*rballe
    
    score1=0
    score2=0
    
    while True:
        quitter()
        s1=str(score1)
        s2=str(score2) 
        screen.fill([0,0,0])
        lst=[s1," ",":"," ",s2]
        phrase="".join(lst)
        police = pygame.font.Font("police.ttf", 128)
        texte = police.render((phrase), True, (255, 255, 255))

        pygame.draw.circle(screen, couleur, [xballe,yballe], rballe, 0)
        pygame.draw.rect(screen, couleur, [raquette_x,raquette_y,raquette_l,raquette_h])
        pygame.draw.rect(screen, couleur, [raquette2_x,raquette2_y,raquette_l,raquette_h])
        
        screen.blit(texte,(longueur/2-130,30))
        
        xballe=xballe+vxballe
        yballe=yballe+vyballe
        
        #collision avec les murs
        if xballe+rballe > longueur:
            vxballe= -vxballe
            score1=score1+1
            #decompte()
        if xballe-rballe < 0:
            vxballe= -vxballe
            score2=score2+1
            #decompte()
        if yballe+rballe > largeur:
            vyballe= -vyballe        
        if yballe-rballe < 0:
            vyballe= -vyballe  
    
        pygame.display.flip()
        delay(10)
    
        #collision entre le bord droit de la raquette de gauche (uniquement) et la balle (plus une marge)
        if xballe-rballe < raquette_x + raquette_l  and yballe > raquette_y - marge and yballe  < raquette_y + raquette_h + marge:
            vxballe = -vxballe
        
        #collision entre le bord gauche de la raquette de droite (uniquement) et la balle (plus une marge)
        if xballe + rballe > raquette2_x and yballe > raquette2_y - marge and yballe  < raquette2_y + raquette_h + marge:
            vxballe = -vxballe


        for event in pygame.event.get():
            
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
            
afficher = menu
 
def boucle_principale():
    while RUNNING:
        screen.fill( (0,0,0) )         
        quitter()
         
        ## Exécute la fonction affecté à afficher (menu/jeu)
        afficher()
        pygame.display.update()
         
    pygame.quit()
  
boucle_principale()            
          
            
            
            
            
            
            
            
            
            
            
            
            
            