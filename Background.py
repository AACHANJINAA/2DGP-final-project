from pico2d import*
import server
import game_framework
import end_state


class BACK:
    def __init__(self, n):
        self.stage_num = n
        if server.other_boss_die:
            self.bgm = load_music('bgm/kill_other_boss.mp3')
            self.bgm.set_volume(120)
            self.bgm.repeat_play()
        elif server.last_boss_die:
            self.bgm = load_music('bgm/kill_last_boss.mp3')
            self.bgm.set_volume(120)
            self.bgm.repeat_play()
        elif self.stage_num == 0:
            self.bgm = load_music('bgm/kirby_map_music.mp3')
            self.bgm.set_volume(120)
            self.bgm.repeat_play()
        elif self.stage_num == 1 or self.stage_num == 3 or self.stage_num == 5:
            self.bgm = load_music('bgm/kirby_basic_music.mp3')
            self.bgm.set_volume(120)
            self.bgm.repeat_play()
        elif self.stage_num == 2 or self.stage_num == 4 or self.stage_num == 6:
            self.bgm = load_music('bgm/kirby_boss_music.mp3')
            self.bgm.set_volume(120)
            self.bgm.repeat_play()
        elif self.stage_num == 7:
            self.bgm = load_music('bgm/last_boss_battle_music.mp3')
            self.bgm.set_volume(120)
            self.bgm.repeat_play()
        self.image = [load_image('map/map_stage.png'),
                      load_image('basic_stage/sword_basic_stage.png'),
                      load_image('basic_stage/spark_basic_stage.png'),
                      load_image('basic_stage/bomber_basic_stage.png'),
                      load_image('boss_stage/sword_boss_stage.png'),
                      load_image('boss_stage/spark_boss_stage.png'),
                      load_image('boss_stage/bomber_boss_stage.png'),
                      load_image('boss_stage/last_boss_stage.png')]

        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image[self.stage_num].w
        self.h = self.image[self.stage_num].h
        self.window_left = clamp(0,
                                 int(server.kirby.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width - 1)
        self.window_bottom = clamp(0,
                                   int(server.kirby.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height - 1)
        self.frame = 0.0



    def draw(self):
        self.image[self.stage_num].clip_draw_to_origin(self.window_left, self.window_bottom,
                                                       self.canvas_width, self.canvas_height,
                                                       0, 0)

    def update(self):
        if server.last_boss_die:
            game_framework.change_state(end_state)
        if server.other_boss_die:
            server.stage_number += 1
            server.potal_number += 1
            self.__init__(self.stage_num)
            server.other_boss_die = False
            server.stage_replay = True


        if server.last_boss_die:
            self.__init__(self.stage_num)
            server.last_boss_die = False

        self.frame = (self.frame + 0.2) % 3
        self.window_left = clamp(0,
                                 int(server.kirby.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width - 1)
        self.window_bottom = clamp(0,
                                   int(server.kirby.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height - 1)

    def handle_event(self, event):
        pass

class POTAL:
    def __init__(self, n, pn):
        self.stage_num = n
        self.potal = [load_image('map/potal_blue.png'),
                      load_image('map/potal_purple.png')]
        self.frame = 0.0
        self.sx, self.sy = 2300, 120
        self.potal_num = pn
        self.potal_sound = load_wav('bgm/kirby_basic/kirby_enter_potal.wav')
        self.potal_sound.set_volume(32)

    def draw(self):
        if self.stage_num == 0 and self.potal_num < 3:
            self.potal[0].clip_composite_draw(int(self.frame) * 134, 0, 134, 129,
                                             0.0, 'h', 250 * (self.potal_num + 1), 320, 100, 100)
        elif self.stage_num == 0 and self.potal_num == 3:
            self.potal[1].clip_composite_draw(int(self.frame) * 134, 0, 134, 129,
                                             0.0, 'h', 250 * (self.potal_num + 1), 320, 100, 100)
        elif self.stage_num == 1 or self.stage_num == 3 or self.stage_num == 5:
            self.sx = 2200 - server.background.window_left
            self.sy = 120 - server.background.window_bottom
            self.potal[0].clip_composite_draw(int(self.frame) * 134, 0, 134, 129,
                                             0.0, 'h', self.sx, self.sy, 100, 100)
        elif self.stage_num == 2 or self.stage_num == 4 or self.stage_num == 6:
            self.sx, self.sy = 2700, 2000
            self.potal[0].clip_composite_draw(int(self.frame) * 134, 0, 134, 129,
                                              0.0, 'h', self.sx, self.sy, 100, 100)
        #draw_rectangle(*self.get_bb())
        pass
    def update(self):
        self.frame = (self.frame + 0.2) % 3


    def get_bb(self):
        if self.stage_num == 0:
            return 250 * (self.potal_num + 1) - 50, 320 - 50, \
                   250 * (self.potal_num + 1) + 50, 320 + 50,
        else:
            return self.sx - 50, self.sy - 50, \
                   self.sx + 50, self.sy + 50

    def handle_collision(self, other, group):
        if group == 'kirby:enter_potal':
            self.potal_sound.play()
            match self.stage_num:
                case 0:
                    match self.potal_num:
                        case 0:
                            server.stage_number = 1
                            server.stage_replay = True
                        case 1:
                            server.stage_number = 4
                            server.stage_replay = True
                        case 2:
                            server.stage_number = 7
                            server.stage_replay = True
                        case 3:
                            server.stage_number = 10
                            server.stage_replay = True
                case 1:
                    server.stage_number = 2
                    server.stage_replay = True
                case 3:
                    server.stage_number = 5
                    server.stage_replay = True
                case 5:
                    server.stage_number = 8
                    server.stage_replay = True



    def handle_event(self, event):
        pass


