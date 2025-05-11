import pygame
import time
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
q = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
w = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
e = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
r = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
t = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
y = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
u = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
i = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
o = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))

p = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
a = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
s = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
d = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
f = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
g = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
h = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
j = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
k = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
l = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
z = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
x = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
c = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
v = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
b = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
n = (random.randint(0,800),random.randint(0,600),random.randint(10,60),random.randint(18,200))
player = (0,550,40,40)
player_dx = 0
player_dy = 550
PLAYER_SIZEX = 40
PLAYERSIZEY = 40
FPS = 20
clock = pygame.time.Clock()
gameloop = True
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_dx = player_dx + 30
            
            elif event.key == pygame.K_LEFT:
                player_dx = player_dx - 30              
            elif event.key == pygame.K_UP:  
                player_dy = player_dy - 30
            elif event.key == pygame.K_DOWN:
                player_dy = player_dy + 30
    playerposition = (player_dx,player_dy,PLAYER_SIZEX,PLAYERSIZEY)  
    player = pygame.draw.rect(screen,"white",playerposition)

    screen.fill("black")
    wall = pygame.draw.rect(screen,"red", q)
    wall2 = pygame.draw.rect(screen,"green", w)
    wall3 = pygame.draw.rect(screen,"pink", e)
    wall4 = pygame.draw.rect(screen,"green", r)
    wall5 = pygame.draw.rect(screen,"green", t)
    wall6 = pygame.draw.rect(screen,"red", y)
    wall7 = pygame.draw.rect(screen,"red", u)
    wall8 = pygame.draw.rect(screen,"purple", i)
    wall9 = pygame.draw.rect(screen,"purple", o)
    wall10 = pygame.draw.rect(screen,"purple", p)
    wall11 = pygame.draw.rect(screen,"purple", a)
    wall12 = pygame.draw.rect(screen,"purple", s)
    wall13 = pygame.draw.rect(screen,"purple", d)
    wall14 = pygame.draw.rect(screen,"purple", f)
    wall15 = pygame.draw.rect(screen,"purple", g)
    wall16 = pygame.draw.rect(screen,"purple", h)
    wall17 = pygame.draw.rect(screen,"purple", j)
    wall18 = pygame.draw.rect(screen,"purple", k)
    wall19 = pygame.draw.rect(screen,"purple", l)
    wall20 = pygame.draw.rect(screen,"purple", z)
    wall21 = pygame.draw.rect(screen,"purple", x)
    wall22 = pygame.draw.rect(screen,"purple", c)
    wall23 = pygame.draw.rect(screen,"purple", v)
    wall24 = pygame.draw.rect(screen,"purple", b)
    wall25 = pygame.draw.rect(screen,"purple", n)
    player =pygame.draw.rect(screen, "white", player)
    if player.colliderect(wall) or player.colliderect(wall2) or player.colliderect(wall3) or player.colliderect(wall4) or player.colliderect(wall5) or player.colliderect(wall6) or player.colliderect(wall7) or player.colliderect(wall8) or player.colliderect(wall9) or player.colliderect(wall10)or player.colliderect(wall11) or player.colliderect(wall12) or player.colliderect(wall13) or player.colliderect(wall14) or player.colliderect(wall15) or player.colliderect(wall16) or player.colliderect(wall17) or player.colliderect(wall18) or player.colliderect(wall19) or player.colliderect(wall20) or player.colliderect(wall21) or player.colliderect(wall21) or player.colliderect(wall22) or player.colliderect(wall23) or player.colliderect(wall24) or player.colliderect(wall25):
        gameloop = False
    clock.tick(FPS)
    pygame.display.flip()
