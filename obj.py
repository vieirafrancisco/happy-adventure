import pygame

class Object:
    
    def __init__(self, master, pos_x, pos_y, width, height, color=None, image_root=None):
        self.master = master
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

        self.image = pygame.image.load(image_root) if image_root else pygame.Surface((self.width, self.height))
        self.image.fill(color if color else pygame.Color('white'))
        self.rect = self.image.get_rect()

    def draw(self):
        self.master.blit(self.image, (self.pos_x, self.pos_y))
