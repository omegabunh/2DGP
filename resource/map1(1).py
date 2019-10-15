from pico2d import *
import random

MAP_WIDTH, MAP_HEIGHT = 1748, 979
class Character:
    def __init__(self):
        self.x, self.y = MAP_WIDTH // 2, 170
        self.frame = 0
        self.character = load_image('character.png')
        self.character_attack = load_image('character_attack.png')
        self.character_prone = load_image('character_prone.png')
        self.jump_state = False
        self.jump_force = 0
    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += dir_x * 5
        if self.jump_state == True:
            self.y = 170 + self.jump_force
            self.jump_force -= 8
            print(self.jump_force)
            if self.y <= 170:
                self.y = 170
                self.jump_state = False

    def draw (self):
        if attack == False:
            if prone == False:
                self.character.clip_draw(self.frame * 92, side_1 * 96, 92, 96, self.x, self.y)
        elif attack == True:
            if prone == False:
                self.character_attack.clip_draw(self.frame * 260, side_2 * 172, 260, 172, self.x, self.y + 23)
            if prone == True:
                self.character_prone.clip_draw(self.frame * 140, side_3 * 55, 140, 55, self.x, self.y - 15)


def character_handle_events():
    global running
    global dir_x
    global dir_y
    global side_1
    global side_2
    global side_3
    global attack
    global prone
    global jump_state
    global jump_force

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
            elif event.key == SDLK_LALT and jump_state == False:
                if side_1 == 0:
                    jump_state = True
                    jump_force = 60
                    side_1 = 4
                elif side_1 == 1:
                    jump_state = True
                    jump_force = 60
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
            elif event.key == SDLK_LALT and jump_state == True:
                if side_1 == 4:
                    side_1 = 0
                elif side_1 == 5:
                    side_1 = 1
            elif event.key == SDLK_LCTRL:
                attack = False
                if side_2 == 0:
                    side_1 = 1
                elif side_2 == 1:
                    side_1 = 0

open_canvas(MAP_WIDTH, MAP_HEIGHT)
map1 = load_image('map1.png')
dir_x = 0
dir_y = 0
side_1 = 0
side_2 = 0
side_3 = 0
running = True
attack = False
prone = False
jump_state = False
jump_force = 0

character = Character()


while running:
    character_handle_events()
    character.update()

    clear_canvas()
    map1.draw(MAP_WIDTH // 2, MAP_HEIGHT // 2)



    character.draw()
    update_canvas()
    delay(0.05)

close_canvas()