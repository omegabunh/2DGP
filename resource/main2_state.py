from pico2d import *
import game_framework
import main_state
import game_world
from character2 import Character
from boss2 import Boss

MAP_WIDTH, MAP_HEIGHT = 1997, 950

boss = None
monster = None
character = None
monsters = None
key = None
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
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(main_state)
        else:
            character.handle_event(event)


def update():
    boss.update()
    character.update()

    if idle_collide(character, boss):
        if character.idlestate:
            if character.idle_op == False and character.hp != 0:
                character.hp -= 2
                character.idle_op = True
                if character.hp <= 0:
                    game_framework.quit()

    if run_collide(character, boss):
        if character.runstate:
            if character.run_op == False and character.hp != 0:
                character.hp -= 2
                character.run_op = True
                if character.hp <= 0:
                    character.deadstate = True
                    character.hp = 0

    if skill_collide(character, boss):
        if character.skillstate:
            if character.skill_damage == False and boss.hitstate == False:
                boss.w += -3
                boss.hp_x += -1.5
                boss.hp -= 2
                character.skill_damage = True
                boss.hitstate = True
                if boss.hp <= 0:
                    game_world.remove_object(boss)

    if attack_collide(character, boss):
        if character.attackstate:
            if not character.attack_damage and boss.hitstate == False:
                boss.w += -1.5
                boss.hp_x += -0.725
                boss.hp -= 1
                character.attack_damage = True
                boss.hitstate = True
                if boss.hp <= 0:
                    game_world.remove_object(boss)


def draw():
    global image
    clear_canvas()
    image.draw(MAP_WIDTH // 2, MAP_HEIGHT // 2)
    boss.draw()
    character.draw()
    key.draw(1700, 50)
    update_canvas()
    delay(0.05)
# open_canvas(MAP_WIDTH, MAP_HEIGHT)
