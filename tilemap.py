import pygame
from settings import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

def load_tilemap(tileset, tile_size, cols, rows):
    tiles = []
    for y in range(rows):
        for x in range(cols):
            rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
            tiles.append(tileset.subsurface(rect))
    return tiles

def render_tilemap(surface, tilemap, tiles, camera_offset=(0, 0)):
    for y, row in enumerate(tilemap):
        for x, tile_index in enumerate(row):
            if 0 <= tile_index < len(tiles):
                screen_x = x * TILE_SIZE - camera_offset[0]
                screen_y = y * TILE_SIZE - camera_offset[1]
                
                if (-TILE_SIZE < screen_x < SCREEN_WIDTH and 
                    -TILE_SIZE < screen_y < SCREEN_HEIGHT):
                    surface.blit(tiles[tile_index], (screen_x, screen_y))
