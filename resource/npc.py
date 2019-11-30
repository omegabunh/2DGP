from pico2d import *
class Npc:
    image = None
    def __init__(self):
        self.x, self.y = 1200, 182
        self.font = load_font('Maplestory Bold.ttf', 16)
        if Npc.image is None:
            Npc.image = load_image('sprite//npc.png')

    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x, self.y)