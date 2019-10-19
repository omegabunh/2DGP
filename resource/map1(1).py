from pico2d import *
import random

MAP_WIDTH, MAP_HEIGHT = 1748, 979
class Character:
    def __init__(self):
        self.x, self.y = MAP_WIDTH // 2, 170
        self.frame = 0
        self.frame1 = 0
        self.character = load_image('character.png')
        self.character_attack = load_image('character_attack.png')
        self.character_prone = load_image('character_prone.png')
        self.character_skill = load_image('character_skill(457x260).png')
        self.character_skill2 = load_image('character_skill2(572x406).png')

    def update(self,jump_state,jump_force):
        self.frame = (self.frame + 1) % 4
        self.frame1 = (self.frame + 1) % 14
        self.x += dir_x * 5
        self.y = 170 + jump_force
            #jump_force -= 8
        print(jump_force)
            #if self.y <= 170:
                #self.y = 170
                #jump_state = False

    def draw(self):
        if attack == False:
            if prone == False and skill == False:
                self.character.clip_draw(self.frame * 92, side_character_idle * 96, 92, 96, self.x, self.y)
            if skill == True and skill2 == False:
                self.character_skill.clip_draw(self.frame1 * 457, side_character_skill1 * 260, 457, 260, self.x, self.y + 70)
            if skill2 == True and skill == True:
                self.character_skill2.clip_draw(self.frame1 * 572, side_character_skill2 * 406, 573, 406, self.x, self.y + 40)
            if prone == True:
                self.character_prone.clip_draw(self.frame * 140, side_character_prone * 55, 140, 55, self.x, self.y - 15)
        elif attack == True:
            self.character_attack.clip_draw(self.frame * 260, side_character_attack * 172, 260, 172, self.x, self.y + 23)

    def handle_events(self):
        global running
        global dir_x
        global dir_y
        global side_character_idle
        global side_character_attack
        global side_character_prone
        global side_character_skill1
        global side_character_skill2
        global attack
        global skill
        global skill2
        global prone
        global jump_state
        global jump_force
        global count

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
                    prone = True
                    if side_character_idle == 0:
                        side_character_prone = 1
                    elif side_character_idle == 1:
                        side_character_prone = 0
                elif event.key == SDLK_LALT and jump_state == False:
                    if side_character_idle == 0:
                        jump_state = True
                        jump_force = 60
                        side_character_idle = 4
                    elif side_character_idle == 1:
                        jump_state = True
                        jump_force = 60
                        side_character_idle = 5
                elif event.key == SDLK_LCTRL:
                    attack = True
                    if side_character_idle == 0:
                        side_character_attack = 1
                    elif side_character_idle == 1:
                        side_character_attack = 0
                elif event.key == SDLK_HOME:
                    count += 1
                    if count % 2 == 1:
                        skill2 = True
                    elif count % 2 == 0:
                        skill2 = False
                elif event.key == SDLK_LSHIFT:
                    skill = True
                    if skill2 == False:
                        if side_character_idle == 0:
                            side_character_skill1 = 0
                        elif side_character_idle == 1:
                            side_character_skill1 = 1
                    elif skill2 == True:
                        if side_character_idle == 0:
                            side_character_skill2 = 0
                        elif side_character_idle == 1:
                            side_character_skill2 = 1

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
                    prone = False
                    if side_character_prone == 1:
                        side_character_idle = 0
                    elif side_character_prone == 0:
                        side_character_idle = 1
                elif event.key == SDLK_LALT and jump_state == True:
                    if side_character_idle == 4:
                        jump_state = False
                        jump_force -= 60
                        side_character_idle = 0
                    elif side_character_idle == 5:
                        jump_state = False
                        jump_force -= 60
                        side_character_idle = 1
                elif event.key == SDLK_LCTRL:
                    attack = False
                    if side_character_attack == 0:
                        side_character_idle = 1
                    elif side_character_attack == 1:
                        side_character_idle = 0
                elif event.key == SDLK_LSHIFT:
                    skill = False
                    if skill2 == False:
                        if side_character_skill1 == 0:
                            side_character_idle = 0
                        elif side_character_skill1 == 1:
                            side_character_idle = 1
                    elif skill2 == True:
                        if side_character_skill2 == 0:
                            side_character_idle = 0
                        elif side_character_skill2 == 1:
                            side_character_idle = 1

open_canvas(MAP_WIDTH, MAP_HEIGHT)
map1 = load_image('map1.png')
dir_x = 0
dir_y = 0
side_character_idle = 0
side_character_attack = 0
side_character_prone = 0
side_character_skill1 = 0
side_character_skill2 = 0
running = True
attack = False
prone = False
skill = False
skill2 = False
jump_state = False
jump_force = 0
count = 0
character = Character()

while running:
    character.handle_events()
    character.update(jump_state, jump_force)

    clear_canvas()
    map1.draw(MAP_WIDTH // 2, MAP_HEIGHT // 2)

    character.draw()
    update_canvas()
    delay(0.05)

close_canvas()