from pico2d import *
import game_framework

count = 0

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

GRAVITY_PPS = (9.8 * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4
FRAMES_PER_ACTION1 = 8
FRAMES_PER_ACTION2 = 3

RIGHT_DOWN, LEFT_DOWN, UPKEY_DOWN, DOWNKEY_DOWN, CTRL_DOWN, SHIFT_DOWN, UPKEY_UP, RIGHT_UP, LEFT_UP, SHIFT_UP, HOME_UP, CTRL_UP, DOWNKEY_UP = range(13)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWNKEY_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UPKEY_DOWN,
    (SDL_KEYDOWN, SDLK_LSHIFT): SHIFT_DOWN,
    (SDL_KEYDOWN, SDLK_LCTRL): CTRL_DOWN,

    (SDL_KEYUP, SDLK_LSHIFT): SHIFT_UP,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UPKEY_UP,
    (SDL_KEYUP, SDLK_LCTRL): CTRL_UP,
    (SDL_KEYUP, SDLK_HOME): HOME_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWNKEY_UP

}


class IdleState:

    @staticmethod
    def enter(character, event):

        if event == RIGHT_DOWN:
            character.velocity += RUN_SPEED_PPS
        elif event == RIGHT_UP:
            character.velocity -= RUN_SPEED_PPS

        if event == LEFT_DOWN:
            character.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            character.velocity += RUN_SPEED_PPS

        if event == UPKEY_DOWN:
            character.velocity_y += RUN_SPEED_PPS
        elif event == UPKEY_UP:
            character.velocity_y -= RUN_SPEED_PPS

        if event == DOWNKEY_DOWN:
            character.velocity_y -= RUN_SPEED_PPS
        elif event == DOWNKEY_UP:
            character.velocity_y += RUN_SPEED_PPS
        character.timer = 300

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        character.timer -= 1
        character.idleing = True
        character.idlestate = True
        character.runstate = False
        character.attackstate = False
        character.skillstate = False


    @staticmethod
    def draw(character):
        cx, cy = character.x - character.bg.window_left, character.y - character.bg.window_bottom
        if character.idlestate:
            #draw_rectangle(*character.get_idle_collide())
            if character.dir == 1:
                character.idle.clip_draw(int(character.frame) * 92, 0 * 96, 92, 96, cx, cy)
            elif character.dir == -1:
                character.idle.clip_draw(int(character.frame) * 92, 1 * 96, 92, 96, cx, cy)



class RunState:

    @staticmethod
    def enter(character, event):
        if event == RIGHT_DOWN:
            character.velocity += RUN_SPEED_PPS
        elif event == RIGHT_UP:
            character.velocity -= RUN_SPEED_PPS

        if event == LEFT_DOWN:
            character.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            character.velocity += RUN_SPEED_PPS

        if event == UPKEY_DOWN:
            character.velocity_y += RUN_SPEED_PPS
        elif event == UPKEY_UP:
            character.velocity_y -= RUN_SPEED_PPS

        if event == DOWNKEY_DOWN:
            character.velocity_y -= RUN_SPEED_PPS
        elif event == DOWNKEY_UP:
            character.velocity_y += RUN_SPEED_PPS

    @staticmethod
    def exit(character, event):
        pass



    @staticmethod
    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        character.x += character.velocity * game_framework.frame_time
        character.y += character.velocity_y * game_framework.frame_time
        character.x = clamp(25, character.x, character.bg.w - 25)
        character.y = clamp(25, character.y, character.bg.h - 25)
        character.running = True
        character.idlestate = False
        character.runstate = True
        character.attackstate = False
        character.skillstate = False

    @staticmethod
    def draw(character):
        cx, cy = character.x - character.bg.window_left, character.y - character.bg.window_bottom
        if character.runstate:
            #draw_rectangle(*character.get_run_collide())
            if character.velocity > 0:
                character.idle.clip_draw(int(character.frame) * 92, 2 * 96, 92, 96, cx, cy)
                character.dir = 1
            elif character.velocity < 0:
                character.idle.clip_draw(int(character.frame) * 92, 3 * 96, 92, 96, cx, cy)
                character.dir = -1
            else:
                if character.velocity_y > 0 or character.velocity_y < 0:
                    if character.dir == 1:
                        character.idle.clip_draw(int(character.frame) * 92, 2 * 96, 92, 96, cx, cy)
                    else:
                        character.idle.clip_draw(int(character.frame) * 92, 3 * 96, 92, 96, cx, cy)


