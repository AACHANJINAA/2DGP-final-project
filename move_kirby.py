from pico2d import*
import game_framework

RD, LD, RU, LU, JD, AD, TIMER = range(7)
event_name = ['RD', 'LD', 'RU', 'LU', 'JD', 'AD', 'TIMER']

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 2.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

key_event_table = {
    (SDL_KEYUP, SDLK_a): AD,
    (SDL_KEYDOWN, SDLK_UP): JD,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}


class IDLE:
    @staticmethod
    def enter(self, event):
        self.dir_x = 0
        self.timer = 310

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)

    @staticmethod
    def draw(self):
        match self.mode:
            case 0:
                if self.face_dir_x == -1:
                    self.Idle[self.mode].clip_composite_draw(int(self.frame) * 23, 0, 22, 18,
                                                             0.0, '', self.x, self.y, self.kx, self.ky)
                else:
                    self.Idle[self.mode].clip_composite_draw(int(self.frame) * 23, 0, 22, 18,
                                                             0.0, 'h', self.x, self.y, self.kx, self.ky)
            case 1:
                if self.face_dir_x == -1:
                    self.Idle[self.mode].clip_composite_draw(int(self.frame) * 31, 0, 31, 28,
                                                             0.0, 'h', self.x, self.y, self.kx, self.ky)
                else:
                    self.Idle[self.mode].clip_composite_draw(int(self.frame) * 31, 0, 31, 28,
                                                             0.0, '', self.x, self.y, self.kx, self.ky)
            case 2:
                if self.face_dir_x == -1:
                    self.Idle[self.mode].clip_composite_draw(int(self.frame) * 23, 0, 23, 30,
                                                             0.0, 'h', self.x, self.y, self.kx, self.ky)
                else:
                    self.Idle[self.mode].clip_composite_draw(int(self.frame) * 23, 0, 23, 30,
                                                             0.0, '', self.x, self.y, self.kx, self.ky)
            case 3:
                if self.face_dir_x == -1:
                    self.Idle[self.mode].clip_composite_draw(int(self.frame) * 31, 0, 31, 28,
                                                             0.0, 'h', self.x, self.y, self.kx, self.ky)
                else:
                    self.Idle[self.mode].clip_composite_draw(int(self.frame) * 31, 0, 31, 28,
                                                             0.0, '', self.x, self.y, self.kx, self.ky)


class RUN:
    @staticmethod
    def enter(self, event):
        if event == RD:
            self.dir_x += 1
        elif event == LD:
            self.dir_x -= 1
        elif event == RU:
            self.dir_x -= 1
        elif event == LU:
            self.dir_x += 1

    @staticmethod
    def exit(self, event):
        self.face_dir_x = self.dir_x

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.x += self.dir_x * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 800)

    @staticmethod
    def draw(self):
        match self.mode:
            case 0:
                if self.dir_x == -1:
                    self.Run[self.mode].clip_composite_draw(int(self.frame) * 22, 0, 22, 20,
                                                            0.0, '', self.x, self.y, self.kx, self.ky)
                else:
                    self.Run[self.mode].clip_composite_draw(int(self.frame) * 22, 0, 22, 20,
                                                            0.0, 'h', self.x, self.y, self.kx, self.ky)
            case 1:
                if self.dir_x == -1:
                    self.Run[self.mode].clip_composite_draw(int(self.frame) * 30, 0, 30, 30,
                                                            0.0, 'h', self.x, self.y, self.kx, self.ky)
                else:
                    self.Run[self.mode].clip_composite_draw(int(self.frame) * 30, 0, 30, 30,
                                                            0.0, '', self.x, self.y, self.kx, self.ky)
            case 2:
                if self.dir_x == -1:
                    self.Run[self.mode].clip_composite_draw(int(self.frame) * 29, 0, 29, 30,
                                                            0.0, 'h', self.x, self.y, self.kx, self.ky)
                else:
                    self.Run[self.mode].clip_composite_draw(int(self.frame) * 29, 0, 29, 30,
                                                            0.0, '', self.x, self.y, self.kx, self.ky)
            case 3:
                if self.dir_x == -1:
                    self.Run[self.mode].clip_composite_draw(int(self.frame) * 30, 0, 30, 30,
                                                            0.0, 'h', self.x, self.y, self.kx, self.ky)
                else:
                    self.Run[self.mode].clip_composite_draw(int(self.frame) * 30, 0, 30, 30,
                                                            0.0, '', self.x, self.y, self.kx, self.ky)


