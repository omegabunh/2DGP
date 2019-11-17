from pico2d import *
import random

PIXEL_PER_METER = (10.0 / 0.3)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Monster:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(0, 1748), 800
        self.frame = 0

        if Monster.image == None:
            Monster.image = load_image('monster(191x224).png')

    def get_bb(self):
        return self.x - 100, self.y - 100, self.x + 100, self.y + 100

    def update(self):
        self.frame = random.randint(0, 5)
        if self.y > 330:
            self.y -= 50
        elif self.y < 330:
            self.y = 330

    def draw(self):
        draw_rectangle(*self.get_bb())
        self.image.clip_draw(self.frame * 191, 0, 191, 224, self.x, self.y)
