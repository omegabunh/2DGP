from pico2d import *
import random
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Horn:
    image = None
    spacebar = None
    spacebar_fill = None
    def __init__(self):
        if Horn.image == None:
            Horn.image = load_image('horn(304x244).png')
        if Horn.spacebar == None:
            Horn.spacebar = load_image('KeyDownBar.png')
        if Horn.spacebar_fill == None:
            Horn.spacebar_fill = load_image('KeyDownBar2.png')
        self.x, self.y = 1400, 650
        self.bar_x, self.bar_y = 1430, 730
        self.bar_x1, self.bar_y1 = 1397, 730
        self.w, self.h = 0, 8
        self.frame = 0
        self.hit = 0
        self.font = load_font('ENCR10B.TTF', 16)
        self.deadstate = False
        self.hitstate = False
        self.hit_count = 0

    def get_bb(self):
        return self.x - 100, self.y - 120, self.x + 100, self.y + 100

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

    def draw(self):
        draw_rectangle(*self.get_bb())
        self.image.clip_draw(int(self.frame) * 304, 0, 304, 244, self.x, self.y)
        self.spacebar.draw(self.bar_x, self.bar_y)
        self.spacebar_fill.draw(self.bar_x1, self.bar_y1, self.w, self.h)
