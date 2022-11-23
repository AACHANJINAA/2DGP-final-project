from pico2d import*
import game_framework

class IDLE1:
    @staticmethod
    def enter(self, event):
        self.x, self.y = 700, 130
        self.frame = 0
        self.dir = -1

    @staticmethod
    def exit(self, event):
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x < 100 or self.x > 700:
            self.dir *= -1

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.Idle.clip_composite_draw(int(self.frame) * 48, 0, 48, 56,
                                          0.0, 'h', self.x, self.y, self.kx, self.ky)
        else:
            self.Idle.clip_composite_draw(int(self.frame) * 48, 0, 48, 56,
                                          0.0, '', self.x, self.y, self.kx, self.ky)
class IDLE2:
    @staticmethod
    def enter(self, event):
        self.frame = 0
        self.dir = -1

    @staticmethod
    def exit(self, event):
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x < 100 or self.x > 700:
            self.dir *= -1

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.Idle.clip_composite_draw(int(self.frame) * 80, 0, 80, 64,
                                          0.0, 'h', self.x, self.y, self.kx, self.ky)
        else:
            self.Idle.clip_composite_draw(int(self.frame) * 80, 0, 80, 64,
                                          0.0, '', self.x, self.y, self.kx, self.ky)
class IDLE3:
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
class IDLE4:
    @staticmethod
    def enter(self, event):
        self.x, self.y = 700, 130
        self.frame = 0
        self.dir = -1

    @staticmethod
    def exit(self, event):
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x < 100 or self.x > 700:
            self.dir *= -1

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.Idle.clip_composite_draw(int(self.frame) * 48, 0, 48, 49,
                                          0.0, 'h', self.x, self.y, self.kx, self.ky)
        else:
            self.Idle.clip_composite_draw(int(self.frame) * 48, 0, 48, 49,
                                          0.0, '', self.x, self.y, self.kx, self.ky)

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 2.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
class SWORD_BOSS:
    def __init__(self):
        self.x, self.y = 700, 100
        self.kx, self.ky = 96, 112
        self.frame = 0
        self.dir = -1

        self.event_que = []
        self.cur_state = IDLE1
        self.cur_state.enter(self, None)

        self.Idle = load_image('boss/sword_boss.png')

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
class SPARK_BOSS:
    def __init__(self):
        self.x, self.y = 700, 100
        self.kx, self.ky = 150, 120
        self.frame = 0
        self.dir = -1

        self.event_que = []
        self.cur_state = IDLE2
        self.cur_state.enter(self, None)

        self.Idle = load_image('boss/spark_boss.png')

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
class BOMBER_BOSS:
    def __init__(self):
        self.x, self.y = 710, 400 // 2
        self.kx, self.ky = 200, 400
        self.frame = 0

        self.event_que = []
        self.cur_state = IDLE3
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
class LAST_BOSS:
    def __init__(self):
        self.x, self.y = 700, 130
        self.kx, self.ky = 96, 112
        self.frame = 0
        self.dir = -1

        self.event_que = []
        self.cur_state = IDLE4
        self.cur_state.enter(self, None)

        self.Idle = load_image('boss/last_boss.png')

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


