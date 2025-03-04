import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
s =  (200,100,40,250)
d = (200,100,100,40)
f = (301,140,40,60)
g = (200,200,101,40)
h = (300,240,40,110)
j = (200,350,100,40)
gameloop = True
gameloop = True
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    screen.fill("white")
    b = pygame.draw.rect(screen,"lime",s)
    n = pygame.draw.rect(screen,"lime",d)
    m = pygame.draw.rect(screen,"lime",f)
    q = pygame.draw.rect(screen,"lime",g)
    w = pygame.draw.rect(screen,"lime",h)
    e = pygame.draw.rect(screen,"lime",j)
    pygame.display.flip()
pygame.quit()