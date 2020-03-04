import pygame
from . import spritebatch

class SpriteAnimation:

    def __init__(self, surface, rectangle, sprite_count, loop=False, animation_frames=1):
        """Load Sprite Sheet"""
        sprites = spritebatch.get_sprite_batch( surface, rectangle, sprite_count )
        self.sprite_iter = 0
        self.loop = loop
        self.animation_frames = animation_frames
        self.current_frame = animation_frames

    def resetFrames(self):
        self.sprite_iter = 0
        self.current_frame = animation_frames

    def setNextFrame(self):
        if ( self.sprite_iter >= sprite_count ):
            if not self.loop:
                return
            else:
                self.sprite_iter = 0
        self.current_frame -= 1
        if self.current_frame == 0:
            self.sprite_iter += 1
            self.current_frame = animation_frames

    def getCurrentFrame(self):
        image = self.sprites[ self.sprite_iter ]
        return image
