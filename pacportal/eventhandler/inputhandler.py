from pygame.math import Vector2
from pygame.locals import *

def getVector( input_key ):
    if input_key == K_UP:
        return Vector2( 0 , 1 )
    elif input_key == K_DOWN:
        return Vector2( 0, -1 )
    elif input_key == K_RIGHT:
        return Vector2( 1, 0 )
    elif input_key == K_LEFT:
        return Vector2( -1, 0 )
