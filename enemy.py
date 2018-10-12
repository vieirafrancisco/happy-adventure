from obj import Object

class Enemy(Object):

    def __init__(self, master, pos_x, pos_y, width, height, image_root=None):
        super().__init__(master, pos_x, pos_y, width, height, image_root)