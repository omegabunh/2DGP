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

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SHIFT_DOWN, SHIFT_UP, ALT_DOWN, HOME_UP, CTRL_DOWN, CTRL_UP, DOWN_DOWN, DOWN_UP = range(
    12)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYDOWN, SDLK_LSHIFT): SHIFT_DOWN,
    (SDL_KEYDOWN, SDLK_LALT): ALT_DOWN,
    (SDL_KEYDOWN, SDLK_LCTRL): CTRL_DOWN,
    (SDL_KEYUP, SDLK_LSHIFT): SHIFT_UP,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_LCTRL): CTRL_UP,
    (SDL_KEYUP, SDLK_HOME): HOME_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP

}


class IdleState:

    @staticmethod
    def enter(character, event):

        if event == RIGHT_DOWN:
            character.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            character.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            character.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            character.velocity += RUN_SPEED_PPS
        character.timer = 300

    @staticmethod
    def exit(character, event):
        if event == ALT_DOWN:
            character.jump()
            character.jumpSound()
            character.jumping = True
            character.idleing = False

    @staticmethod
    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        character.timer -= 1
        character.idleing = True
        character.idlestate = True

    @staticmethod
    def draw(character):
        if character.idlestate:
            draw_rectangle(*character.get_idle_collide())
            if character.dir == 1 and character.idleing:
                character.idle.clip_draw(int(character.frame) * 92, 0 * 96, 92, 96, character.x, character.y)
            elif character.dir == 1 and character.idleing == False:
                character.idle.clip_draw(int(character.frame) * 92, 4 * 96, 92, 96, character.x, character.y)

            elif character.dir == -1 and character.idleing:
                character.idle.clip_draw(int(character.frame) * 92, 1 * 96, 92, 96, character.x, character.y)
            elif character.dir == -1 and character.idleing == False:
                character.idle.clip_draw(int(character.frame) * 92, 5 * 96, 92, 96, character.x, character.y)


class RunState:

    @staticmethod
    def enter(character, event):
        if event == RIGHT_DOWN:
            character.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            character.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            character.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            character.velocity += RUN_SPEED_PPS
        character.dir = clamp(-1, character.velocity, 1)

    @staticmethod
    def exit(character, event):
        if event == ALT_DOWN:
            character.jumpSound()
            character.jump()
            character.jumping = True
            character.running = False

    @staticmethod
    def do(character):
        draw_rectangle(*character.get_idle_collide())
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        character.x += character.velocity * game_framework.frame_time
        character.x = clamp(25, character.x, 1600 - 25)
        character.running = True
        character.runstate = True

    @staticmethod
    def draw(character):
        if character.runstate:
            draw_rectangle(*character.get_idle_collide())
            if character.dir == 1 and character.running:
                character.idle.clip_draw(int(character.frame) * 92, 2 * 96, 92, 96, character.x, character.y)
            elif character.dir == 1 and character.running == False:
                character.idle.clip_draw(int(character.frame) * 92, 4 * 96, 92, 96, character.x, character.y)

            elif character.dir == -1 and character.running:
                character.idle.clip_draw(int(character.frame) * 92, 3 * 96, 92, 96, character.x, character.y)
            elif character.dir == -1 and character.running == False:
                character.idle.clip_draw(int(character.frame) * 92, 5 * 96, 92, 96, character.x, character.y)


class ProneState:
    @staticmethod
    def enter(character, event):
        character.frame = 0

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        character.pronestate = True

    @staticmethod
    def draw(character):
        if character.pronestate:
            draw_rectangle(*character.get_prone_collide())
            if character.dir == 1:
                character.prone.clip_draw(int(character.frame) * 140, 1 * 55, 140, 55, character.x, character.y - 15)
            else:
                character.prone.clip_draw(int(character.frame) * 140, 0 * 55, 140, 55, character.x, character.y - 15)


class AttackState:
    @staticmethod
    def enter(character, event):
        character.frame = 0

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION2 * ACTION_PER_TIME * game_framework.frame_time) % 3
        character.attackstate = True

    @staticmethod
    def draw(character):
        if character.attackstate:
            draw_rectangle(*character.get_attack_collide())
            if character.dir == 1:
                character.attack.clip_draw(int(character.frame) * 260, 1 * 172, 260, 172, character.x, character.y + 23)
            else:
                character.attack.clip_draw(int(character.frame) * 260, 0 * 172, 260, 172, character.x, character.y + 23)


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
        character.skillstate = True

    @staticmethod
    def draw(character):
        if character.skillstate:
            draw_rectangle(*character.get_skill_collide())
            if character.dir == 1 and count % 2 == 0:
                character.skill.clip_draw(int(character.frame1) * 457, 0 * 260, 457, 260, character.x, character.y + 70)
            elif character.dir != 1 and count % 2 == 0:
                character.skill.clip_draw(int(character.frame1) * 457, 1 * 260, 457, 260, character.x, character.y + 70)
            if character.dir == 1 and count % 2 == 1:
                character.skill2.clip_draw(int(character.frame1) * 572, 0 * 406, 573, 406, character.x,
                                           character.y + 40)
            elif character.dir != 1 and count % 2 == 1:
                character.skill2.clip_draw(int(character.frame1) * 572, 1 * 406, 573, 406, character.x,
                                           character.y + 40)


