from pico2d import*
import game_framework
import game_world

RD, LD, RU, LU, JD, AD = range(6)
event_name = ['RD', 'LD', 'RU', 'LU', 'JD', 'AD']

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
    def enter(self,event):
        print('ENTER IDLE')
        #self.dir_x = 1

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')
    @staticmethod
    def do(self):
        self.frame = 7

    @staticmethod
    def draw(self):
        if self.face_dir_x == 1:
            self.Run.clip_draw(self.frame * self.kx, self.ky - self.dir_y * self.ky,
                               self.kx, self.ky, self.x, self.y)
        else:
            self.Run.clip_draw(self.frame * self.kx, self.ky - self.dir_y * self.ky,
                               self.kx, self.ky, self.x, self.y)
class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir_x += 1
        elif event == LD:
            self.dir_x -= 1
        elif event == RU:
            self.dir_x -= 1
        elif event == LU:
            self.dir_x += 1

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir_x = self.dir_x
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir_x
        self.x = clamp(0, self.x, 800)

    def draw(self):
        if self.dir_x == 1:
            self.Run.clip_draw(self.frame * self.kx, self.ky - self.dir_y * self.ky,
                               self.kx, self.ky, self.x, self.y)
        else:
            self.Run.clip_draw(self.frame * self.kx, self.ky - self.dir_y * self.ky,
                               self.kx, self.ky, self.x, self.y)

# def handle_events():
#     global running, kirby
#     events = get_events()
#     for event in events:
#         #keydown
#         if kirby.run_appear and not kirby.jump_appear and not kirby.absorb_appear:
#             if event.type == SDL_QUIT:
#                 running = False
#             elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#                 running = False
#             elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
#                 kirby.R_move = True
#             elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
#                 kirby.L_move = True
#             elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
#                 kirby.frame = 0
#                 kirby.run_appear = False
#                 kirby.jump_appear = True
#                 kirby.jump_move = True
#             elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
#                 kirby.frame = 0
#                 kirby.run_appear = False
#                 kirby.absorb_appear = True
#                 kirby.absorb_move = True
#         #keyup
#         if event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
#             kirby.R_move = False
#             kirby.frame = 7
#         elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
#             kirby.L_move = False
#             kirby.frame = 7

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE},
}
class Kirby:
    def __init__(self):
        self.x, self.y = 30, 100
        self.kx, self.ky = 70, 55
        self.face_dir_x, self.dir_x = 1, 0
        self.dir_y = 1
        self.jump_y = 1
        self.frame = 7

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

        self.Run = load_image('kirby_move.png')
        self.Jump = load_image('kirby_jump.png')
        self.absorb = load_image('kirby_absorb.png')

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
        # if self.run_appear:
        #     if self.R_move:
        #         self.dir_x = +1
        #         self.dir_y = 1
        #         self.x += self.dir_x * 10
        #         self.frame = (self.frame - 1) % 7
        #
        #     elif self.L_move:
        #         self.dir_x = -1
        #         self.dir_y = 0
        #         self.x += self.dir_x * 10
        #         self.frame = (self.frame - 1) % 7

        # if self.jump_appear:
        #     if self.jump_move:
        #         self.y += self.jump_y * 25
        #         self.frame = (self.frame + 1) % 8
        #         delay(0.01)
        #         if self.frame > 3:
        #             self.jump_y = -1
        #         else:
        #             self.jump_y = +1
        #         if self.frame == 0:
        #             self.jump_move = False
        #             self.jump_appear = False
        #             self.frame = 7

        # if self.absorb_appear:
        #     if self.absorb_move:
        #         self.frame = (self.frame + 1) % 8
        #         delay(0.05)
        #         if self.frame == 0:
        #             self.absorb_move = False
        #             self.absorb_appear = False
        #             self.frame = 7

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
        # if self.run_appear:
        #     if self.y != 100 and not self.jump_appear:
        #         self.y = 100
        #     self.Run.clip_draw(self.frame * self.kx, self.ky - self.dir_y * self.ky,
        #                        self.kx, self.ky, self.x, self.y)
        # elif self.jump_appear:
        #     self.Jump.clip_draw(self.frame * self.kx, self.ky - self.dir_y * self.ky,
        #                         self.kx, self.ky, self.x, self.y)
        # elif self.absorb_appear:
        #     self.absorb.clip_draw(self.frame * self.kx + 3, self.ky - self.dir_y * self.ky,
        #                           self.kx, self.ky, self.x, self.y)