class AttackState:
    @staticmethod
    def enter(character, event):
        character.frame = 0
        character.attackSound()

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION2 * ACTION_PER_TIME * game_framework.frame_time) % 3
        character.idlestate = False
        character.runstate = False
        character.attackstate = True
        character.skillstate = False
        character.pronestate = False

    @staticmethod
    def draw(character):
        cx, cy = character.x - character.bg.window_left, character.y - character.bg.window_bottom
        if character.attackstate:
            #draw_rectangle(*character.get_attack_collide())
            if character.dir == 1:
                character.attack.clip_draw(int(character.frame) * 260, 1 * 172, 260, 172, cx, cy + 23)
            else:
                character.attack.clip_draw(int(character.frame) * 260, 0 * 172, 260, 172, cx, cy + 23)


class SkillState:

    @staticmethod
    def enter(character, event):
        global count
        character.frame1 = 0
        character.skillSound()
        if event == HOME_UP:
            count = count + 1

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        character.frame1 = (character.frame1 + FRAMES_PER_ACTION1 * ACTION_PER_TIME * game_framework.frame_time) % 14
        character.idlestate = False
        character.runstate = False
        character.attackstate = False
        character.skillstate = True
        character.pronestate = False


    @staticmethod
    def draw(character):
        if character.skillstate:
            cx, cy = character.x - character.bg.window_left, character.y - character.bg.window_bottom
            #draw_rectangle(*character.get_skill_collide())
            if character.dir == 1 and count % 2 == 0:
                character.skill.clip_draw(int(character.frame1) * 457, 0 * 260, 457, 260, cx, cy + 70)
            elif character.dir != 1 and count % 2 == 0:
                character.skill.clip_draw(int(character.frame1) * 457, 1 * 260, 457, 260, cx, cy + 70)
            if character.dir == 1 and count % 2 == 1:
                character.skill2.clip_draw(int(character.frame1) * 572, 0 * 406, 573, 406, cx, cy + 40)
            elif character.dir != 1 and count % 2 == 1:
                character.skill2.clip_draw(int(character.frame1) * 572, 1 * 406, 573, 406, cx, cy + 40)


next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SHIFT_UP: IdleState, SHIFT_DOWN: SkillState, DOWNKEY_DOWN: RunState, DOWNKEY_UP: IdleState,
                CTRL_UP: IdleState, CTRL_DOWN: AttackState, HOME_UP: IdleState, UPKEY_DOWN: RunState, UPKEY_UP: IdleState,
                },
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, CTRL_UP: IdleState,
               CTRL_DOWN: AttackState, DOWNKEY_DOWN: RunState, DOWNKEY_UP: IdleState, UPKEY_DOWN: RunState, UPKEY_UP: IdleState,
               HOME_UP: IdleState, SHIFT_UP: IdleState, SHIFT_DOWN: SkillState,
               },
    AttackState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                  SHIFT_UP: IdleState, SHIFT_DOWN: SkillState, UPKEY_DOWN: RunState, UPKEY_UP: IdleState,
                  DOWNKEY_DOWN: RunState, DOWNKEY_UP: IdleState, CTRL_UP: IdleState, CTRL_DOWN: AttackState,
                  HOME_UP: IdleState
                  },
    SkillState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                 SHIFT_UP: IdleState, SHIFT_DOWN: SkillState, DOWNKEY_DOWN: RunState, UPKEY_DOWN: RunState, UPKEY_UP: IdleState,
                 DOWNKEY_UP: IdleState, CTRL_UP: IdleState, CTRL_DOWN: AttackState, HOME_UP: IdleState
                 },
}

