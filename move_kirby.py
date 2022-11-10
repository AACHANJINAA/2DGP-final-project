from pico2d import*
import game_framework
import game_world

RD, LD, RU, LU, JD, AD, TIMER = range(7)
event_name = ['RD', 'LD', 'RU', 'LU', 'JD', 'AD', 'TIMER']

key_event_table = {
    (SDL_KEYDOWN, SDLK_a): AD,
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
        self.timer = 70

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
        if self.face_dir_x == -1:
            self.Idle.clip_composite_draw(int(self.frame) * 23, 0, 22, 18,
                                           0.0, '', self.x, self.y, self.kx - 1, self.ky - 1)
        else:
            self.Idle.clip_composite_draw(int(self.frame) * 23, 0, 22, 18,
                                           0.0, 'h', self.x, self.y, self.kx - 1, self.ky - 1)
class RUN:
    def enter(self, event):
        if event == RD:
            self.dir_x += 1
        elif event == LD:
            self.dir_x -= 1
        elif event == RU:
            self.dir_x -= 1
        elif event == LU:
            self.dir_x += 1
    def exit(self, event):
        self.face_dir_x = self.dir_x
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.x += self.dir_x * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 800)
    def draw(self):
        if self.dir_x == -1:
            self.Run.clip_composite_draw(int(self.frame) * 22, 0, 22, 20,
                               0.0, '', self.x, self.y, self.kx, self.ky)
        else:
            self.Run.clip_composite_draw(int(self.frame) * 22, 0, 22, 20,
                               0.0, 'h', self.x, self.y, self.kx, self.ky)
class JUMP:
    def enter(self, event):
        if event == JD:
            self.dir_y = 1
            self.timer = 70
            self.s_timer = self.timer // 2
    def exit(self, event):
        pass
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        jump_dis = self.dir_y * RUN_SPEED_PPS * game_framework.frame_time
        self.y += jump_dis
        self.timer -= 1
        if self.timer == self.s_timer:
            self.dir_y *= -1
        elif self.timer == 0:
            self.dir_y *= -1
            self.add_event(TIMER)
    def draw(self):
        if self.face_dir_x == -1:
            self.Jump.clip_composite_draw(int(self.frame) * 25, 0, 25, 22,
                                           0.0, '', self.x, self.y, self.kx, self.ky)
        else:
            self.Jump.clip_composite_draw(int(self.frame) * 25, 0, 25, 22,
                                           0.0, 'h', self.x, self.y, self.kx, self.ky)
class SWAL:
    def enter(self, event):
        if event == AD:
            self.timer = 70
    def exit(self, event):
        pass
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 9
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)

    def draw(self):
        if self.face_dir_x == -1:
            self.Swallow.clip_composite_draw(int(self.frame) * 30, 0, 30, 22,
                                             0.0, '', self.x, self.y, self.kx + 3, self.ky + 3)
        else:
            self.Swallow.clip_composite_draw(int(self.frame) * 30, 0, 30, 22,
                                             0.0, 'h', self.x, self.y, self.kx + 3, self.ky + 3)
class SLEEP:
    def enter(self, event):
        self.frame = 0
    def exit(self, event):
        pass
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    def draw(self):
        if self.face_dir_x == -1:
            self.Sleep.clip_composite_draw(int(self.frame) * 30, 0, 30, 18,
                                           0.0, '', self.x, self.y, self.kx, self.ky)
        else:
            self.Sleep.clip_composite_draw(int(self.frame) * 30, 0, 30, 18,
                                           0.0, 'h', self.x, self.y, self.kx, self.ky)

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN,  JD: JUMP, TIMER: SLEEP, AD: SWAL},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, JD: JUMP, TIMER: IDLE,  AD: SWAL},
    SLEEP: {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN,  JD: IDLE, TIMER: IDLE,  AD: IDLE},
    JUMP:  {RU: JUMP, LU: JUMP, RD: JUMP, LD: JUMP, JD: JUMP, TIMER: IDLE,  AD: JUMP},
    SWAL:  {RU: SWAL, LU: SWAL, RD: SWAL, LD: SWAL, JD: SWAL, TIMER: IDLE,  AD: SWAL}
}
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 2.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
class Kirby:
    def __init__(self):
        self.x, self.y = 30, 100
        self.kx, self.ky = 70, 55
        self.face_dir_x, self.dir_x = 1, 0
        self.dis_y = self.y
        self.dir_y = 1
        self.frame = 7
        self.timer = 0
        self.s_timer = 0

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

        self.Idle = load_image('kirby_idle.png')
        self.Run = load_image('kirby_move.png')
        self.Jump = load_image('kirby_jump.png')
        self.Swallow = load_image('kirby_swallow.png')
        self.Sleep = load_image('kirby_sleep.png')

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

    def add_event(self, event):
        self.event_que.insert(0, event)
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)