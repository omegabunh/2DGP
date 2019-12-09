from pico2d import *

class Map:
    def __init__(self):
        self.bgm = load_music('music//NxLogo.mp3')
        self.bgm.set_volume(64)
        self.bgm.play(1)
        self.image = load_image('sprite//start.jpg')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1748 // 2, 950 // 2)