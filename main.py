import pygame
from paddle import Paddle 
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Brick Blaster")
gameloop = True 
paddle = Paddle()
FPS = 20
clock = pygame.time.Clock()
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    keys = pygame.key.get_pressed()
    paddle.move(keys)
    screen.fill("black")
    paddle.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
