from ..pygame_api.pyapp import App
from ..settings import IMAGES_PATH

from ..game_objects.player import Character
from ..game_objects.enviroment import Environ

from ..map.world import Camera
from ..map.map_creation import build_maze_map


class GameApp(App):
    def __init__(name, fps, width, height, debug = False):
        App.__init__(name, fps, width, height, debug)
    
    def on_init(self):
        super().on_init()

        world = build_maze_map(self._display, (100,100))
        world.build()
        world.pack(0,0)

        player = Character(self._display, IMAGES_PATH+"player.png", 4, 9)
        player.pack(8*64,7*64)

        camera = Camera(player)
        world.camera = camera

        self.environ = Environ(world, camera, player)

    def on_loop(self):
        self.environ.update()
