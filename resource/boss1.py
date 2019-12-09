from pico2d import *
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3

class Boss:
    image = None
    hp_image = None
    hp_background = None
    attack_image = None

    def __init__(self):
        self.x, self.y = 1070, 470
        self.hp_x, self.hp_y = 1748 // 2, 920
        self.hp_x1, self.hp_y1 = 1748 // 2, 920
        self.frame = 0
        self.frame1 = 0
        self.hp = 1000
        self.count = 0
        self.font = load_font('Maplestory Bold.ttf', 16)
        self.w = 1500
        self.w1 = 1505
        self.h = 30
        self.h1 = 35
        self.hitstate = False
        self.skillstate = False
        self.skillcount = 0
        self.hit_count = 0
        if Boss.image is None:
            Boss.image = load_image('sprite//boss1(320x410).png')
        if Boss.attack_image is None:
            Boss.attack_image = load_image('sprite//boss1_attack(340x420).png')
        if Boss.hp_image is None:
            Boss.hp_image = load_image('sprite//boss_hp.png')
        if Boss.hp_background is None:
            Boss.hp_background = load_image('sprite//boss_hp_background.png')
        self.dead_sound = load_wav('music//lucid_die1.wav')
        self.dead_sound.set_volume(80)
        self.skill_sound = load_wav('music//lucid_skill.wav')
        self.skill_sound.set_volume(80)

    def get_bb(self):
        return self.x - 100, self.y - 100, self.x + 100, self.y + 130

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 15
        if self.hitstate == True:
            self.hit_count += 1
            self.image.opacify(0.8)
            if self.hit_count % 50 == 0:
                self.image.opacify(1.0)
            if self.hit_count == 150:
                self.hitstate = False
                self.hit_count = 0

        if self.hp % 50 == 0 and self.count == 0:
            self.skillSound()
            self.count += 1
            self.skillstate = True

        #self.hp != 1000 and
        if self.skillstate == True:
            self.skillcount += 1
            if self.skillcount == 220:
                self.skillcount = 0
                self.skillstate = False

        if self.hp % 50 == 40:
            self.count = 0

        if self.hp == 0:
            self.deadSound()

    def draw(self):
        self.font.draw(self.x - 60, self.y + 150, '(hp: %0.0f)' % self.hp, (0, 255, 0))
        if self.skillstate:
            self.attack_image.clip_draw(int(self.frame) * 340, 0, 340, 420, self.x - 10, self.y + 4)
        else:
            self.image.clip_draw(int(self.frame) * 320, 0, 320, 410, self.x, self.y)
        #draw_rectangle(*self.get_bb())
        self.hp_background.draw(self.hp_x1, self.hp_y1, self.w1, self.h1)
        self.hp_image.draw(self.hp_x, self.hp_y, self.w, self.h)

    def deadSound(self):
        self.dead_sound.play()

    def skillSound(self):
        self.skill_sound.play()