class Character:
    idle = None
    attack = None
    prone = None
    skill = None
    skill2 = None
    dead = None
    hp_background = None
    hp_bar = None

    def __init__(self):
        self.frame = 0
        self.dir = 1
        self.jump_force = 430
        self.up = 0
        self.velocity = 0
        self.velocity_y = 0
        self.frame = 0
        self.timer = 0
        self.idleing = True
        self.running = True
        self.idlestate = False
        self.runstate = False
        self.attackstate = False
        self.skillstate = False
        self.deadstate = False
        self.idle_op = False
        self.run_op = False
        self.jump_sound = load_wav('music//Jump.wav')
        self.jump_sound.set_volume(70)
        self.skill_sound = load_wav('music//UseSkill.wav')
        self.skill_sound.set_volume(70)
        self.eat_sound = load_wav('music//Use.wav')
        self.eat_sound.set_volume(70)
        self.attack_sound = load_wav('music//Attack.wav')
        self.attack_sound.set_volume(70)
        self.dead_sound = load_wav('music//Tombstone.wav')
        self.dead_sound.set_volume(80)
        self.idle_op_count, self.run_op_count = 0, 0
        self.font = load_font('Maplestory Bold.ttf', 16)
        self.hp = 1700
        self.hp_x, self.hp_y = 1700 // 2, 25
        self.hp_x1, self.hp_y1 = 1700 // 2 + 8, 25 - 8
        self.w, self.h = 170, 13
        self.skill_damage = False
        self.skill_damage_count = 0
        self.attack_damage = False
        self.attack_damage_count = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        if Character.idle is None:
            Character.idle = load_image('sprite//character.png')
        if Character.attack is None:
            Character.attack = load_image('sprite//character_attack.png')
        if Character.skill is None:
            Character.skill = load_image('sprite//character_skill(457x260).png')
        if Character.skill2 is None:
            Character.skill2 = load_image('sprite//character_skill2(572x406).png')
        if Character.dead is None:
            Character.dead = load_image('sprite//character_dead.png')
        if Character.hp_background is None:
            Character.hp_background = load_image('sprite//character_hp_background.png')
        if Character.hp_bar is None:
            Character.hp_bar = load_image('sprite//character_hp_bar.png')

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2

    def get_idle_collide(self):
        if self.idlestate:
            return self.x - self.bg.window_left - 30, self.y - self.bg.window_bottom - 38, self.x - self.bg.window_left + 20, self.y - self.bg.window_bottom + 42

    def get_run_collide(self):
        if self.runstate:
            return self.x - self.bg.window_left - 30, self.y - self.bg.window_bottom - 38, self.x - self.bg.window_left + 20, self.y - self.bg.window_bottom + 42

    def get_prone_collide(self):
        if self.pronestate:
            if self.dir == 1:
                return self.x - self.bg.window_left - 70, self.y - self.bg.window_bottom - 38, self.x - self.bg.window_left + 10, self.y - self.bg.window_bottom + 20
            else:
                return self.x - self.bg.window_left - 10, self.y - self.bg.window_bottom - 38, self.x - self.bg.window_left + 70, self.y - self.bg.window_bottom + 20

    def get_attack_collide(self):
        if self.attackstate:
            if self.dir == 1:
                return self.x - self.bg.window_left - 50, self.y - self.bg.window_bottom - 38, self.x - self.bg.window_left + 120, self.y - self.bg.window_bottom + 100
            else:
                return self.x - self.bg.window_left - 120, self.y - self.bg.window_bottom - 38, self.x - self.bg.window_left + 50, self.y - self.bg.window_bottom + 100

    def get_skill_collide(self):
        if self.skillstate:
            if self.dir == 1:
                return self.x - self.bg.window_left - 50, self.y - self.bg.window_bottom - 38, self.x - self.bg.window_left + 280, self.y - self.bg.window_bottom + 200
            else:
                return self.x - self.bg.window_left - 280, self.y - self.bg.window_bottom - 38, self.x - self.bg.window_left + 50, self.y - self.bg.window_bottom + 200

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):

        if self.idle_op:
            self.idle_op_count += 1
            self.idle.opacify(0.5)
            if self.idle_op_count % 50 == 0:
                self.idle.opacify(1.0)
            if self.idle_op_count == 150:
                self.idle_op = False
                self.idle_op_count = 0

        if self.run_op:
            self.run_op_count += 1
            self.idle.opacify(0.5)
            if self.run_op_count % 50 == 0:
                self.idle.opacify(1.0)
            if self.run_op_count == 150:
                self.run_op = False
                self.run_op_count = 0

        if self.skill_damage:
            self.skill_damage_count += 1
            if self.skill_damage_count == 14:
                self.skill_damage = False
                self.skill_damage_count = 0

        if self.attack_damage:
            self.attack_damage_count += 1
            if self.attack_damage_count == 12:
                self.attack_damage = False
                self.attack_damage_count = 0

        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        #self.font.draw(self.x - self.bg.window_left - 60, self.y - self.bg.window_bottom + 50, '(hp: %0.0f)' % self.hp, (0, 255, 0))
        if self.deadstate:
            self.dead.draw(self.x, self.y)
            self.deadSound()
        else:
            self.cur_state.draw(self)
        self.hp_bar.draw(self.hp_x1, self.hp_y1, self.w, self.h)
        self.hp_background.draw(self.hp_x, self.hp_y)
    def handle_event(self, event):
        global count
        if (event.type, event.key) in key_event_table and self.deadstate == False:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        elif event.key == SDLK_HOME:
            count += 1
        elif event.key == SDLK_DELETE:
            self.hp = 1700
            self.eatSound()
            self.hp_x1 = 1700 // 2 + 8
            self.w = 170

    def jumpSound(self):
        self.jump_sound.play()

    def skillSound(self):
        self.skill_sound.play()

    def eatSound(self):
        self.eat_sound.play()

    def attackSound(self):
        self.attack_sound.play()

    def deadSound(self):
        self.dead_sound.play()