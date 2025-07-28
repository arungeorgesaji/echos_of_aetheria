import pygame
from settings import *
from camera import Camera
from player import Player
from tilemap import load_tilemap, render_tilemap

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    tileset = pygame.image.load("assets/Tileset/tileset.png").convert_alpha()
    tiles = load_tilemap(tileset, TILE_SIZE, 8, 8)
    
    player = Player(5, 5)
    camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    tilemap = [
        [0, 1, 1, 1, 0],
        [0, 1, 2, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        player.update()
        camera.update(player)
        
        screen.fill((0, 0, 0))
        render_tilemap(screen, tilemap, tiles, (camera.offset_x, camera.offset_y))
        screen.blit(player.image, camera.apply(player))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
