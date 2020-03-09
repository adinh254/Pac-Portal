from pathlib import Path

import pygame
import pytmx
from pytmx import load_pygame

from eventhandler import inputhandler
from entity.pacman import PacMan
from spritesheet.spriteanimation import SpriteAnimation
from pygame.math import Vector2

pygame.init()

SCREEN_WIDTH = 448
SCREEN_HEIGHT = 576
FPS = 60

screen = pygame.display.set_mode( ( SCREEN_WIDTH, SCREEN_HEIGHT ) )
pygame.display.set_caption( 'Pac-Portal' )
clock = pygame.time.Clock()

# load map
base_path = Path(__file__).parent
file_path = ( base_path / "../resources/tilemap/" \
                          "default16x16/default16x16.tmx" ).resolve()
game_map = pytmx.load_pygame( file_path )
print( ( base_path / "../assets/atlas/pacman_animate.png" ).resolve() )

pacman_sprites = pygame.image.load( str( ( base_path / "../assets/atlas/pacman_animate.png" ).resolve() ) ).convert_alpha()

loaded_animations = [ SpriteAnimation( pacman_sprites, ( 0, 0, 28, 28 ), 3, True, 3 ) ]

# Pacman moves at 10 tiles per second ( 160px per second )
player = PacMan( Vector2( SCREEN_WIDTH / 2, 16 * 26.5 ), loaded_animations[0], ( 10 * 16 ) / FPS )

def gameLoop():
    game_exit = False
    while not game_exit:
        screen.fill( ( 0, 0, 0 ) )
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
               key_event =  inputhandler.processKey( event.key )
               if key_event is not None:
                   player.changeDirection( key_event )
            if event.type == pygame.QUIT:
                game_exit = True
        # draw map data on screen
        player.move()
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
        screen.blit( player.render(), player.getPosition() )
        pygame.display.update()
        clock.tick( FPS )

if __name__ == '__main__':
    gameLoop()
    pygame.quit()
