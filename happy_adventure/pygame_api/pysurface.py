import pygame
from pygame import Surface,surfarray
from .pyevent import Events

class Canvas(Surface,Events):
    def __init__(self, master = None, surface = None, **surf_kwargs):     
        self.children = []

        if not surface:
            self._build_surface(**surf_kwargs)
        else:
            surf_rect = surface.get_rect()
            Surface.__init__(surf_rect.size, masks = pygame.mask.from_surface(surface))
            array = surfarray.array2d(surface)
            surfarray.blit_array(self, array)

        if not master:
            self.master = pygame.display.get_surface()
        else:
            self.master = master

        Events.__init__(self)

    def _build_surface(self, width, height, flags=pygame.SRCALPHA, depth=32):
        Surface.__init__(self,(width,height), flags, depth)

    def add_child(self, canvas):
        self.children.append(canvas)

    def pack(self, posX, posY):
        self.posX, self.posY = posX, posY
        if isinstance(self.master, Canvas):
            self.master.add_child(self)

    def update(self):
        self.update_children()
        
        if self.has_change():
            self.draw()
        

    def update_children(self):
        for child in self.children:
            child.update()

    def draw(self):
        self.master.blit(self, (self.posX,self.posY))

    def has_change(self):
        return True

    def event_call(self, event):
        if event.type in self.dict_events:
            self.dict_events[event.type](event)

        for child in self.children:
            child.event_call(event)
        

