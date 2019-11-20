from pico2d import *
import game_framework
import main_state
import game_world
from character2 import Character
from boss2 import Boss
MAP_WIDTH, MAP_HEIGHT = 1997, 950

boss2 = None
monster = None
character = None
monsters = None
key = None
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
    global boss2, monster, character
    image = load_image('map3.png')
    key = load_image('key.png')
    boss2 = Boss()
    character = Character()
    game_world.add_object(image, 0)
    game_world.add_object(key, 1)
    game_world.add_object(character, 1)
    game_world.add_object(boss2, 1)

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
    boss2.update()
    character.update()

def draw():
    global image
    clear_canvas()
    image.draw(MAP_WIDTH // 2, MAP_HEIGHT // 2)
    boss2.draw()
    character.draw()
    key.draw(1700, 50)
    update_canvas()
    delay(0.05)
#open_canvas(MAP_WIDTH, MAP_HEIGHT)




