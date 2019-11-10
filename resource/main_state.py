import random
import json
import os

from pico2d import *
import game_framework
import title_state
import main2_state
import game_world
from character1 import Character
from boss1 import Boss
from monster import Monster
MAP_WIDTH, MAP_HEIGHT = 1997, 950

boss = None
monster = None
character = None
monsters = None
key = None
running = True

character_hp = 10000

t = random.randint(1, 4)

def enter():
    global image, key
    global boss, monster, character, monsters
    image = load_image('map2.png')
    key = load_image('key.png')
    boss = Boss()
    monster = Monster()
    character = Character()
    game_world.add_object(image, 0)
    game_world.add_object(key, 1)
    game_world.add_object(character, 2)
    game_world.add_object(monster, 3)
    game_world.add_object(boss, 4)

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(main2_state)
        else:
            character.handle_event(event)
def update():
    boss.update()
    character.update()
    monster.update()

def draw():
    global image
    clear_canvas()
    image.draw(MAP_WIDTH//2, MAP_HEIGHT//2)
    boss.draw()
    monster.draw()
    character.draw()
    key.draw(1700, 50)
    update_canvas()
    delay(0.05)
#open_canvas(MAP_WIDTH, MAP_HEIGHT)






