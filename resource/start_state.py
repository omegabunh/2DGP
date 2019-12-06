import game_framework
from pico2d import *
import title_state
from map0 import Map
import game_world

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global map2
    map2 = Map()
    game_world.add_object(map2, 0)

def exit():
    game_world.clear()


def update():
    global logo_time

    if(logo_time > 2.0):
        logo_time = 0
        #game_framework.quit()
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01



def draw():
    clear_canvas()
    map2.image.draw(1748 // 2, 950 // 2)
    update_canvas()

def handle_events():
    events = get_events()
    pass

def pause(): pass


def resume(): pass




