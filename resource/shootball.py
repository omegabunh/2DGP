import random
from pico2d import *
import game_world
import game_framework


class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('Shootball0.png')
        self.x, self.y = random.randint(1, 1280 - 1), random.randint(1, 1024 - 1)
        self.hp = 100

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass
