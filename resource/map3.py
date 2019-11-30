from pico2d import *

class Map:
    def __init__(self):
        self.image = load_image('sprite//map3.png')
        self.bgm = load_music('music//BrokenDream.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
    def update(self):
        pass

    def draw(self):
        self.image.draw(2050 // 2, 1550 // 2)