from pico2d import *

class Map:
    def __init__(self):
        self.bgm = load_music('music//lucid_spine.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        self.image = load_image('sprite//boss1clear.jpg')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1748 // 2, 950 // 2)