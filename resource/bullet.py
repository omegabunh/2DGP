from pico2d import *

import game_world
import game_framework
import random
import math
import main2_state

PIXEL_PER_METER = (10.0 / 0.3)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Bullet:
    image = None

    def __init__(self, x=800, y=10, velocity=5, round_bullet_count=18):
        if Bullet.image is None:
            Bullet.image = load_image('sprite//bullet(32x32).png')
        self.x = x
        self.y = y
        self.frame = random.randint(0, 5)
        self.r = 10
        self.round_bullet_count = 6
        self.velocity = velocity
        self.round_bullet_count = round_bullet_count

    def get_bb(self):
        return self.x - 12, self.y - 12, self.x + 12, self.y + 12

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.r = 3
        if self.x < 10 or self.x > 1748 - 10 or main2_state.character.hp < 0:
            game_world.remove_object(self)

        if main2_state.idle_collide(main2_state.character, self):
            if main2_state.character.idlestate:
                if main2_state.character.idle_op == False and main2_state.character.hp != 0:
                    main2_state.character.hp -= 100
                    main2_state.character.w -= 10
                    main2_state.character.hp_x1 -= 5
                    main2_state.character.idle_op = True
                    game_world.remove_object(self)

        if main2_state.run_collide(main2_state.character, self):
            if main2_state.character.runstate:
                if main2_state.character.run_op == False and main2_state.character.hp != 0:
                    main2_state.character.hp -= 100
                    main2_state.character.w -= 10
                    main2_state.character.hp_x1 -= 5
                    main2_state.character.run_op = True
                    game_world.remove_object(self)

    def draw(self):
        draw_rectangle(*self.get_bb())
        angle = self.round_bullet_count * 3.141592 / 180
        self.x = self.x + self.r * math.cos(angle) * FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        self.y = self.y + self.r * math.sin(angle) * FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        self.image.clip_draw(int(self.frame) * 32, 0, 32, 32, self.x, self.y)
