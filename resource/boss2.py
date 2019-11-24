from pico2d import *
import random
import math
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

MAP_WIDTH, MAP_HEIGHT = 1997, 950

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10


class Boss:
    image = None
    hp_image = None
    hp_background = None

    def __init__(self):
        self.x, self.y = 1070, 470
        self.dir = random.random() * 2 * math.pi  # random moving direction
        self.timer = 1.0  # change direction every 1 sec when wandering
        self.hp_x, self.hp_y = 1748 // 2, 920
        self.hp_x1, self.hp_y1 = 1748 // 2, 920
        self.build_behavior_tree()
        self.speed = 0
        self.frame = 0
        self.count = 0
        self.hp = 1000
        self.w = 1500
        self.w1 = 1505
        self.h = 30
        self.h1 = 35
        self.font = load_font('ENCR10B.TTF', 16)
        if Boss.image is None:
            Boss.image = load_image('boss_phase2(356x384).png')
        if Boss.hp_image is None:
            Boss.hp_image = load_image('boss_hp.png')
        if Boss.hp_background is None:
            Boss.hp_background = load_image('boss_hp_background.png')

    def calculate_current_position(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(50, self.y, 1024 - 50)

    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()
        self.timer -= game_framework.frame_time
        if self.timer < 0:
            self.timer += 1.0
            self.dir = random.random() * 2 * math.pi
        return BehaviorTree.SUCCESS

    def get_bb(self):
        return self.x - 150, self.y - 140, self.x + 130, self.y + 180

    def find_player(self):
        # fill here
        pass

    def move_to_player(self):
        # fill here
        pass

    def get_next_position(self):
        # fill here
        pass

    def move_to_target(self):
        # fill here
        pass

    def build_behavior_tree(self):
        wander_node = LeafNode("Wander", self.wander)
        self.bt = BehaviorTree(wander_node)

    def update(self):
        self.bt.run()
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 16

    def draw(self):
        self.font.draw(self.x - 60, self.y + 150, '(hp: %0.0f)' % self.hp, (0, 255, 0))
        self.image.clip_draw(int(self.frame) * 356, 0, 356, 384, self.x, self.y)
        draw_rectangle(*self.get_bb())
        self.hp_background.draw_now(self.hp_x1, self.hp_y1, self.w1, self.h1)
        self.hp_image.draw_now(self.hp_x, self.hp_y, self.w, self.h)