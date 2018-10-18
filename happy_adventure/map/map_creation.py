import pygame
import numpy as np

from ..settings import IMAGES_PATH
from .world import MazeMap
from .map_generation import generate_map


def build_environment_matrix(shape, objects_graph):
    matrix_objects = np.empty(shape, dtype = object)
    matrix = generate_map(shape, 400, 20)

    for cont in range(len(matrix)):
        for cont2 in range(len(matrix[cont])):
            if matrix[cont][cont2] == 0:
                matrix[cont][cont2] = "ground"
            elif matrix[cont][cont2] == 1:
                matrix[cont][cont2] = "grass"

    return matrix

def build_maze_map(display_surface, shape):
    grass_object = pygame.image.load(IMAGES_PATH+"grass.jpg")
    ground_object = pygame.image.load(IMAGES_PATH+"new_ground.jpg")
    water_object = pygame.image.load(IMAGES_PATH+"water.png")
    objects_dict = {
        "grass": grass_object,
        "ground": ground_object,
        "water": water_object,
    }

    environment_matrix = build_environment_matrix(shape, None) 
    return MazeMap((100*shape[0],100*shape[1]), display_surface, (100,100), 
                    environment_matrix, objects_dict)