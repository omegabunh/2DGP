from pico2d import *
class Npc:
    image = None
    def __init__(self):
        self.x, self.y = 1200, 182
        if Npc.image == None:
            Npc.image = load_image('npc.png')

    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x, self.y)