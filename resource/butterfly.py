from pico2d import *
import random
import game_world
import game_framework
from bullet import Bullet

PIXEL_PER_METER = (10.0 / 0.3)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

bullet = None
t = 0
i = 0
r = 1

class Butterfly:
    image = None

    def __init__(self):
        if Butterfly.image == None:
            Butterfly.image = load_image('sprite//butterfly(92x112).png')
        self.x, self.y = random.randint(100, 1748), random.randint(100, 800)
        self.frame = random.randint(0, 5)
        self.speed = 2
        self.bullet_count = 0
        self.r = 5
        self.bullet_draw_time = 0

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 40, self.y + 50

    def update(self):
        global t, i, r
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.bullet_draw_time += 0.01
        i += 1
        t = i / 100
        if (i > 101):
            r = (r + 1) % 10
            i = 0
        if self.bullet_draw_time > 2.0:
            while self.bullet_count < 360:
                self.bullet_count += 30
                bullets = Bullet(self.x, self.y, 5, self.bullet_count)
                game_world.add_object(bullets, 1)
            self.bullet_draw_time = 0
            self.bullet_count = 0

    def draw(self):
        draw_rectangle(*self.get_bb())
        self.image.clip_draw(int(self.frame) * 92, 0, 92, 112, self.x, self.y)