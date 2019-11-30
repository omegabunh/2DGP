import random
import json
import os
import game_framework
from pico2d import *
import main_state
import game_world
from character import Character
from npc import Npc

name = "TitleState"
image = None
character = None
npc = None
npc_chat = None
running = True
space_cnt = 0

character_hp = 10000

def enter():
    global image, key
    global character
    global npc
    global npc_chat
    image = load_image('sprite//map1.png')
    key = load_image('sprite//key.png')
    character = Character()
    npc = Npc()
    npc_chat = load_image('sprite//npc_chat.png')
    game_world.add_object(image, 0)
    game_world.add_object(key, 1)
    game_world.add_object(character, 1)
    game_world.add_object(npc, 1)
    game_world.add_object(npc_chat, 1)

def exit():
    game_world.clear()

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
    if 1170 <= character.x <= 1240:
        npc.font.draw(npc.x - 45, npc.y + 60, 'PRESS SPACE', (255, 0, 0))
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

