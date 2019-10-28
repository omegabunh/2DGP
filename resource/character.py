from pico2d import *

count = 0
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SHIFT_DOWN, SHIFT_UP, ALT_DOWN, ALT_UP, HOME_DOWN, HOME_UP, CTRL_DOWN, CTRL_UP, DOWN_DOWN, DOWN_UP = range(14)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYDOWN, SDLK_LSHIFT): SHIFT_DOWN,
    (SDL_KEYDOWN, SDLK_LALT): ALT_DOWN,
    (SDL_KEYDOWN, SDLK_LCTRL): CTRL_DOWN,
    (SDL_KEYDOWN, SDLK_HOME): HOME_DOWN,
    (SDL_KEYUP, SDLK_LSHIFT): SHIFT_UP,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_LALT): ALT_UP,
    (SDL_KEYUP, SDLK_LCTRL): CTRL_UP,
    (SDL_KEYUP, SDLK_HOME): HOME_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP

}

class IdleState:

    @staticmethod
    def enter(character, event):
        if event == RIGHT_DOWN:
            character.velocity += 1
        elif event == LEFT_DOWN:
            character.velocity -= 1
        elif event == RIGHT_UP:
            character.velocity -= 1
        elif event == LEFT_UP:
            character.velocity += 1
        character.timer = 300

    @staticmethod
    def exit(character, event):
        # fill here
        pass

    @staticmethod
    def do(character):
        character.frame = (character.frame + 1) % 4
        character.timer -= 1


    @staticmethod
    def draw(character):
        if character.dir == 1:
            character.idle.clip_draw(character.frame * 92, 0 * 96, 92, 96, character.x, character.y)
        else:
            character.idle.clip_draw(character.frame * 92, 1 * 96, 92, 96, character.x, character.y)

class RunState:

    @staticmethod
    def enter(character, event):
        if event == RIGHT_DOWN:
            character.velocity += 1
        elif event == LEFT_DOWN:
            character.velocity -= 1
        elif event == RIGHT_UP:
            character.velocity -= 1
        elif event == LEFT_UP:
            character.velocity += 1
        character.dir = character.velocity

    @staticmethod
    def exit(character, event):
        # fill here
        pass

    @staticmethod
    def do(character):
        character.frame = (character.frame + 1) % 4
        character.timer -= 1
        character.x += character.velocity
        character.x = clamp(25, character.x, 1600 - 25)

    @staticmethod
    def draw(character):
        if character.velocity == 1:
            character.idle.clip_draw(character.frame * 92, 2 * 96, 92, 96, character.x, character.y)
        else:
            character.idle.clip_draw(character.frame * 92, 3 * 96, 92, 96, character.x, character.y)

class ProneState:
    @staticmethod
    def enter(character, event):
        character.frame = 0
    @staticmethod
    def exit(character, event):
        pass
    @staticmethod
    def do(character):
        character.frame = (character.frame + 1) % 4
    @staticmethod
    def draw(character):
        if character.dir == 1:
            character.prone.clip_draw(character.frame * 140, 1 * 55, 140, 55, character.x, character.y - 15)
        else:
            character.prone.clip_draw(character.frame * 140, 0 * 55, 140, 55, character.x, character.y - 15)

class JumpState:
    @staticmethod
    def enter(character, event):
        if event == ALT_DOWN:
            character.up += 100
        elif event == ALT_UP:
            character.up -= 100

        character.jump_force = character.up

    @staticmethod
    def exit(character, event):
        # fill here
        pass

    @staticmethod
    def do(character):
        character.frame = (character.frame + 1) % 4
        character.timer -= 1
        character.y = character.up
        character.y = clamp(170, character.y, 270)

    @staticmethod
    def draw(character):
        if character.dir == 1:
            character.idle.clip_draw(character.frame * 92, 4 * 96, 92, 96, character.x, character.y)
        else:
            character.idle.clip_draw(character.frame * 92, 5 * 96, 92, 96, character.x, character.y)

