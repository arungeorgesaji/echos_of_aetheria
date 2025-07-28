import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, CAMERA_LERP_FACTOR

class Camera:
    def __init__(self, width, height):
        self.rect = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.offset_x = 0  
        self.offset_y = 0
    
    def update(self, target):
        target_x = target.rect.centerx - self.width // 2
        target_y = target.rect.centery - self.height // 2
        
        self.offset_x += (target_x - self.offset_x) * CAMERA_LERP_FACTOR
        self.offset_y += (target_y - self.offset_y) * CAMERA_LERP_FACTOR
    
    def apply(self, entity):
        return entity.rect.move(-self.offset_x, -self.offset_y)
    
    def apply_pos(self, pos):
        return (pos[0] - self.offset_x, pos[1] - self.offset_y)
