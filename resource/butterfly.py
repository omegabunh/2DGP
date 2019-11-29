from pico2d import *
import random
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Butterfly:
    image = None

    def __init__(self):
        if Butterfly.image == None:
            Butterfly.image = load_image('butterfly(92x112).png')
        self.x, self.y = random.randint(100, 1748), random.randint(100, 800)
        self.frame = random.randint(0, 5)
        self.hit = 0
        self.font = load_font('ENCR10B.TTF', 16)
        self.deadstate = False
        self.hitstate = False
        self.hit_count = 0

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 40, self.y + 50

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

    def draw(self):
        draw_rectangle(*self.get_bb())
        self.image.clip_draw(int(self.frame) * 92, 0, 92, 112, self.x, self.y)
