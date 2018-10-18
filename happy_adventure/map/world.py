import pygame
from ..pygame_api.pysurface import Canvas

class Camera():
    def __init__(self, player):
        self.map = map
        self.player = player

    @property
    def pos(self):
        return 350 - self.player.posX ,250 - self.player.posY
    
class MazeMap(Canvas):
    def __init__(self, map_size,display_canvas, block_size, block_matrix, objects_dict):
        self.camera = None
        self.display_canvas = display_canvas
        self.block_size = block_size
        self.block_matrix = block_matrix
        self._objects_dict = objects_dict

        super().__init__(width = map_size[0],height = map_size[1], master = display_canvas)

    def get_blocks(self, posX, posY):
        rect_list = []
        x_index = posX // self.block_size[0]
        y_index = posY // self.block_size[1]

        for cont in range(x_index-1, x_index+2):
            for cont2 in range(y_index-1, y_index + 2):
                if self.block_matrix[cont2][cont] == "ground":
                    rect_list.append(pygame.rect.Rect(cont*100, cont2*100, 100, 100))
           
        return rect_list

    def build(self):
        for row in range(len(self.block_matrix)):
            for col in range(len(self.block_matrix[row])):
                object_name = self.block_matrix[row][col]
                object_surface = self._objects_dict[object_name]
                object_pos = self.block_size[0]*col, self.block_size[1]*row
                self.blit(object_surface, object_pos)

    def update_map_position(self, camera):
        self.posX, self.posY = self.camera.pos
    