class JUMP:
    @staticmethod
    def enter(self, event):
        if event == JD:
            self.timer = 310
            self.s_timer = self.timer // 2

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        if self.timer == self.s_timer:
            self.dir_y = -1
        elif self.timer == 0:
            self.dir_y = 1
            self.add_event(TIMER)
        match self.mode:
            case 0:
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
            case 1:
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            case 2:
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
            case 3:
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        jump_dis = self.dir_y * RUN_SPEED_PPS * game_framework.frame_time
        self.y += jump_dis * 1.5
        self.x += self.face_dir_x / 1.5
        self.x = clamp(0, self.x, 800)
        self.timer -= 1

    @staticmethod
    def draw(self):
        match self.mode:
            case 0:
                if self.face_dir_x == -1:
                    self.Jump[self.mode].clip_composite_draw(int(self.frame) * 25, 0, 25, 22,
                                                             0.0, '', self.x, self.y, self.kx, self.ky)
                else:
                    self.Jump[self.mode].clip_composite_draw(int(self.frame) * 25, 0, 25, 22,
                                                             0.0, 'h', self.x, self.y, self.kx, self.ky)
            case 1:
                if self.face_dir_x == -1:
                    self.Jump[self.mode].clip_composite_draw(int(self.frame) * 28, 0, 28, 34,
                                                             0.0, 'h', self.x, self.y, self.kx, self.ky)
                else:
                    self.Jump[self.mode].clip_composite_draw(int(self.frame) * 28, 0, 28, 34,
                                                             0.0, '', self.x, self.y, self.kx, self.ky)
            case 2:
                if self.face_dir_x == -1:
                    self.Jump[self.mode].clip_composite_draw(int(self.frame) * 24, 0, 24, 34,
                                                             0.0, 'h', self.x, self.y, self.kx, self.ky)
                else:
                    self.Jump[self.mode].clip_composite_draw(int(self.frame) * 24, 0, 24, 34,
                                                             0.0, '', self.x, self.y, self.kx, self.ky)
            case 3:
                if self.face_dir_x == -1:
                    self.Jump[self.mode].clip_composite_draw(int(self.frame) * 28, 0, 28, 34,
                                                             0.0, 'h', self.x, self.y, self.kx, self.ky)
                else:
                    self.Jump[self.mode].clip_composite_draw(int(self.frame) * 28, 0, 28, 34,
                                                             0.0, '', self.x, self.y, self.kx, self.ky)


class SKILL:
    @staticmethod
    def enter(self, event):
        if event == AD:
            match self.mode:
                case 0:
                    self.timer = 310
                case 1:
                    self.timer = 200
                case 2:
                    self.timer = 420
                case 3:
                    if event == AD:
                        self.move_pos = 24
                        self.mp = 0
                        self.pos_boom = self.x
                        self.move_boom = 0

    @staticmethod
    def exit(self, event):
        self.mode = 3

    @staticmethod
    def do(self):
        match self.mode:
            case 0:
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 9
                self.timer -= 1
                if self.timer == 0:
                    self.add_event(TIMER)
            case 1:
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
                self.timer -= 1
                if self.timer == 0:
                    self.add_event(TIMER)
            case 2:
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
                self.timer -= 1
                if self.timer == 0:
                    self.add_event(TIMER)
            case 3:
                self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
                self.move_boom += 2 * RUN_SPEED_PPS * game_framework.frame_time
                if int(self.frame) == 1:
                    self.move_pos = 33
                    self.mp = 24
                elif int(self.frame) == 2:
                    self.move_pos = 38
                    self.mp = 24 + 33
                else:
                    self.move_pos = 24
                    self.mp = 0

    @staticmethod
    def draw(self):
        match self.mode:
            case 0:
                if self.face_dir_x == -1:
                    self.Skill[self.mode].clip_composite_draw(int(self.frame) * 30, 0, 30, 22,
                                                              0.0, '', self.x, self.y, self.kx + 3, self.ky + 3)
                else:
                    self.Skill[self.mode].clip_composite_draw(int(self.frame) * 30, 0, 30, 22,
                                                              0.0, 'h', self.x, self.y, self.kx + 3, self.ky + 3)
            case 1:
                if self.face_dir_x == -1:
                    self.Skill[self.mode].clip_composite_draw(int(self.frame) * 56, 0, 56, 31,
                                                              0.0, 'h', self.x, self.y, self.kx + 50, self.ky)
                    self.Effect[self.mode - 1].clip_composite_draw(0, 0, 38, 40,
                                                                   0.0, 'h', self.x - 90, self.y + 10, self.kx - 5, self.ky + 10)
                else:
                    self.Skill[self.mode].clip_composite_draw(int(self.frame) * 56, 0, 56, 31,
                                                              0.0, '', self.x, self.y, self.kx + 50, self.ky)
                    self.Effect[self.mode - 1].clip_composite_draw(0, 0, 38, 40,
                                                                   0.0, '', self.x + 90, self.y + 10, self.kx + 5, self.ky + 10)
            case 2:
                if self.face_dir_x == -1:
                    self.Effect[self.mode - 1].clip_composite_draw(0, 0, 64, 64,
                                                                   0.0, 'h', self.x, self.y, self.kx * 2, self.ky * 2)
                    self.Skill[self.mode].clip_composite_draw(int(self.frame) * 22, 0, 22, 34,
                                                              0.0, 'h', self.x, self.y, self.kx, self.ky)
                else:
                    self.Effect[self.mode - 1].clip_composite_draw(0, 0, 64, 64,
                                                                   0.0, '', self.x, self.y, self.kx * 2, self.ky * 2)
                    self.Skill[self.mode].clip_composite_draw(int(self.frame) * 22, 0, 22, 34,
                                                              0.0, '', self.x, self.y, self.kx, self.ky)
            case 3:
                if self.face_dir_x == -1:
                    self.Effect[self.mode - 1].clip_composite_draw(int(self.frame + 1) * 23, 0, 23, 29,
                                                                   0.0, 'h', self.pos_boom - self.move_boom, self.y, self.kx, self.ky)
                    self.Skill[self.mode].clip_composite_draw(self.mp, 0, self.move_pos, 34,
                                                              0.0, 'h', self.x, self.y, self.kx, self.ky)
                else:
                    self.Effect[self.mode - 1].clip_composite_draw(int(self.frame + 1) * 23, 0, 23, 29,
                                                                   0.0, '', self.pos_boom + self.move_boom, self.y, self.kx, self.ky)
                    self.Skill[self.mode].clip_composite_draw(self.mp, 0, self.move_pos, 34,
                                                              0.0, '', self.x, self.y, self.kx, self.ky)


