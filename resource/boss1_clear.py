import game_framework
from pico2d import *
import main2_state
import game_world
from clear1 import Map
name = "boss1Clear"
image = None
logo_time = 0.0


def enter():
    global map
    map = Map()
    game_world.add_object(map, 0)


def exit():
    game_world.clear()

def update():
    global logo_time

    if (logo_time > 0.12):
        logo_time = 0
        # game_framework.quit()
        game_framework.change_state(main2_state)
    delay(0.01)
    logo_time += 0.01 * game_framework.frame_time



def draw():
    clear_canvas()
    map.image.draw(1748//2, 950//2)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

def pause(): pass


def resume(): pass




