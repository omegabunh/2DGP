from pico2d import *

class Map:
    def __init__(self):
        self.image = load_image('sprite//map3.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(2050 // 2, 1550 // 2)