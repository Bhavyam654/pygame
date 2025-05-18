import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
s =  (0,0,200,75)
d = (400,0,200,75)
f = (400,525,200,75)
g = (0,525,200,75)
x=200
y=300
h = (x,y,200,75)

WIDTH = 600
HEIGHT = 600

FPS = 30
clock = pygame.time.Clock()
midas = pygame.draw.rect(screen,"gold",h) 

midas_dx = 0
midas_dy = 0



score = 0
speed = 10
gameloop = True
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    screen.fill("white")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            midas_dx = 0
            midas_dy = -1*speed
        elif event.key ==pygame.K_DOWN:
            midas_dx =0
            midas_dy = 1*speed
        elif event.key == pygame.K_RIGHT:
            midas_dx = 1*speed
            midas_dy = 0
        elif event.key == pygame.K_LEFT:
            midas_dx = -1*speed
            midas_dy = 0
    
    x = midas_dx + x
    y = midas_dy + y
    h = (x,y,200,75)
    c = "lime"
    b = pygame.draw.rect(screen,c,s)
    n = pygame.draw.rect(screen,c,d)
    m = pygame.draw.rect(screen,c,f)
    q = pygame.draw.rect(screen,c,g)
    midas = pygame.draw.rect(screen,"gold",h) 
    if midas.colliderect(b):
        b_color="gold"

    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()