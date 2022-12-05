from pico2d import*
import server


class BACK:
    def __init__(self, n, pn):
        # self.bgm = load_music('bgm/kirby_basic_music.mp3')
        # self.bgm.set_volume(32)
        # self.bgm.repeat_play()
        self.stage_num = n
        self.image = [load_image('map/map_stage.png'),
                      load_image('basic_stage/sword_basic_stage.png'),
                      load_image('basic_stage/spark_basic_stage.png'),
                      load_image('basic_stage/bomber_basic_stage.png'),
                      load_image('boss_stage/sword_boss_stage.png'),
                      load_image('boss_stage/spark_boss_stage.png'),
                      load_image('boss_stage/bomber_boss_stage.png'),
                      load_image('boss_stage/last_boss_stage.png')]
        self.potal = [load_image('map/potal_blue.png'),
                      load_image('map/potal_blue.png'),
                      load_image('map/potal_blue.png'),
                      load_image('map/potal_purple.png')]

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
        self.potal_num = pn




    def draw(self):
        self.image[self.stage_num].clip_draw_to_origin(self.window_left, self.window_bottom,
                                                       self.canvas_width, self.canvas_height,
                                                       0, 0)
        if self.stage_num == 0:
            for i in range(0, self.potal_num):
                self.potal[i].clip_composite_draw(int(self.frame) * 134, 0, 134, 129,
                                                  0.0, 'h', 250 * (i + 1), 120, 100, 90)

    def update(self):
        self.frame = (self.frame + 0.2) % 3
        self.window_left = clamp(0,
                                 int(server.kirby.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width - 1)
        self.window_bottom = clamp(0,
                                   int(server.kirby.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height - 1)

    def handle_event(self, event):
        pass


