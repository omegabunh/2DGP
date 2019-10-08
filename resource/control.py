from pico2d import *

def handle_events():
    global running
    global dir_x
    global dir_y
    global side_1
    global side_2
    global side_3
    global attack
    global prone
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 2
                side_1 = 2
            elif event.key == SDLK_LEFT:
                dir_x -= 2
                side_1 = 3
            elif event.key == SDLK_DOWN:
                prone = True
                if side_1 == 0:
                    side_3 = 1
                elif side_1 == 1:
                    side_3 = 0
            elif event.key == SDLK_LALT:
                if side_1 == 0:
                    dir_y += 4
                    side_1 = 4
                elif side_1 == 1:
                    dir_y += 4
                    side_1 = 5
            elif event.key == SDLK_LCTRL:
                attack = True
                if side_1 == 0:
                    side_2 = 1
                elif side_1 == 1:
                    side_2 = 0
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 2
                side_1 = 0
            elif event.key == SDLK_LEFT:
                dir_x += 2
                side_1 = 1
            elif event.key == SDLK_DOWN:
                prone = False
                if side_3 == 1:
                    side_1 = 0
                elif side_3 == 0:
                    side_1 = 1
            elif event.key == SDLK_LALT:
                if side_1 == 4:
                    dir_y -= 4
                    side_1 = 0
                elif side_1 == 5:
                    dir_y -= 4
                    side_1 = 1
            elif event.key == SDLK_LCTRL:
                attack = False
                if side_2 == 0:
                    side_1 = 1
                elif side_2 == 1:
                    side_1 = 0

    pass

open_canvas(1748, 979)
map1 = load_image('map1.png')
character = load_image('character.png')
character_attack = load_image('character_attack.png')
character_prone = load_image('character_prone.png')
attack = False
prone = False
running = True
x = 1748 // 2
y = 170
frame = 0
dir_x = 0
dir_y = 0
side_1 = 0
side_2 = 0
side_3 = 0

while running:
    clear_canvas()
    map1.draw(874, 489.5)
    if attack == False:
        if prone == False:
            character.clip_draw(frame * 92, side_1 * 96, 92, 96, x, y)
    elif attack == True:
        if prone == False:
            character_attack.clip_draw(frame * 260, side_2 * 172, 260, 172, x, y+23)
    if prone == True:
        character_prone.clip_draw(frame * 140, side_3 * 55, 140, 55, x, y - 15)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 4
    x += dir_x * 5
    y = 170 + dir_y * 15
    delay(0.08)


close_canvas()