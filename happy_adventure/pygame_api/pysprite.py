from pygame import mask
from .pysurface import Canvas

class Sprite(Canvas):
    def __init__(self, master, surface = None, **surf_kwargs):
        super().__init__(master, surface, **surf_kwargs)
        self.mask = mask.from_surface(self)

    def move(self ,x, y):
        self.posX = self.posX + x
        self.posY = self.posY + y
    
    def collide(self, sprite):
        rect_x = self.get_rect()
        rect_y = sprite.get_rect()
        offset_x = rect_x[0] - rect_y[0]
        offset_y = rect_x[1] - rect_y[1]
        if self.mask.overlap(sprite.mask, (offset_x,offset_y)):
            return True
        else:
            return False
    
    def collidelist(self, sprite_list):
        for sprite in sprite_list:
            yield self.collide(sprite)