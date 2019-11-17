from pico2d import *
import random

MAP_WIDTH, MAP_HEIGHT = 1997, 950
size = 10
points = [(random.randint(0 + 50, MAP_WIDTH-50), random.randint(0+50, MAP_HEIGHT-50)) for i in range(size)]
n = 1

class Boss:
    image = None
    def __init__(self):
        self.x, self.y = 1070, 470
        self.frame = 0
        self.count = 0
        if Boss.image == None:
            Boss.image = load_image('boss_phase2(356x384).png')

    def move(self, p1, p2, p3, p4):
        for i in range(0, 50, 2):
            t = i / 1000
            self.x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p1[0]) / 2
            self.y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p1[1]) / 2

    def update(self):
        global p1, p2, p3, p4
        global n

        if self.count % 10 == 0:
            p1, p2, p3, p4 = points[n - 3], points[n - 2], points[n - 1], points[n]
            n = (n + 1) % size
            Boss.move(self, p1, p2, p3, p4)
        self.count += 1
        self.frame = (self.frame + 1) % 8
    def draw(self):
        self.image.clip_draw(self.frame * 356, 0, 356, 384, self.x, self.y)
