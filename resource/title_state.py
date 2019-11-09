import random
import json
import os
import game_framework
from pico2d import *
import main_state

from character import Character

name = "TitleState"
image = None
character = None
npc = None
npc_chat = None
dir_x = 0
dir_y = 0
side_character_idle = 0
side_character_attack = 0
side_character_prone = 0
side_character_skill1 = 0
side_character_skill2 = 0
idle = False
running = True
attack = False
prone = False
skill = False
skill2 = False
jump_state = False
jump_force = 0
count = 0
space_cnt = 0
up_cnt = 0
down_cnt = 0
character_hp = 10000
bottom = 170
class Npc:
    image_n = None
    def __init__(self):
        self.x, self.y = 1200, 182
        if Npc.image_n == None:
            Npc.image_n = load_image('npc.png')

    def update(self):
        pass
    def draw(self):
        self.image_n.draw(self.x, self.y)

def enter():
    global image, key
    global character
    global npc
    global npc_chat
    image = load_image('map1.png')
    key = load_image('key.png')
    character = Character()
    npc = Npc()
    npc_chat = load_image('npc_chat.png')

def exit():
    global image, key
    global character
    global npc
    global npc_chat
    del(image)
    del(key)
    del(character)
    del(npc)
    del(npc_chat)



def handle_events():
    global space_cnt
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if 1170 <= character.x <= 1240:
                space_cnt += 1
                if event.key == SDLK_SPACE and (space_cnt != 0 and space_cnt % 2 == 0):
                    game_framework.change_state(main_state)
        else:
            character.handle_event(event)
def draw():
    clear_canvas()
    image.draw(MAP_WIDTH//2, MAP_HEIGHT//2)
    npc.draw()
    if space_cnt % 2 == 1:
        npc_chat.draw(MAP_WIDTH//2, MAP_HEIGHT//2)
    character.draw()
    key.draw(1700, 50)
    update_canvas()
    delay(0.05)
def update():
    character.update()
    npc.update()
    #npc_chat.update()
def pause():
    pass


def resume():
    pass

MAP_WIDTH, MAP_HEIGHT = 1748, 979


#open_canvas(MAP_WIDTH, MAP_HEIGHT)
#map1 = load_image('map1.png')

