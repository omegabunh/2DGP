from pico2d import *
open_canvas(1748,979)
map1 = load_image('map1.png')
character_r = load_image('r_walk4.png')
character_l = load_image('l_walk4.png')

running = True
x = 1748 // 2
frame = 0

def handle_events():
    global running
    global x
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x = x + 5
            elif event.key == SDLK_LEFT:
                x = x - 5
            elif event.key == SDLK_ESCAPE:
                running = False
    pass

while True:

    while x < 1450:
        clear_canvas()
        map1.draw(874,489.5)
        character_r.clip_draw(frame * 92, 0, 92, 96, x, 170)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 4
        delay(0.05)
        get_events()
    while x > 600:
        clear_canvas()
        map1.draw(874,489.5)
        character_l.clip_draw(frame * 92, 0, 92, 96, x, 170)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 4
        delay(0.05)
        get_events()

close_canvas()

