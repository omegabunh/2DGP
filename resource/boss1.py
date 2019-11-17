from pico2d import *
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Boss:
    image = None
    hp_image = None

    def __init__(self):
        self.x, self.y = 1070, 470
        self.hp_x, self.hp_y = 1748 // 2, 920
        self.frame = 0

        if Boss.image is None:
            Boss.image = load_image('boss_phase1(248x245).png')

        if Boss.hp_image is None:
            Boss.hp_image = load_image('boss_hp.png')

    def get_bb(self):
        return self.x - 100, self.y - 100, self.x + 100, self.y + 100

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(self):
        self.image.clip_draw(int(self.frame) * 248, 0, 248, 245, self.x, self.y)
        draw_rectangle(*self.get_bb())
        self.hp_image.draw_now(self.hp_x, self.hp_y)


