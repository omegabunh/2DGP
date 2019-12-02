import random
import json
import os

from pico2d import *
import game_framework
import title_state
import main2_state
import over_state
import game_world

from map2 import Map
from key import Key
from character1 import Character
from boss1 import Boss
from monster import Monster
from mushroom import Mushroom

boss = None
character = None
monsters = []
mushroom = None
running = True
timer = 0
overTimer = 0

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
    global map2
    map2 = Map()
    game_world.add_object(map2, 0)

    key = Key()
    game_world.add_object(key, 1)

    global boss
    boss = Boss()
    game_world.add_object(boss, 1)

    global monsters
    monsters = [Monster() for i in range(3)]
    # monsters = Monster()
    game_world.add_objects(monsters, 1)

    global mushroom
    mushroom = Mushroom()
    game_world.add_object(mushroom, 1)

    global character
    character = Character()
    game_world.add_object(character, 1)


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
            map2.bgm.stop()
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            map2.bgm.stop()
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            map2.bgm.stop()
            game_framework.change_state(main2_state)
        else:
            character.handle_event(event)

def update():
    global timer, overTimer
    timer += 1
    for game_object in game_world.all_objects():
        game_object.update()

    if mushroom.hit >= 30:
        mushroom.deadstate = True
        game_world.remove_object(mushroom)

    if boss.hp <= 0:
        game_world.remove_object(boss)
        map2.bgm.stop()
        game_framework.change_state(main2_state)

    if character.hp <= 0:
        map2.bgm.stop()
        character.deadstate = True
        character.hp = 0
        overTimer += 1
        if overTimer == 100:
            game_framework.change_state(over_state)

    if idle_collide(character, boss):
        if character.idlestate:
            if character.idle_op == False and character.hp != 0:
                character.hp -= 2
                character.w -= 0.2
                character.hp_x1 -= 0.1
                character.idle_op = True

    if run_collide(character, boss):
        if character.runstate:
            if character.run_op == False and character.hp != 0:
                character.hp -= 2
                character.w -= 0.2
                character.hp_x1 -= 0.1
                character.run_op = True

    if prone_collide(character, boss):
        if character.pronestate:
            if character.prone_op == False and character.hp != 0:
                character.hp -= 2
                character.w -= 0.2
                character.hp_x1 -= 0.1
                character.prone_op = True

    if skill_collide(character, boss):
        if character.skillstate:
            if character.boss_skill_damage == False and boss.hitstate == False:
                boss.w += -3
                boss.hp_x += -1.5
                boss.hp -= 2
                character.boss_skill_damage = True
                boss.hitstate = True

    if attack_collide(character, boss):
        if character.attackstate:
            if character.attack_damage == False and boss.hitstate == False:
                boss.w += -1.5
                boss.hp_x += -0.725
                boss.hp -= 1
                character.attack_damage = True
                boss.hitstate = True

    if idle_collide(character, mushroom):
        if character.idlestate and mushroom.deadstate == False:
            if character.idle_op == False and character.hp != 0:
                character.hp -= 50
                character.w -= 5
                character.hp_x1 -= 2.5
                character.idle_op = True

    if run_collide(character, mushroom):
        if character.runstate and mushroom.deadstate == False:
            if character.run_op == False and character.hp != 0:
                character.hp -= 50
                character.w -= 5
                character.hp_x1 -= 2.5
                character.run_op = True

    if prone_collide(character, mushroom):
        if character.pronestate and mushroom.deadstate == False:
            if character.prone_op == False and character.hp != 0:
                character.hp -= 50
                character.w -= 5
                character.hp_x1 -= 2.5
                character.prone_op = True

    if skill_collide(character, mushroom):
        if mushroom.hit >= 30:
            game_world.remove_object(mushroom)
        if character.skillstate:
            if character.mushroom_skill_damage == False or character.mushroom_skill2_damage == False and mushroom.hitstate == False:
                mushroom.hit += 2
                character.mushroom_skill_damage = True
                character.mushroom_skill2_damage = True
                mushroom.hitstate = True

    if attack_collide(character, mushroom):
        if character.attackstate:
            if character.attack_damage == False and mushroom.hitstate == False:
                mushroom.hit += 1
                character.attack_damage = True
                mushroom.hitstate = True

    for monster in monsters:

        if monster.hit >= 30:
            monster.deadstate = True
            game_world.remove_object(monster)

        if idle_collide(character, monster):
            if character.idlestate and monster.deadstate == False:
                if character.idle_op == False and character.hp != 0:
                    character.hp -= 100
                    character.w -= 10
                    character.hp_x1 -= 5
                    character.idle_op = True

        if run_collide(character, monster):
            if character.runstate and monster.deadstate == False:
                if character.run_op == False and character.hp != 0:
                    character.hp -= 100
                    character.w -= 10
                    character.hp_x1 -= 5
                    character.run_op = True

        if prone_collide(character, monster):
            if character.pronestate and monster.deadstate == False:
                if character.prone_op == False and character.hp != 0:
                    character.hp -= 100
                    character.w -= 10
                    character.hp_x1 -= 5
                    character.prone_op = True

        if skill_collide(character, monster):
            if monster.hit >= 30:
                game_world.remove_object(monster)
            if character.skillstate:
                if character.monster_skill_damage == False or character.monster_skill2_damage == False and monster.hitstate == False:
                    monster.hit += 2
                    character.monster_skill_damage = True
                    character.monster_skill2_damage = True
                    monster.hitstate = True

        if attack_collide(character, monster):
            if character.attackstate:
                if character.attack_damage == False and monster.hitstate == False:
                    monster.hit += 1
                    character.attack_damage = True
                    monster.hitstate = True

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    delay(0.05)

