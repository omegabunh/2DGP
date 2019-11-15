import random
import json
import os
from pico2d import *
import game_framework
import title_state
import main_state
import game_world
from boss2 import Boss
MAP_WIDTH, MAP_HEIGHT = 1997, 950

boss = None
monster = None
character = None
key = None
dir_x = 0
dir_y = 0
side_character_idle = 0
side_character_attack = 0
side_character_skill1 = 0
side_character_skill2 = 0
running = True
attack = False
skill = False
skill2 = False
jump_state = False
jump_force = 0
count = 0

character_hp = 10000

class Character:
    idle = None
    attack = None
    prone = None
    skill = None
    skill2 = None
    def __init__(self):
        self.x, self.y = MAP_WIDTH // 2, 300
        self.frame = 0
        self.frame1 = 0
        if Character.idle == None:
            Character.idle = load_image('character.png')
        if Character.attack == None:
            Character.attack = load_image('character_attack.png')
        if Character.skill == None:
            Character.skill = load_image('character_skill(457x260).png')
        if Character.skill2 == None:
            Character.skill2 = load_image('character_skill2(572x406).png')

    def update(self):
        global jump_state
        global jump_force
        self.frame = (self.frame + 1) % 4
        self.frame1 = (self.frame + 1) % 14
        self.frame2 = (self.frame + 1) % 3
        self.x += dir_x * 5
        self.y += dir_y * 5

    def draw(self):
        if attack == False:
            if skill == False:
                self.idle.clip_draw(self.frame * 92, side_character_idle * 96, 92, 96, self.x, self.y)
            if skill == True and skill2 == False:
                self.skill.clip_draw(self.frame1 * 457, side_character_skill1 * 260, 457, 260, self.x, self.y + 70)
            if skill2 == True and skill == True:
                self.skill2.clip_draw(self.frame1 * 572, side_character_skill2 * 406, 573, 406, self.x, self.y + 40)
        elif attack == True:
            self.attack.clip_draw(self.frame2 * 260, side_character_attack * 172, 260, 172, self.x, self.y + 23)

def enter():
    global image, key
    global boss, monster, character
    image = load_image('map3.png')
    key = load_image('key.png')
    boss = Boss()
    character = Character()
    game_world.add_object(image, 0)
    game_world.add_object(key, 1)
    game_world.add_object(character, 1)
    game_world.add_object(boss, 1)

def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def handle_events():
    global running
    global dir_x
    global dir_y
    global side_character_idle
    global side_character_attack
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
            game_framework.quit()
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            #game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(main_state)
            elif event.key == SDLK_RIGHT:
                dir_x += 2
                side_character_idle = 2
            elif event.key == SDLK_LEFT:
                dir_x -= 2
                side_character_idle = 3
            elif event.key == SDLK_DOWN:
                if side_character_idle == 0:
                    dir_y -= 2
                    side_character_idle = 4
                elif side_character_idle == 1:
                    dir_y -= 2
                    side_character_idle = 5
            elif event.key == SDLK_LALT:
                if side_character_idle == 0:
                    dir_y += 2
                    side_character_idle = 4
                elif side_character_idle == 1:
                    dir_y += 2
                    side_character_idle = 5
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
                if side_character_idle == 4:
                    dir_y += 2
                    side_character_idle = 0
                elif side_character_idle == 5:
                    dir_y += 2
                    side_character_idle = 1
            elif event.key == SDLK_LALT:
                if side_character_idle == 4:
                    dir_y -= 2
                    side_character_idle = 0
                elif side_character_idle == 5:
                    dir_y -= 2
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

def update():
    boss.update()
    character.update()

def draw():
    global image
    clear_canvas()
    image.draw(MAP_WIDTH//2, MAP_HEIGHT//2)
    boss.draw()
    character.draw()
    key.draw(1700, 50)
    update_canvas()
    delay(0.05)
#open_canvas(MAP_WIDTH, MAP_HEIGHT)




