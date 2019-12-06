from pico2d import *
import random
import game_world
import game_framework
import map3
import main2_state

PIXEL_PER_METER = (10.0 / 0.3)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Horn:
    image = None
    spacebar = None
    spacebar_fill = None

    def __init__(self):
        if Horn.image is None:
            Horn.image = load_image('sprite//horn(304x244).png')
        if Horn.spacebar is None:
            Horn.spacebar = load_image('sprite//KeyDownBar.png')
        if Horn.spacebar_fill is None:
            Horn.spacebar_fill = load_image('sprite//KeyDownBar2.png')
        self.w, self.h = 0, 8

        self.frame = 0
        self.hit = 0
        self.font = load_font('Maplestory Bold.ttf', 16)
        self.deadstate = False
        self.hitstate = False
        self.hit_count = 0

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2
        self.bar_x, self.bar_y = self.bg.w / 2, self.bg.h / 2
        self.bar_x1, self.bar_y1 = self.bg.w / 2, self.bg.h / 2

    def get_bb(self):
        cx, cy = self.x - self.bg.window_left + 526, self.y - self.bg.window_bottom + 175
        return cx - 100, cy - 120, cx + 100, cy + 100

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

    def draw(self):
        cx, cy = self.x - self.bg.window_left + 526, self.y - self.bg.window_bottom + 175
        cx1, cy1 = self.bar_x - self.bg.window_left + 556, self.bar_y - self.bg.window_bottom + 255
        cx2, cy2 = self.bar_x1 - self.bg.window_left + 523, self.bar_y1 - self.bg.window_bottom + 255

        if main2_state.boss.hp <= 900:
            self.font.draw(cx - 20, cy + 120, 'PRESS SPACE', (255, 0, 0))
            self.spacebar.draw(cx1, cy1+30)
            self.spacebar_fill.draw(cx2, cy2+30, self.w, self.h)
        self.image.clip_draw(int(self.frame) * 304, 0, 304, 244, cx, cy)
        #draw_rectangle(*self.get_bb())

