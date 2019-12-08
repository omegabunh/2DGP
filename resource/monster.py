from pico2d import *
import random
import game_world
import game_framework
import main_state

PIXEL_PER_METER = (10.0 / 0.3)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Monster:
    image = None

    def __init__(self):
        if Monster.image == None:
            Monster.image = load_image('sprite//monster(191x224).png')
        self.x, self.y = random.randint(800, 1200), 1100
        self.frame = random.randint(0, 5)
        self.hit = 0
        self.font = load_font('ENCR10B.TTF', 16)
        self.deadstate = False
        self.hitstate = False
        self.hit_count = 0
        self.op_count = 0

    def get_bb(self):
        return self.x - 80, self.y - 100, self.x + 80, self.y + 100

    def update(self):
        #self.frame = random.randint(0, 5)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        if 495 <= main_state.boss.hp <= 500 and main_state.boss.hp != 0:
            if self.y > 330:
                self.y -= 10
            elif self.y < 330:
                self.y = 330
        if self.hit >= 300:
            self.deadstate = True
        if self.hitstate == True:
            self.op_count += 1
            self.image.opacify(0.8)
            if self.op_count % 50:
                self.image.opacify(1.0)
            if self.op_count == 150:
                self.hitstate = False
                self.op_count = 0

    def draw(self):
        #self.font.draw(self.x - 60, self.y + 70, '(hit: %0.0f)' % self.hit, (0, 255, 0))
        #draw_rectangle(*self.get_bb())
        self.image.clip_draw(int(self.frame) * 191, 0, 191, 224, self.x, self.y)
