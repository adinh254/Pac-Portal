import pygame
from pygame.math import Vector2

import pacportal.spritesheet.spriteanimation

class PacMan(pygame.sprite.Sprite):
    def __init__( self, position, animation, speed ):
        super().__init__()
        self.box = animation.getSpriteBox()
        self.box.center = ( self.box.width / 2, self.box.height / 2 )
        self.position = Vector2( position )
        self.animation = animation
        self.speed = speed
        self.direction_vector = Vector2( 0, 0 )
        self.queued_vector = Vector2( 0, 0 )
        self.velocity = Vector2( 0, 0 )
        self.orientation = 0

    def move( self ):
        if self.direction_vector.magnitude_squared() != 0:
            self.position.x += ( self.direction_vector.x * self.speed )
            self.position.y += ( self.direction_vector.y * self.speed )

            self.animation.setNextFrame()

    def changeDirection( self, velocity ):
        # Normalize vector if magnitude is greater than 1
        input_direction = velocity.normalize()

        if input_direction.magnitude_squared() != 0.0:
            # If pacman is not moving
            if self.direction_vector.magnitude_squared() == 0.0:
                if input_direction.x < 0:
                    rotation_angle = 180
                elif input_direction.y != 0:
                    rotation_angle = input_direction.y * -90
                else:
                    rotation_angle = 0
                self.orientation = rotation_angle % 360
                self.direction_vector = input_direction
            # Allows pacman to always turn around in place
            elif self.direction_vector.dot( input_direction ) < 0:
                self.orientation = (self.orientation + 180 ) % 360
                self.direction_vector = input_direction
                self.queued_vector = Vector2( 0, 0 )
            # Queued direction vector
            # TODO: If in a direction tile execute queued vector
            else:
                # rotation_angle = self.direction_vector.cross( input_direction ) * -90
                # self.orientation = ( self.orientation + rotation_angle ) % 360
                self.queued_vector = input_direction
        else:
            self.direction_vector = input_direction

    def getVelocity( self ):
        return self.velocity

    def render( self ):
        image = self.animation.getCurrentFrame()
        oriented_image = pygame.transform.rotate( image, self.orientation )
        return oriented_image

    def getPosition( self ):
        offset = Vector2( self.box.center )
        position = Vector2( self.position.x - offset.x, self.position.y - offset.y )
        return position
