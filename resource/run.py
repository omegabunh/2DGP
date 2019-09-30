from pico2d import *
open_canvas(1748,979)
map1 = load_image('map1.png')
character_r = load_image('r_walk4.png')
character_l = load_image('l_walk4.png')
x = 600
frame = 0

while True:
    while x < 1450:
        clear_canvas()
        map1.draw(874,489.5)
        character_r.clip_draw(frame * 92, 0, 92, 96, x, 170)
        update_canvas()
        frame = (frame + 1) % 4
        x = x + 5
        delay(0.05)
        get_events()
    while x > 600:
        clear_canvas()
        map1.draw(874,489.5)
        character_l.clip_draw(frame * 92, 0, 92, 96, x, 170)
        update_canvas()
        frame = (frame + 1) % 4
        x = x - 5
        delay(0.05)
        get_events()

close_canvas()

