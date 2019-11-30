import game_framework
from pico2d import *
import title_state

name = "overState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('sprite//gameover.png')


def exit():
    global image
    del(image)


def update():
   pass



def draw():
    global image
    clear_canvas()
    image.draw(1748//2, 950//2)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)

def pause(): pass


def resume(): pass




