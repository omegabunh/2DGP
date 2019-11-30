from pico2d import *


class Key:
    def __init__(self):
        self.image = load_image('sprite//key.PNG')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1700, 50)
