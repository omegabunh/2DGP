from pico2d import *
class Npc:
    image_n = None
    def __init__(self):
        self.x, self.y = 1200, 182
        if Npc.image_n == None:
            Npc.image_n = load_image('npc.png')

    def update(self):
        pass
    def draw(self):
        self.image_n.draw(self.x, self.y)