import pygame
from settings import * 

class Camera:
    def __init__(self, width, height, tmx_data=None):
        self.rect = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.offset_x = 0
        self.offset_y = 0
        self.tmx_data = tmx_data  
        
    def apply(self, entity):
        return entity.rect.move(-self.offset_x, -self.offset_y)
    
    def apply_rect(self, rect):
        return rect.move(-self.offset_x, -self.offset_y)
    
    def update(self, target):
        target_x = target.rect.centerx - self.width // 2
        target_y = target.rect.centery - self.height // 2
        
        if self.tmx_data:
            max_x = self.tmx_data.width * self.tmx_data.tilewidth - self.width
            max_y = self.tmx_data.height * self.tmx_data.tileheight - self.height
            target_x = max(0, min(target_x, max_x))
            target_y = max(0, min(target_y, max_y))
        
        self.offset_x += (target_x - self.offset_x) * CAMERA_LERP_FACTOR
        self.offset_y += (target_y - self.offset_y) * CAMERA_LERP_FACTOR
        self.rect.x = int(self.offset_x)
        self.rect.y = int(self.offset_y)
