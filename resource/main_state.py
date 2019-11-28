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
#monsters = None
running = True
character_hp = 10000


def idle_collide(a, b):
    if character.idlestate:
        left_a, bottom_a, right_a, top_a = a.get_idle_collide()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False

    return True


def run_collide(a, b):
    if character.runstate:
        left_a, bottom_a, right_a, top_a = a.get_run_collide()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False

    return True


def prone_collide(a, b):
    if character.pronestate:
        left_a, bottom_a, right_a, top_a = a.get_prone_collide()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False

    return True


def attack_collide(a, b):
    if character.attackstate:
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
    monsters = [Monster() for i in range(3)]
    #monsters = Monster()
    game_world.add_objects(monsters, 1)


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


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    delay(0.05)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for monster in monsters:

        if monster.hit >= 30:
            monster.deadstate = True
            game_world.remove_object(monster)

        if boss.hp <= 0:
            game_world.remove_object(boss)
            game_framework.change_state(main2_state)

        if character.hp <= 0:
            character.deadstate = True
            character.hp = 0

        if idle_collide(character, boss):
            if character.idlestate:
                if character.idle_op == False and character.hp != 0:
                    character.hp -= 2
                    character.idle_op = True

        if idle_collide(character, monster):
            if character.idlestate and monster.deadstate == False:
                if character.idle_op == False and character.hp != 0:
                    character.hp -= 100
                    character.idle_op = True

        if run_collide(character, boss):
            if character.runstate:
                if character.run_op == False and character.hp != 0:
                    character.hp -= 2
                    character.run_op = True

        if run_collide(character, monster):
            if character.runstate and monster.deadstate == False:
                if character.run_op == False and character.hp != 0:
                    character.hp -= 100
                    character.run_op = True

        if prone_collide(character, boss):
            if character.pronestate:
                if character.prone_op == False and character.hp != 0:
                    character.hp -= 2
                    character.prone_op = True

        if prone_collide(character, monster):
            if character.pronestate and monster.deadstate == False:
                if character.prone_op == False and character.hp != 0:
                    character.hp -= 500
                    character.prone_op = True

        if skill_collide(character, boss):
            if character.skillstate:
                if character.skill_damage == False and boss.hitstate == False:
                    boss.w += -3
                    boss.hp_x += -1.5
                    boss.hp -= 2
                    character.skill_damage = True
                    boss.hitstate = True

        if skill_collide(character, monster):
            if monster.hit >= 30:
                game_world.remove_object(monster)
            if character.skillstate:
                if character.skill_damage == False or character.skill2_damage == False and monster.hitstate == False:
                    monster.hit += 2
                    character.skill_damage = True
                    character.skill2_damage = True
                    monster.hitstate = True

        if attack_collide(character, boss):
            if character.attackstate:
                if character.attack_damage == False and boss.hitstate == False:
                    boss.w += -1.5
                    boss.hp_x += -0.725
                    boss.hp -= 1
                    character.attack_damage = True
                    boss.hitstate = True

        if attack_collide(character, monster):
            if character.attackstate:
                if character.attack_damage == False and monster.hitstate == False:
                    monster.hit += 1
                    character.attack_damage = True
                    monster.hitstate = True

# open_canvas(MAP_WIDTH, MAP_HEIGHT)
