import pytmx
from pygame.math import Vector2

def getTilePosFromVec( vec, tile_size ):
    return Vector2(
                    vec.x - ( vec.x % tile_size ),
                    vec.y - ( vec.y % tile_size ),
                  )

def getFrontTilePos( vec, tile_pos, tile_size ):
    if vec.magnitude_squared() != 0:
        direction = vec.normalize()
        return Vector2(
                        tile_pos + ( direction * tile_size ),
                        tile_pos + ( direction * tile_size ),
                      )
    else:
        return

def isCollided( entity_rect, tile_rect ):
    if ( entity_rect.x >= ( tile_rect.x + tile_rect.width ) ):
            return False
    if ( ( entity_rect.x + entity_rect.width ) <= tile_rect.x ):
            return False
    if ( entity_rect.y >= ( tile_rect.y + tile_rect.height ) ):
            return False
    if ( ( entity_rect.y + entity_rect.height ) <= tile_rect.y ):
            return False
    return True