class SLEEP:
    @staticmethod
    def enter(self, event):
        self.frame = 0

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    @staticmethod
    def draw(self):
        if self.face_dir_x == -1:
            self.Sleep.clip_composite_draw(int(self.frame) * 30, 0, 30, 18,
                                           0.0, '', self.x, self.y, self.kx, self.ky)
        else:
            self.Sleep.clip_composite_draw(int(self.frame) * 30, 0, 30, 18,
                                           0.0, 'h', self.x, self.y, self.kx, self.ky)


next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN,  JD: JUMP, TIMER: SLEEP, AD: SKILL},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, JD: JUMP, TIMER: IDLE,  AD: SKILL},
    SLEEP: {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN,  JD: IDLE, TIMER: IDLE,  AD: IDLE},
    JUMP:  {RU: JUMP, LU: JUMP, RD: JUMP, LD: JUMP, JD: JUMP, TIMER: IDLE,  AD: JUMP},
    SKILL: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, JD: JUMP, TIMER: IDLE, AD: SKILL}
}


class Kirby:
    def __init__(self):
        self.mode = 0

        self.move_pos = 0
        self.mp = 0
        self.pos_boom = 0
        self.move_boom = 0

        self.x, self.y = 30, 100
        self.kx, self.ky = 70, 55
        self.face_dir_x, self.dir_x = 1, 0
        self.dir_y = 1
        self.frame = 0
        self.timer = 0
        self.s_timer = 0

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

        self.Idle = [load_image('kirby/kirby_idle.png'), load_image('kirby(sword)/kirby(sword)_idle.png'),
                     load_image('kirby(spark)/kirby(spark)_idle.png'),
                     load_image('kirby(bomber)/kirby(bomber)_idle.png')]
        self.Run = [load_image('kirby/kirby_run.png'), load_image('kirby(sword)/kirby(sword)_run.png'),
                    load_image('kirby(spark)/kirby(spark)_run.png'),
                    load_image('kirby(bomber)/kirby(bomber)_run.png')]
        self.Jump = [load_image('kirby/kirby_jump.png'), load_image('kirby(sword)/kirby(sword)_jump.png'),
                     load_image('kirby(spark)/kirby(spark)_jump.png'),
                     load_image('kirby(bomber)/kirby(bomber)_jump.png')]
        self.Skill = [load_image('kirby/kirby_skill.png'), load_image('kirby(sword)/kirby(sword)_skill.png'),
                      load_image('kirby(spark)/kirby(spark)_skill.png'),
                      load_image('kirby(bomber)/kirby(bomber)_skill.png')]
        self.Effect = [load_image('kirby(sword)/kirby(sword)_skill_effect.png'),
                       load_image('kirby(spark)/kirby(spark)_skill_effect.png'),
                       load_image('kirby(bomber)/kirby(bomber)_skill_effect.png')]
        self.Sleep = load_image('kirby/kirby_sleep.png')
    def update(self):
        self.cur_state.do(self)
        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print('ERROR', self.cur_state.__name__, ' ', event_name[event])

            self.cur_state.enter(self, event)
    def draw(self):
        self.cur_state.draw(self)
        debug_print('PPPP')
        debug_print(f'Face Dir: {self.face_dir_x}, Dir: {self.dir_x}')
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25