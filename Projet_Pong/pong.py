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

x=500
y=333
r=20
X=8
Y=12

phrase="".join(lst)
police = pygame.font.Font("police.ttf", 128)
texte = police.render((phrase), True, (255, 255, 255))

rx=30
r2x=longueur-30
ry=largeur/2
r2y=largeur/2
dry=5
rh=100
rl=20
d=10
pygame.key.set_repeat(10, 10)
while True:
    screen.fill([0,0,0])
    s1=str(score1)
    s2=str(score2)
    lst=[s1," ",":"," ",s2]
    texte = police.render((phrase), True, (255, 255, 255))
    pygame.draw.circle(screen, couleur, [x,y], r, 0)
    pygame.draw.rect(screen, couleur, [rx,ry,rl,rh])
    pygame.draw.rect(screen, couleur, [r2x,r2y,rl,rh])
    screen.blit(texte,(longueur/2-130,30))
    x=x+X
    y=y+Y
    if x+r > longueur:
        X= -X
        score1+=1
    if x-r < 0:
        X= -X
        score2+=1
    if y+r > largeur:
        Y= -Y
    if y-r < 0:
        Y= -Y
    pygame.display.flip()
    pygame.time.delay(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_w]:
                if ry>0:
                    ry=ry-d
            if pygame.key.get_pressed()[pygame.K_s]:
                if ry+rh<largeur:
                    ry=ry+d
            if pygame.key.get_pressed()[pygame.K_UP]:
                if r2y>0:
                    r2y=r2y-d
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                if r2y+rh<largeur:
                    r2y=r2y+d
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            