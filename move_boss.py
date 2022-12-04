from pico2d import*
import game_framework
import game_world
import server



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
        self.x, self.y = 700, 130
        self.sx, self.sy = 700, 130
        self.kx, self.ky = 96, 112
        self.frame = 0
        self.dir = -1
        self.hp_cnt = 16.0

        self.event_que = []
        self.cur_state = IDLE1
        self.cur_state.enter(self, None)

        self.Idle = load_image('boss/sword_boss.png')
        self.Hp = [load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png')]

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)

            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        for i in range(0, int(self.hp_cnt)):
            self.Hp[i].clip_composite_draw(0, 0, 457, 62,
                                           0.0, '', self.x - 70 + i * 10, self.y + 80, 20, 20)
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.sx - 50, self.sy - 50, self.sx + 50, self.sy + 50

    def handle_collision(self, other, group):
        match group:
            case 'kirby:sword_boss':
                pass
            case'kirby_skill:sword_boss':
                self.hp_cnt -= 0.02
                if server.skill is True and self.hp_cnt < 0:
                    game_world.remove_object(self)
class IDLE1:
    @staticmethod
    def enter(self, event):
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
        self.sx = self.x - server.background.window_left
        self.sy = self.y - server.background.window_bottom
        if self.dir == -1:
            self.Idle.clip_composite_draw(int(self.frame) * 48, 0, 48, 56,
                                          0.0, 'h', self.sx, self.sy, self.kx, self.ky)
        else:
            self.Idle.clip_composite_draw(int(self.frame) * 48, 0, 48, 56,
                                          0.0, '', self.sx, self.sy, self.kx, self.ky)
class SPARK_BOSS:
    def __init__(self):
        self.x, self.y = 700, 100
        self.sx, self.sy = 700, 100
        self.kx, self.ky = 150, 120
        self.frame = 0
        self.dir = -1
        self.hp_cnt = 16.0

        self.event_que = []
        self.cur_state = IDLE2
        self.cur_state.enter(self, None)

        self.Idle = load_image('boss/spark_boss.png')
        self.Hp = [load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png')]

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)

            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        for i in range(0, int(self.hp_cnt)):
            self.Hp[i].clip_composite_draw(0, 0, 457, 62,
                                           0.0, '', self.sx - 70 + i * 10, self.sy + 80, 20, 20)
        draw_rectangle(*self.get_bb())
    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.sx - 50, self.sy - 50, self.sx + 50, self.sy + 50
    def handle_collision(self, other, group):
        match group:
            case 'kirby:spark_boss':
                pass
            case 'kirby_skill:spark_boss':
                self.hp_cnt -= 0.02
                if server.skill is True and self.hp_cnt < 0:
                    game_world.remove_object(self)

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
        self.sx = self.x - server.background.window_left
        self.sy = self.y - server.background.window_bottom
        if self.dir == -1:
            self.Idle.clip_composite_draw(int(self.frame) * 80, 0, 80, 64,
                                          0.0, 'h', self.sx, self.sy, self.kx, self.ky)
        else:
            self.Idle.clip_composite_draw(int(self.frame) * 80, 0, 80, 64,
                                          0.0, '', self.sx, self.sy, self.kx, self.ky)

class BOMBER_BOSS:
    def __init__(self):
        self.x, self.y = 1200 - 100, 500 // 2
        self.sx, self.sy = 1200 - 100, 500 // 2
        self.kx, self.ky = 200, 500
        self.frame = 0
        self.hp_cnt = 16.0

        self.event_que = []
        self.cur_state = IDLE3
        self.cur_state.enter(self, None)

        self.Idle = load_image('boss/bomber_boss.png')
        self.Hp = [load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png')]

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)

            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        for i in range(0, int(self.hp_cnt)):
            self.Hp[i].clip_composite_draw(0, 0, 600, 400,
                                           0.0, '', self.sx - 70 + i * 10, self.sy + 220, 20, 20)
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.sx - 60, self.sy - 200, self.sx + 60, self.sy + 200
    def handle_collision(self, other, group):
        match group:
            case 'kirby:bomber_boss':
                pass
            case 'kirby_skill:bomber_boss':
                self.hp_cnt -= 0.02
                if server.skill is True and self.hp_cnt < 0:
                    game_world.remove_object(self)

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
        self.sx = self.x - server.background.window_left
        self.sy = self.y - server.background.window_bottom
        self.Idle.clip_composite_draw(int(self.frame) * 86, 0, 86, 136,
                                        0.0, '', self.sx, self.sy, self.kx, self.ky)

class LAST_BOSS:
    def __init__(self):
        self.x, self.y = 1100, 130
        self.sx, self.sy = 1100, 130
        self.kx, self.ky = 100, 116.8
        self.frame = 0
        self.dir = -1
        self.hp_cnt = 16.0

        self.event_que = []
        self.cur_state = IDLE4
        self.cur_state.enter(self, None)

        self.Idle = load_image('boss/last_boss.png')
        self.Hp = [load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png'),
                   load_image('UI/hp.png'), load_image('UI/hp.png')]

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)

            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        for i in range(0, int(self.hp_cnt)):
            self.Hp[i].clip_composite_draw(0, 0, 457, 62,
                                           0.0, '', self.sx - 70 + i * 10, self.sy + 80, 20, 20)
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.sx - 50, self.sy - 50, self.sx + 50, self.sy + 50
    def handle_collision(self, other, group):
        match group:
            case 'kirby:last_boss':
                pass
            case 'kirby_skill:last_boss':
                self.hp_cnt -= 0.005
                if server.skill is True and self.hp_cnt < 0:
                    game_world.remove_object(self)

class IDLE4:
    @staticmethod
    def enter(self, event):
        self.frame = 0
        self.dir = -1

    @staticmethod
    def exit(self, event):
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time * 2
        if self.x < 50 or self.x > 1150:
            self.dir *= -1

    @staticmethod
    def draw(self):
        self.sx = self.x - server.background.window_left
        self.sy = self.y - server.background.window_bottom
        if self.dir == -1:
            self.Idle.clip_composite_draw(int(self.frame) * 48, 0, 48, 49,
                                          0.0, 'h', self.sx, self.sy, self.kx, self.ky)
        else:
            self.Idle.clip_composite_draw(int(self.frame) * 48, 0, 48, 49,
                                          0.0, '', self.sx, self.sy, self.kx, self.ky)


