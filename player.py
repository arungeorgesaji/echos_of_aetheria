import pygame
import pytmx
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))  
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = PLAYER_SPEED
        self.velocity = [0, 0]  
        self.prev_pos = self.rect.copy()
    
    def update(self, camera=None):
        self.velocity = [0, 0]  
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.velocity[0] = -self.speed
        if keys[pygame.K_RIGHT]: self.velocity[0] = self.speed
        if keys[pygame.K_UP]: self.velocity[1] = -self.speed
        if keys[pygame.K_DOWN]: self.velocity[1] = self.speed
        
        self.prev_pos = self.rect.copy()
        
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if camera:
            self._clamp_to_camera(camera)
    
    def _clamp_to_camera(self, camera):
        if self.rect.left < camera.rect.left:
            self.rect.left = camera.rect.left

        if self.rect.right > camera.rect.right:
            self.rect.right = camera.rect.right

        if self.rect.top < camera.rect.top:
            self.rect.top = camera.rect.top

        if self.rect.bottom > camera.rect.bottom:
            self.rect.bottom = camera.rect.bottom

