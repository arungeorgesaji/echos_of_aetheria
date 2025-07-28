import pygame
from settings import TILE_SIZE, PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x * TILE_SIZE, y * TILE_SIZE))
        self.speed = PLAYER_SPEED
        self.velocity = [0, 0]  
    
    def update(self):
        self.velocity = [0, 0]  
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.velocity[0] = -self.speed
        if keys[pygame.K_RIGHT]: self.velocity[0] = self.speed
        if keys[pygame.K_UP]: self.velocity[1] = -self.speed
        if keys[pygame.K_DOWN]: self.velocity[1] = self.speed
        
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