class AttackState:
    @staticmethod
    def enter(character, event):
        character.frame = 0
    @staticmethod
    def exit(character, event):
        pass
    @staticmethod
    def do(character):
        character.frame = (character.frame + 1) % 3
    @staticmethod
    def draw(character):
        if character.dir == 1:
            character.attack.clip_draw(character.frame * 260, 1 * 172, 260, 172, character.x, character.y + 23)
        else:
            character.attack.clip_draw(character.frame * 260, 0 * 172, 260, 172, character.x, character.y + 23)

class SkillState:
    @staticmethod
    def enter(character, event):
        character.frame1 = 0

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        character.frame1 = (character.frame1 + 1) % 14

    @staticmethod
    def draw(character):
        if character.dir == 1 and count % 2 == 0:
            character.skill.clip_draw(character.frame1 * 457, 0 * 260, 457, 260, character.x, character.y + 70)
        elif character.dir != 1 and count % 2 == 0:
            character.skill.clip_draw(character.frame1 * 457, 1 * 260, 457, 260, character.x, character.y + 70)
        if character.dir == 1 and count % 2 == 1:
            character.skill2.clip_draw(character.frame1 * 572, 0 * 406, 573, 406, character.x, character.y + 40)
        elif character.dir != 1 and count % 2 ==1:
            character.skill2.clip_draw(character.frame1 * 572, 1 * 406, 573, 406, character.x, character.y + 40)

next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState,
                LEFT_DOWN: RunState, SHIFT_UP: IdleState, SHIFT_DOWN: SkillState,
                DOWN_DOWN: ProneState, DOWN_UP: IdleState, ALT_UP: IdleState, ALT_DOWN: JumpState,
                CTRL_UP: IdleState, CTRL_DOWN: AttackState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState,
               RIGHT_DOWN: IdleState, CTRL_UP: IdleState, CTRL_DOWN: AttackState,ALT_UP: IdleState, ALT_DOWN: JumpState,
               DOWN_DOWN: ProneState, DOWN_UP: IdleState},
    ProneState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState,
                LEFT_DOWN: RunState, SHIFT_UP: IdleState, SHIFT_DOWN: SkillState,
                DOWN_DOWN: ProneState, DOWN_UP: IdleState,  CTRL_UP: IdleState, CTRL_DOWN: AttackState,
                 ALT_UP: IdleState, ALT_DOWN: JumpState, },
    AttackState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState,
                LEFT_DOWN: RunState, SHIFT_UP: IdleState, SHIFT_DOWN: SkillState,ALT_UP: IdleState, ALT_DOWN: JumpState,
                DOWN_DOWN: ProneState, DOWN_UP: IdleState, CTRL_UP: IdleState, CTRL_DOWN: AttackState},
    SkillState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState,
                LEFT_DOWN: RunState, SHIFT_UP: IdleState, SHIFT_DOWN: SkillState,ALT_UP: IdleState, ALT_DOWN: JumpState,
                DOWN_DOWN: ProneState, DOWN_UP: IdleState,  CTRL_UP: IdleState, CTRL_DOWN: AttackState,
                 },
    JumpState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState,
                LEFT_DOWN: RunState, SHIFT_UP: IdleState, SHIFT_DOWN: SkillState, ALT_UP: IdleState, ALT_DOWN: JumpState,
                DOWN_DOWN: ProneState, DOWN_UP: IdleState,  CTRL_UP: IdleState, CTRL_DOWN: AttackState,
                }
}

class Character:

    def __init__(self):
        self.x, self.y = 1700 // 2, 170
        self.frame = 0
        self.dir = 1
        self.jump_force = 1
        self.up = 0
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        Character.idle = load_image('character.png')
        Character.attack = load_image('character_attack.png')
        Character.prone = load_image('character_prone.png')
        Character.skill = load_image('character_skill(457x260).png')
        Character.skill2 = load_image('character_skill2(572x406).png')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        global count
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        elif event.key == SDLK_HOME:
            count += 1

