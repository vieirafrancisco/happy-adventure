import pygame
from random import choice
from pygame.locals import *

from .pysurface import Canvas

def set_key_pressed_events():
    keys = pygame.key.get_pressed()
    for cont in range(len(keys)):
        if keys[cont]:
            pygame.event.post(pygame.event.Event(31, key=cont))

class App():
    def __init__(self, name, fps, width, height, debug = False):
        self._running = False
        self.screen_width = width
        self.screen_height = height

        self._display = None
        self.time_event = pygame.event.Event(30, time = 0, fps = fps, count_fps = 0)

    def add_events_queue(self):
        pygame.event.post(self.time_event)

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            set_key_pressed_events()
            self.add_events_queue()
            for event in pygame.event.get():
                self.on_event(event)
            self._display.fill((0,145,0))
            self.on_loop()
            self.on_render()
            self.tick()

        self.on_cleanup()

    def on_init(self):
        pygame.init()
        pygame.display.set_mode((self.screen_width, self.screen_height), pygame.HWSURFACE | pygame.DOUBLEBUF)

        self._display = Canvas(width = self.screen_width, height = self.screen_height)
        self._display.pack(0, 0)

        self.screen = pygame.display.get_surface()
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        else:
            self._display.event_call(event)

    def on_loop(self):
        pass
        
    def on_render(self):
        self._display.update()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def tick(self):
        time_event = self.time_event
        time_event.count_fps += 1
        if time_event.count_fps % time_event.fps == 0:
            time_event.time += 1
            time_event.count_fps = 0
        
        pygame.time.Clock().tick(time_event.fps)

    
if __name__ == "__main__":
    app = App("teste", 800, 600)
    app.run()