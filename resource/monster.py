from pico2d import *
import random

class Monster:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(0, 1748), 800
        self.frame = 0
        if Monster.image == None:
            Monster.image = load_image('monster(191x224).png')
    def update(self):
        self.frame = random.randint(0, 5)
        if self.y > 330:
            self.y -= 50
        elif self.y < 330:
            self.y = 330
    def draw(self):
        self.image.clip_draw(self.frame * 191, 0, 191, 224, self.x, self.y)