next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SHIFT_UP: IdleState, SHIFT_DOWN: SkillState, DOWN_DOWN: ProneState, DOWN_UP: IdleState,
                ALT_DOWN: IdleState, CTRL_UP: IdleState, CTRL_DOWN: AttackState, HOME_UP: IdleState
                },
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, CTRL_UP: IdleState,
               CTRL_DOWN: AttackState, ALT_DOWN: RunState, DOWN_DOWN: ProneState, DOWN_UP: IdleState,
               HOME_UP: IdleState, SHIFT_UP: IdleState, SHIFT_DOWN: SkillState,
               },
    ProneState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                 SHIFT_UP: IdleState,
                 SHIFT_DOWN: SkillState, DOWN_DOWN: ProneState, DOWN_UP: IdleState, CTRL_UP: IdleState,
                 CTRL_DOWN: AttackState, ALT_DOWN: IdleState, HOME_UP: IdleState
                 },
    AttackState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                  SHIFT_UP: IdleState, SHIFT_DOWN: SkillState, ALT_DOWN: IdleState,
                  DOWN_DOWN: ProneState, DOWN_UP: IdleState, CTRL_UP: IdleState, CTRL_DOWN: AttackState,
                  HOME_UP: IdleState
                  },
    SkillState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                 SHIFT_UP: IdleState,
                 SHIFT_DOWN: SkillState, ALT_DOWN: IdleState, DOWN_DOWN: ProneState,
                 DOWN_UP: IdleState, CTRL_UP: IdleState, CTRL_DOWN: AttackState, HOME_UP: IdleState
                 },
}


class Character:
    idle = None
    attack = None
    prone = None
    skill = None
    skill2 = None

    def __init__(self):
        self.x, self.y = 1700 // 2, 170
        self.frame = 0
        self.dir = 1
        self.jump_force = 300
        self.up = 0
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.jump_y = 0
        self.jumping = False
        self.idleing = True
        self.running = True
        self.idlestate = False
        self.runstate = False
        self.pronestate = False
        self.attackstate = False
        self.skillstate = False
        self.event_que = []
        self.cur_state = IdleState
        self.jump_sound = load_wav('music//Jump.wav')
        self.jump_sound.set_volume(70)
        self.skill_sound = load_wav('music//UseSkill.wav')
        self.skill_sound.set_volume(70)

        self.cur_state.enter(self, None)
        if Character.idle is None:
            Character.idle = load_image('sprite//character.png')
        if Character.attack is None:
            Character.attack = load_image('sprite//character_attack.png')
        if Character.prone is None:
            Character.prone = load_image('sprite//character_prone.png')
        if Character.skill is None:
            Character.skill = load_image('sprite//character_skill(457x260).png')
        if Character.skill2 is None:
            Character.skill2 = load_image('sprite//character_skill2(572x406).png')

    def get_idle_collide(self):
        if self.idlestate:
            return self.x - 30, self.y - 38, self.x + 20, self.y + 42

    def get_prone_collide(self):
        if self.pronestate:
            if self.dir == 1:
                return self.x - 70, self.y - 38, self.x + 10, self.y + 20
            else:
                return self.x - 10, self.y - 38, self.x + 70, self.y + 20

    def get_attack_collide(self):
        if self.attackstate:
            if self.dir == 1:
                return self.x - 50, self.y - 38, self.x + 120, self.y + 100
            else:
                return self.x - 120, self.y - 38, self.x + 50, self.y + 100

    def get_skill_collide(self):
        if self.skillstate:
            if self.dir == 1:
                return self.x - 50, self.y - 38, self.x + 280, self.y + 200
            else:
                return self.x - 280, self.y - 38, self.x + 50, self.y + 200

    def jump(self):
        if self.jumping:
            self.jump_y = self.jump_force
            self.jumping = False

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        if self.jumping:
            self.y += self.jump_y * game_framework.frame_time
            self.jump_y -= GRAVITY_PPS * game_framework.frame_time
            self.y = clamp(170, self.jump_y, 300)

        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        # draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        global count
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        elif event.key == SDLK_HOME:
            count += 1

    def jumpSound(self):
        self.jump_sound.play()

    def skillSound(self):
        self.skill_sound.play()
