import game_framework
from pico2d import *
import main2_state

name = "boss1Clear"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('sprite//boss1clear.jpg')


def exit():
    global image
    del(image)


def update():
    global logo_time

    if (logo_time > 2.0):
        logo_time = 0
        # game_framework.quit()
        game_framework.change_state(main2_state)
    delay(0.01)
    logo_time += 0.01



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

def pause(): pass


def resume(): pass




