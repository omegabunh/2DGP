import game_framework
import pico2d

import start_state

pico2d.open_canvas(1748, 950)
game_framework.run(start_state)
pico2d.close_canvas()
