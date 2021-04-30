import pygame
import sys
import pygame.key

pygame.init()

longueur=1000
largeur=666
couleur=[255,255,255]

screen = pygame.display.set_mode([longueur,largeur])

screen.fill([0,0,0])

x=500
y=333
r=20
X=8
Y=12

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
    pygame.draw.circle(screen, couleur, [x,y], r, 0)
    pygame.draw.rect(screen, couleur, [rx,ry,rl,rh])
    pygame.draw.rect(screen, couleur, [r2x,r2y,rl,rh])
    x=x+X
    y=y+Y
    if x+r > longueur:
        X= -X
    if x-r < 0:
        X= -X
    if y+r > largeur:
        Y= -Y
    if y-r < 0:
        Y= -Y
    pygame.display.flip()
    pygame.time.delay(10)
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
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            