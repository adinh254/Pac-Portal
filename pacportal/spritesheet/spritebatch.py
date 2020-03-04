import pygame

def get_image_at( surface, rectangle ):
    image_area = pygame.Rect( rectangle )
    image = pygame.Surface( image_area.size ).convert()
    image.blit( surface, ( 0, 0 ), image_area )
    return image

def get_images_at( surface, rectangles ):
    return [ get_image_at( surface, rectangle ) for rectangle in rectangles ]

def get_sprite_batch( surface, rect, sprite_count ):
    sprite_areas = [ ( rect[0] + ( rect[2] * x ), rect[1], rect[2], rect[3] )
                      for x in range( sprite_count ) ]
    return get_images_at( surface, sprite_areas )
