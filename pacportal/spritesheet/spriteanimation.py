import pygame
from . import spritebatch

class SpriteAnimation:

    def __init__(self, surface, dimensions, sprite_count, loop=False, animation_frames=1):
        """Load Sprite Sheet"""
        self.sprites = spritebatch.get_sprite_batch( surface, dimensions, sprite_count )
        self.sprite_dimensions = dimensions
        self.sprite_iter = 0
        self.loop = loop
        self.animation_frames = animation_frames
        self.current_frame = animation_frames
        self.sprite_count = sprite_count

    def getSpriteBox(self):
        # Convert sprite to rectangle format
        sprite_box = pygame.Rect( 0, 0, self.sprite_dimensions[2], self.sprite_dimensions[3] )
        return sprite_box

    def resetFrames(self):
        self.sprite_iter = 0
        self.current_frame = animation_frames

    def setNextFrame(self):
       self.current_frame -= 1
       if self.current_frame == 0:
           self.sprite_iter += 1
           self.current_frame = self.animation_frames
       if ( self.sprite_iter >= self.sprite_count ):
           if not self.loop:
               return
           else:
               self.sprite_iter = 0

    def getCurrentFrame(self):
        image = self.sprites[ self.sprite_iter ]
        return image
