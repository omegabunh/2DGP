import random
import json
import os

from pico2d import *
import game_framework
import title_state
import main2_state
import game_world

from map2 import Map
from key import Key
from character1 import Character
from boss1 import Boss
from monster import Monster

boss = None
character = None
monsters = []
running = True
character_hp = 10000


def idle_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_idle_collide()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def prone_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_prone_collide()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def attack_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_attack_collide()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def skill_collide(a, b):
    if character.skillstate:
        left_a, bottom_a, right_a, top_a = a.get_skill_collide()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False

    return True


def enter():
    map2 = Map()
    game_world.add_object(map2, 0)

    key = Key()
    game_world.add_object(key, 1)

    global boss
    boss = Boss()
    game_world.add_object(boss, 1)

    global character
    character = Character()
    game_world.add_object(character, 1)

    global monsters
    # monsters = [Monster() for i in range(3)]
    monsters = Monster()
    game_world.add_object(monsters, 1)


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
    for game_object in game_world.all_objects():
        game_object.update()

    if skill_collide(character, boss):
        if character.skillstate:
            print('skill collide to boss')
            boss.hp_x += -0.1
            boss.hp -= 2
            if boss.hp <= 0:
                game_world.remove_object(boss)
                game_framework.change_state(main2_state)

    if skill_collide(character, monsters):
        if character.skillstate:
            monsters.hit += 1
            game_world.remove_object(monsters)
            if monsters.hit == 100:
                game_world.remove_object(monsters)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    delay(0.05)

# open_canvas(MAP_WIDTH, MAP_HEIGHT)
