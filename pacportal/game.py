from pathlib import Path

import pygame
import pytmx
from pytmx import load_pygame

from eventhandler import inputhandler
from entity.pacman import PacMan
from spritesheet.spriteanimation import SpriteAnimation

pygame.init()

SCREEN_WIDTH = 448
SCREEN_HEIGHT = 576

screen = pygame.display.set_mode( ( SCREEN_WIDTH, SCREEN_HEIGHT ) )
pygame.display.set_caption( 'Pac-Portal' )
clock = pygame.time.Clock()

# load map
base_path = Path(__file__).parent
file_path = ( base_path / "../resources/tilemap/" \
                          "default16x16/default16x16.tmx" ).resolve()
game_map = pytmx.load_pygame( file_path )
print( ( base_path / "../assets/atlas/pacman_animate.png" ).resolve() )

pacman_sprites = pygame.image.load( str( ( base_path / "../assets/atlas/pacman_animate.png" ).resolve() ) )

loaded_animations = [ SpriteAnimation( pacman_sprites, ( 0, 0, 16, 16 ), 3, True, 12 ) ]

# Pacman moves at 11 tiles per second ( 176px per second )
player = PacMan( ( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 ), loaded_animations[0], 11 )

def gameLoop():
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            # if event.type == pygame.KEYDOWN:
                # TODO: Input handling
            if event.type == pygame.QUIT:
                game_exit = True
        # draw map data on screen
        for layer in game_map.visible_layers:
            if ( isinstance( layer, pytmx.TiledTileLayer ) ):
                for x, y, gid, in layer:
                    tile = game_map.get_tile_image_by_gid( gid )
                    if ( tile ):
                        tile.convert()
                        screen.blit( tile, ( x * game_map.tilewidth, y * game_map.tileheight ) )
            elif ( isinstance( layer, pytmx.TiledImageLayer ) ):
                image = game_map.get_tile_image_by_gid( layer.gid )
                if ( image ):
                    image.convert()
                    screen.blit( image, ( 0, 0 ) )
        screen.blit( player.render(), ( 0, 0 ) )
        pygame.display.update()
        clock.tick( 30 )

if __name__ == '__main__':
    gameLoop()
    pygame.quit()
