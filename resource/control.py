from pico2d import *

def handle_events():
    global running
    global dir_x
    global dir_y
    global side
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 2
                side = 2
            elif event.key == SDLK_LEFT:
                dir_x -= 2
                side = 3
            elif event.key == SDLK_LALT:
                if side == 0:
                    dir_y += 4
                    side = 4
                elif side == 1:
                    dir_y += 4
                    side = 5

            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 2
                side = 0
            elif event.key == SDLK_LEFT:
                dir_x += 2
                side = 1
            elif event.key == SDLK_LALT:
                if side == 4:
                    dir_y -= 4
                    side = 0
                elif side == 5:
                    dir_y -= 4
                    side = 1

    pass

open_canvas(1748, 979)
map1 = load_image('map1.png')
character = load_image('character.png')


running = True
x = 1748 // 2
y = 170
frame = 0
dir_x = 0
dir_y = 0
side = 0

while running:
    clear_canvas()
    map1.draw(874, 489.5)
    character.clip_draw(frame * 92, side * 96, 92, 96, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 4
    x += dir_x * 5
    y += dir_y * 5
    delay(0.08)


close_canvas()