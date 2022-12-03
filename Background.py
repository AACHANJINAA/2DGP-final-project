from pico2d import*
import game_framework
import server


class BACK:
    def __init__(self, n):
        self.stage_num = n
        self.image = [load_image('basic_stage/sword_basic_stage.png'),
                      load_image('basic_stage/spark_basic_stage.png'),
                      load_image('basic_stage/bomber_basic_stage.png'),
                      load_image('boss_stage/sword_boss_stage.png'),
                      load_image('boss_stage/spark_boss_stage.png'),
                      load_image('boss_stage/bomber_boss_stage.png'),
                      load_image('boss_stage/last_boss_stage.png')]
        if self.stage_num <= 2:
            self.canvas_width = get_canvas_width()
        else:
            self.canvas_width = 1200
        self.canvas_height = get_canvas_height()
        self.w = self.image[self.stage_num].w
        self.h = self.image[self.stage_num].h

    def draw(self):
        self.image[self.stage_num].clip_draw_to_origin(self.window_left, self.window_bottom,
                                                       self.canvas_width, self.canvas_height,
                                                       0, 0)

    def update(self):
        self.window_left = clamp(0,
                                 int(server.kirby.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width - 1)
        self.window_bottom = clamp(0,
                                   int(server.kirby.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height - 1)

    def handle_event(self, event):
        pass


