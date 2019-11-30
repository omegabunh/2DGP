from pico2d import *
import random
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Mushroom:
    image = None

    def __init__(self):
        if Mushroom.image == None:
            Mushroom.image = load_image('sprite//mushroom.png')
        self.x, self.y = random.randint(100, 1748), 350
        self.frame = 0
        self.velocity = 10
        self.side = 1
        self.hit = 0
        self.font = load_font('ENCR10B.TTF', 16)
        self.deadstate = False
        self.hitstate = False
        self.hit_count = 0

    def get_bb(self):
        return self.x - 80, self.y - 130, self.x + 80, self.y + 100

    def update(self):
        #self.frame = random.randint(0, 5)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        if self.x > 1500:
            self.side = -1
        elif self.x < 100:
            self.side = 1
        self.x += self.velocity * game_framework.frame_time * self.side
        if self.hit >= 30:
            self.deadstate = True
        if self.hitstate == True:
            self.hit_count += 1
            self.image.opacify(0.8)
            if self.hit_count % 10 == 0:
                self.image.opacify(1.0)
            if self.hit_count == 30:
                self.hitstate = False
                self.hit_count = 0

    def draw(self):
        self.font.draw(self.x - 60, self.y + 70, '(hit: %0.0f)' % self.hit, (0, 255, 0))
        draw_rectangle(*self.get_bb())
        if self.side == 1:
            self.image.clip_composite_draw(int(self.frame) * 175, 0, 175, 280, 0.0, 'h', self.x, self.y, 175, 280)

        else:
            self.image.clip_draw(int(self.frame) * 175, 0, 175, 280, self.x, self.y)
