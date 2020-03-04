import pygame
from pygame import math

import pacportal.spritesheet.spriteanimation

class PacMan(pygame.sprite.Sprite):
    def __init__( self, position, animation, speed ):
        super().__init__()
        self.box = animation.getCurrentFrame()
        self.position = position
        self.animation = animation
        self.speed = speed
        self.direction_vector = math.Vector2( 0.0, 0.0 )
        self.alive = True

    def move( self ):
        self.position.x += ( direction_vector.x * speed )
        self.position.y += ( direction_vector.y * speed )
        self.animation.setNextFrame()

    def changeDirection( self, velocity ):
        self.direction_vector = velocity.normalize()

    def render( self ):
        image = self.animation.getCurrentFrame()
        return image

