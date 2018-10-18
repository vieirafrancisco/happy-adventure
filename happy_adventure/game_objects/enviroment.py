class Environ():
    def __init__(self, map, camera, player):
        self.map = map
        self.camera = camera
        self.player = player 

    def update(self):
        rects = self.map.get_blocks(self.player.rect.x, self.player.rect.y)
        collides = [boolean for boolean in self.player.collide_list(rects) if boolean]
        print(collides)
        if len(collides) > 0 :
            if 1 not in self.player.collide_direction:
                self.player.collide_direction[self.player.sprite_animation.section] = 1
        else:
            self.player.collide_direction = [0, 0, 0, 0]
        
        self.map.update_map_position(self.camera)