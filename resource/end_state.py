import game_framework
from pico2d import *
import game_world

name = "endState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('sprite//gameclear.png')
    game_world.add_object(image, 0)

def exit():
    game_world.clear()

def update():
   pass



def draw():
    clear_canvas()
    image.draw(1748//2, 950//2)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
            game_framework.quit()

def pause(): pass


def resume(): pass




