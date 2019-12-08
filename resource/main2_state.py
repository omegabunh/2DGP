from pico2d import *
import game_framework
import main_state
import game_world
import end_state
import over_state
from map3 import Map
from character2 import Character
from boss2 import Boss
from butterfly import Butterfly
from key import Key
from horn import Horn

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

boss = None
character = None
key = None
running = True
butterflys = []
horn = None
overTimer = 0
spacestate = False
spacecount = 0
butterflydead = False

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
    if character.skillstate == True:
        left_a, bottom_a, right_a, top_a = a.get_skill_collide()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False

    return True


def enter():
    global map
    map = Map()
    game_world.add_object(map, 0)

    global horn
    horn = Horn()
    game_world.add_object(horn, 1)

    global boss
    boss = Boss()
    game_world.add_object(boss, 1)

    global character
    character = Character()
    game_world.add_object(character, 1)

    global butterflys
    butterflys = [Butterfly(character) for i in range(4)]
    game_world.add_objects(butterflys, 1)

    key = Key()
    game_world.add_object(key, 1)

    map.set_center_object(character)
    character.set_background(map)
    horn.set_background(map)
    boss.set_background(map)


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    global spacestate, spacecount
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            map.bgm.stop()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(end_state)
            map.bgm.stop()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            spacestate = True
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_SPACE):
            spacestate = False
        else:
            character.handle_event(event)

def update():
    global spacecount, butterflydead, overTimer, deadcount
    for game_object in game_world.all_objects():
        game_object.update()

    if character.hp <= 0:
        character.deadstate = True
        character.hp = 0
        overTimer += 1
        map.bgm.stop()
        if overTimer == 100:
            game_framework.change_state(over_state)

    if boss.hp <= 0:
        boss.deadSound()
        game_world.remove_object(boss)
        deadcount += 1
        if deadcount == 200:
            map.bgm.stop()
            game_framework.push_state(end_state)

    for butterfly in butterflys:
        butterflydead = False
        if idle_collide(character, horn):
            if character.idlestate:
                if spacestate and boss.hp <= 500:
                    horn.bar_x1 += 0.25 * FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
                    horn.w += 0.5 * FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
                    spacecount += 1 * FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
                    if spacecount >= 130:
                        horn.w = 0
                        game_world.remove_object(butterfly)
                        butterflydead = True

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


    if skill_collide(character, boss):
        if character.skillstate:
            if character.skill_damage == False and boss.hitstate == False:
                boss.w += -6
                boss.hp_x += -3
                boss.hp -= 4
                character.skill_damage = True
                boss.hitstate = True


    if attack_collide(character, boss):
        if character.attackstate:
            if not character.attack_damage and boss.hitstate == False:
                boss.w += -1.5
                boss.hp_x += -0.725
                boss.hp -= 1
                character.attack_damage = True
                boss.hitstate = True


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    #delay(0.05)
# open_canvas(MAP_WIDTH, MAP_HEIGHT)