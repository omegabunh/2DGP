import random
from pico2d import *


class Map:
    def __init__(self):
        self.image = load_image('sprite//map3.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.bgm = load_music('music//BrokenDream.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        self.w = self.image.w
        self.h = self.image.h
        self.window_left = 0
        self.window_bottom = 0

    def set_center_object(self, character):
        self.center_object = character

    def update(self):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width // 2, self.w - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height // 2, self.h - self.canvas_height)

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0
                                       )
