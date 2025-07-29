import pygame
from settings import *

class Tilemap:
    def __init__(self, filename):
        self.tile_size = TILE_SIZE
        self.tiles = []
        self.load_map(filename)
        self.width = len(self.tiles[0]) * self.tile_size if self.tiles else 0
        self.height = len(self.tiles) * self.tile_size if self.tiles else 0
        
    def load_map(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        self.tiles.append(list(map(int, line.split(','))))
        except FileNotFoundError:
            self.tiles = [[0 for _ in range(50)] for _ in range(50)]
            
    def render(self, surface, camera):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                if tile != 0:  e
                    rect = pygame.Rect(
                        x * self.tile_size, 
                        y * self.tile_size, 
                        self.tile_size, 
                        self.tile_size
                    )
                    if camera.rect.colliderect(rect):
                        screen_pos = camera.apply_rect(rect)
                        color = (100, 100, 100) if tile == 1 else (200, 200, 0)
                        pygame.draw.rect(surface, color, screen_pos)
