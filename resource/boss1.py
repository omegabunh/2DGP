from pico2d import *
class Boss:
    image = None
    hp_image = None
    def __init__(self):
        self.x, self.y = 1070, 470
        self.hp_x, self.hp_y = 1748//2, 920
        self.frame = 0
        if Boss.image == None:
            Boss.image = load_image('boss_phase1(248x245).png')
        if Boss.hp_image == None:
            Boss.hp_image = load_image('boss_hp.png')
    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 248, 0, 248, 245, self.x, self.y)
        self.hp_image.draw_now(self.hp_x, self.hp_y)
