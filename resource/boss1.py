from pico2d import *
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3


class Boss:
    image = None
    hp_image = None
    attack_image = None

    def __init__(self):
        self.x, self.y = 1070, 470
        self.hp_x, self.hp_y = 1748 // 2, 920
        self.frame = 0
        self.frame1 = 0
        self.hp = 1000
        self.count = 0
        self.font = load_font('ENCR10B.TTF', 16)

        if Boss.image is None:
            #Boss.image = load_image('boss_phase1(248x245).png')
            Boss.image = load_image('boss1(320x410).png')
        if Boss.attack_image is None:
            Boss.attack_image = load_image('boss1_attack(340x420).png')
        if Boss.hp_image is None:
            Boss.hp_image = load_image('boss_hp.png')

    def get_bb(self):
        return self.x - 100, self.y - 100, self.x + 100, self.y + 100

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 15

    def draw(self):
        self.font.draw(self.x - 60, self.y + 150, '(hp: %0.0f)' % self.hp, (255, 255, 0))

        if 690 < self.hp < 700:
            self.attack_image.clip_draw(int(self.frame) * 340, 0, 340, 420, self.x, self.y)
        else:
            self.image.clip_draw(int(self.frame) * 320, 0, 320, 410, self.x, self.y)
        draw_rectangle(*self.get_bb())
        self.hp_image.draw_now(self.hp_x, self.hp_y)
