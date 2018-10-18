class Environ():
    def __init__(self, map, camera, player):
        self.map = map
        self.camera = camera
        self.player = player 

    def update(self):
        rects = self.map.get_blocks(self.player.rect.x, self.player.rect.y)
        print(["collide" for boolean in self.player.collide_list(rects) if boolean])
        
        self.map.update_map_position(self.camera)
