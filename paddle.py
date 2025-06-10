import pygame 
class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(400,580,100,10)
        self.velocity = 10
    def move(self,keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.velocity
    def draw(self,screen):
        pygame.draw.rect(screen,"red", self.rect)