from pico2d import*
import game_framework

class IDLE:
    @staticmethod
    def enter(self, event):
        self.frame = 0

    @staticmethod
    def exit(self, event):
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

    @staticmethod
    def draw(self):
        self.Idle.clip_composite_draw(int(self.frame) * 86, 0, 86, 136,
                                        0.0, '', self.x, self.y, self.kx, self.ky)

TIME_PER_ACTION = 2.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class BOSS1:
    def __init__(self):
        self.x, self.y = 710, 400 // 2
        self.kx, self.ky = 200, 400
        self.frame = 0

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

        self.Idle = load_image('boss/bomber_boss.png')

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)

            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        pass

