from pico2d import *

def handle_events():
    global running
    global dir
    global side
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                side = 0
            elif event.key == SDLK_LEFT:
                dir -= 1
                side = 96
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1

    pass

open_canvas(1748, 979)
map1 = load_image('map1.png')
character = load_image('walk8.png')


running = True
x = 1748 // 2
frame = 0
dir = 0
side = 0
while running:
    clear_canvas()
    map1.draw(874,489.5)
    character.clip_draw(frame * 92, side, 92, 96, x, 170)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 4
    x += dir * 5
    delay(0.08)

close_canvas()