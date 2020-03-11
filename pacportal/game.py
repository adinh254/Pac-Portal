from pathlib import Path

import pygame
import pytmx
from pytmx import load_pygame

from eventhandler import inputhandler, tilehandler
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

# Load map
base_path = Path(__file__).parent
file_path = ( base_path / "../resources/tilemap/" \
                          "default16x16/default16x16.tmx" ).resolve()
game_map = pytmx.load_pygame( file_path )

# Load all layers 
image_layer = game_map.get_layer_by_name( "default16x16" )
bg_image = game_map.get_tile_image_by_gid( image_layer.gid )

object_layer = game_map.get_layer_by_name( "Object Layer" )
collision_layer = game_map.get_layer_by_name( "Collision Layer" )

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

        player_tile = tilehandler.getTilePosFromVec( player.getPosition(), game_map.tilewidth )
        front_adjacent_tile = tilehandler.getFrontTilePos( player.getVelocity(), player_tile, game_map.tilewidth )

        # draw map data on screen
        for obj_tile in object_layer:
            if obj_tile.x == player_tile.x and obj_tile.y == player_tile.y:
                print( player_tile )
                print(player.getPosition() )
                print(( obj_tile.x, obj_tile.y) )
                obj_tile.visible = False
            if obj_tile.visible:
                obj_image = game_map.get_tile_image_by_gid( obj_tile.gid )
                screen.blit( obj_image, ( obj_tile.x, obj_tile.y ) )
               # if layer.visible:
               #     tile_image = game_map.get_tile_image_by_gid( gid )
               #     if ( tile_image ):
               #         screen.blit( tile_image, ( x * game_map.tilewidth, y * game_map.tileheight ) )
        player.move()
        screen.blit( bg_image, ( 0, 0 ) )
        screen.blit( player.render(), player.getPosition() )
        pygame.display.update()
        clock.tick( FPS )

if __name__ == '__main__':
    gameLoop()
    pygame.quit()
