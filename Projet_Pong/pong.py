import pygame
import sys
import pygame.key
import pygame.font

pygame.init()

longueur=1000
largeur=666
couleur=[255,255,255]
score1=0
score2=0
s1=str(score1)
s2=str(score2)
lst=[s1," ",":"," ",s2]

screen = pygame.display.set_mode([longueur,largeur])

screen.fill([0,0,0])

x=500 # abcisse du centre de la balle
y=333 # ordonnée du centre de la balle
r=20  # rayon de la balle
vx=8   #vitesse dans la direction des x positifs
vy=12  # vitesse dans la direction des y positifs

phrase="".join(lst)
police = pygame.font.Font("police.ttf", 128)
texte = police.render((phrase), True, (255, 255, 255))

raquette_x=30
raquette2_x=longueur-30
raquette_y=largeur/2
raquette2_y=largeur/2
raquette_h=100
raquette_l=20
deplacement=10
marge = 2*r

pygame.key.set_repeat(10, 10)

while True:
    screen.fill([0,0,0])
    lst=[s1," ",":"," ",s2]
    phrase="".join(lst)
    texte = police.render((phrase), True, (255, 255, 255))
    
    pygame.draw.circle(screen, couleur, [x,y], r, 0)
    pygame.draw.rect(screen, couleur, [raquette_x,raquette_y,raquette_l,raquette_h])
    pygame.draw.rect(screen, couleur, [raquette2_x,raquette2_y,raquette_l,raquette_h])
    
    screen.blit(texte,(longueur/2-130,30))
    
    x=x+vx
    y=y+vy
    
    #collision avec les murs
    if x+r > longueur:
        vx= -vx
        score1=score1+1
    if x-r < 0:
        vx= -vx
        score2=score2+1        
    if y+r > largeur:
        vy= -vy        
    if y-r < 0:
        vy= -vy
    s1=str(score1)
    s2=str(score2)   
    
    pygame.display.flip()
    pygame.time.delay(15)
    
    #collision entre le bord droit de la raquette de gauche (uniquement) et la balle (plus une marge)
    if x-r < raquette_x + raquette_l  and y > raquette_y - marge and y  < raquette_y + raquette_h + marge:
        vx = -vx
        
    #collision entre le bord gauche de la raquette de droite (uniquement) et la balle (plus une marge)
    if x + r > raquette2_x and y > raquette2_y - marge and y  < raquette2_y + raquette_h + marge:
        vx = -vx


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
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            