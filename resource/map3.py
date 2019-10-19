from pico2d import *
MAP_WIDTH, MAP_HEIGHT = 800, 600
class Boss:
    def __init__(self):
        self.x, self.y = 1070, 470
        self.frame = 0
        self.image = load_image('boss_phase1(248x245).png')
    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 248, 0, 248, 245, self.x, self.y)

def character_handle_events():
    global running
    global dir_x
    global dir_y
    global side_character_idle
    global side_character_attack
    global side_character_prone
    global attack

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 2
                side_character_idle = 2
            elif event.key == SDLK_LEFT:
                dir_x -= 2
                side_character_idle = 3
            elif event.key == SDLK_DOWN:
                if side_character_idle == 0:
                    dir_y -= 4
                    side_character_prone = 4
                elif side_character_idle == 1:
                    dir_y -= 4
                    side_character_prone = 5
            elif event.key == SDLK_LALT:
                if side_character_idle == 0:
                    dir_y += 4
                    side_character_idle = 4
                elif side_character_idle == 1:
                    dir_y += 4
                    side_character_idle = 5
            elif event.key == SDLK_LCTRL:
                attack = True
                if side_character_idle == 0:
                    side_character_attack = 1
                elif side_character_idle == 1:
                    side_character_attack = 0
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 2
                side_character_idle = 0
            elif event.key == SDLK_LEFT:
                dir_x += 2
                side_character_idle = 1
            elif event.key == SDLK_DOWN:
                if side_character_prone == 1:
                    dir_y += 4
                    side_character_idle = 0
                elif side_character_prone == 0:
                    dir_y += 4
                    side_character_idle = 1
            elif event.key == SDLK_LALT:
                if side_character_idle == 4:
                    dir_y -= 4
                    side_character_idle = 0
                elif side_character_idle == 5:
                    dir_y -= 4
                    side_character_idle = 1
            elif event.key == SDLK_LCTRL:
                attack = False
                if side_character_attack == 0:
                    side_character_idle = 1
                elif side_character_attack == 1:
                    side_character_idle = 0

    pass

open_canvas(MAP_WIDTH, MAP_HEIGHT)
map1 = load_image('map3.png')
character = load_image('character.png')
character_attack = load_image('character_attack.png')
boss = Boss()
attack = False
running = True
x = MAP_WIDTH // 2
y = MAP_HEIGHT // 2
frame = 0
dir_x = 0
dir_y = 0
side_character_idle = 0
side_character_attack = 0
side_character_prone = 0


while running:
    boss.update()
    clear_canvas()
    map1.draw(874, 489.5)

    boss.draw()
    if attack == False:
        character.clip_draw(frame * 92, side_character_idle * 96, 92, 96, x, y)
    elif attack == True:
        character_attack.clip_draw(frame * 260, side_character_attack * 172, 260, 172, x, y + 23)

    update_canvas()

    character_handle_events()
    frame = (frame + 1) % 4
    x += dir_x * 5
    y = dir_y * 5

    delay(0.05)


close_canvas()