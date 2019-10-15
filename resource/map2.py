from pico2d import *
import random
MAP_WIDTH, MAP_HEIGHT = 1997, 950
class Boss:
    def __init__(self):
        self.x, self.y = 1070, 470
        self.frame = 0
        self.image = load_image('boss_phase1(248x245).png')
    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 248, 0, 248, 245, self.x, self.y)

class Monster:
    def __init__(self):
        self.x, self.y = random.randint(0, 1748), 800
        self.frame = 0
        self.image = load_image('monster(191x224).png')
    def update(self):
        self.frame = random.randint(0, 5)
        if self.y > 330:
            self.y -= 50
        elif self.y < 330:
            self.y = 330
    def draw(self):
        self.image.clip_draw(self.frame * 191, 0, 191, 224, self.x, self.y)
def character_handle_events():
    global running
    global dir_x
    global dir_y
    global side_1
    global side_2
    global side_3
    global attack
    global prone
    global jumpstate
    global jumpforce

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 2
                side_1 = 2
            elif event.key == SDLK_LEFT:
                dir_x -= 2
                side_1 = 3
            elif event.key == SDLK_DOWN:
                prone = True
                if side_1 == 0:
                    side_3 = 1
                elif side_1 == 1:
                    side_3 = 0
            elif event.key == SDLK_LALT and jumpstate == False:
                if side_1 == 0:
                    jumpstate = True
                    jumpforce = 60
                    side_1 = 4
                elif side_1 == 1:
                    jumpstate = True
                    jumpforce = 60
                    side_1 = 5

            elif event.key == SDLK_LCTRL:
                attack = True
                if side_1 == 0:
                    side_2 = 1
                elif side_1 == 1:
                    side_2 = 0
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 2
                side_1 = 0
            elif event.key == SDLK_LEFT:
                dir_x += 2
                side_1 = 1
            elif event.key == SDLK_DOWN:
                prone = False
                if side_3 == 1:
                    side_1 = 0
                elif side_3 == 0:
                    side_1 = 1
            elif event.key == SDLK_LALT and jumpstate == True:
                if side_1 == 4:
                    side_1 = 0
                elif side_1 == 5:
                    side_1 = 1
            elif event.key == SDLK_LCTRL:
                attack = False
                if side_2 == 0:
                    side_1 = 1
                elif side_2 == 1:
                    side_1 = 0

    pass

open_canvas(MAP_WIDTH, MAP_HEIGHT)
map1 = load_image('map2.png')
character = load_image('character.png')
character_attack = load_image('character_attack.png')
character_prone = load_image('character_prone.png')


attack = False
prone = False
running = True
x = 100
y = 285
boss = Boss()
frame_character = 0
dir_x = 0
dir_y = 0
side_1 = 0
side_2 = 0
side_3 = 0
jumpstate = False
jumpforce = 0
t = random.randint(1, 4)
monsters = [Monster() for i in range(t)]
while running:
    boss.update()
    for monster in monsters:
        monster.update()
    clear_canvas()


    map1.draw(MAP_WIDTH//2, MAP_HEIGHT//2)
    for monster in monsters:
        monster.draw()
    boss.draw()
    if attack == False:
        if prone == False:
            character.clip_draw(frame_character * 92, side_1 * 96, 92, 96, x, y)
    elif attack == True:
        if prone == False:
            character_attack.clip_draw(frame_character * 260, side_2 * 172, 260, 172, x, y+23)
    if prone == True:
        character_prone.clip_draw(frame_character * 140, side_3 * 55, 140, 55, x, y - 15)


    update_canvas()



    character_handle_events()

    frame_character = (frame_character + 1) % 4
    x += dir_x * 5

    if jumpstate == True:
        y = 285 + jumpforce
        jumpforce -=8
        print(jumpforce)
        if y <= 285:
            jumpstate = False
            y = 285

    delay(0.05)

close_canvas()