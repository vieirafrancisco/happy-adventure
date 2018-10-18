import pygame
from .pysurface import Canvas

class Sprite(Canvas):
    def __init__(self, master, surface = None, **surf_kwargs):
        super().__init__(master, surface, **surf_kwargs)
        self.mask = pygame.mask.from_surface(self)
        self.rect = self.get_rect()

    def move(self ,x, y):
        self.posX = self.posX + x
        self.posY = self.posY + y
    
    def collide_with(self, obj):
        if isinstance(obj, pygame.rect.Rect):
            return self.rect.colliderect(obj)
        else:
            rect_x = self.get_rect()
            rect_y = obj.get_rect()
            offset_x = rect_x[0] - rect_y[0]
            offset_y = rect_x[1] - rect_y[1]
            if self.mask.overlap(obj.mask, (offset_x,offset_y)):
                return True
            else:
                return False
    
    def collide_list(self, objects):
        for obj in objects:
            yield self.collide_with(obj)
    