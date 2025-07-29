import pygame
import pytmx
from settings import *
from camera import Camera
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TMX Loader")

    tmx_data = pytmx.load_pygame("assets/Tileset/grassy.tmx")  
    player = Player(16 * tmx_data.tilewidth, 16 * tmx_data.tileheight)  
    camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT, tmx_data)
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        player.update(camera)  
        camera.update(player)
        
        screen.fill((0, 0, 0))  
        
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        screen.blit(tile, camera.apply_rect(pygame.Rect(
                            x * tmx_data.tilewidth,
                            y * tmx_data.tileheight,
                            tmx_data.tilewidth,
                            tmx_data.tileheight
                        )))
        
        screen.blit(player.image, camera.apply(player))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
