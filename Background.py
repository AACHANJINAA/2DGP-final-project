from pico2d import*
import game_framework
import server


class SWORD_BACK:
    def __init__(self):
        self.image = load_image('basic_stage/sword_basic_stage.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom,
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

class SPARK_BACK:
    def __init__(self):
        self.image = load_image('basic_stage/spark_basic_stage.png')

    def draw(self):
        self.image.clip_composite_draw(0, 0, 640, 360, 0, '',
                                       w, h, 800, 400)

    def update(self):
        pass
class BOMBER_BACK:
    def __init__(self):
        self.image = load_image('basic_stage/bomber_basic_stage.png')

    def draw(self):
        self.image.clip_composite_draw(0, 0, 400, 200, 0, '',
                                       w, h, 800, 400)

    def update(self):
        pass
class SWORD_BOSS_BACK:
    def __init__(self):
        self.image = load_image('boss_stage/sword_boss_stage.png')

    def draw(self):
        self.image.clip_composite_draw(0, 0, 736 // 2, 414, 0, '',
                                       w, h, 800, 400)

    def update(self):
        pass
class SPARK_BOSS_BACK:
    def __init__(self):
        self.image = load_image('boss_stage/spark_boss_stage.png')

    def draw(self):
        self.image.clip_composite_draw(0, 0, 1000 // 2, 700, 0, '',
                                       w, h, 800, 400)

    def update(self):
        pass
class BOMBER_BOSS_BACK:
    def __init__(self):
        self.image = load_image('boss_stage/bomber_boss_stage.png')

    def draw(self):
        self.image.clip_composite_draw(0, 0, 1920 // 2, 696, 0, '',
                                       w, h, 800, 400)

    def update(self):
        pass
class LAST_BOSS_BACK:
    def __init__(self):
        self.image = load_image('boss_stage/last_boss_stage.png')

    def draw(self):
        self.image.clip_composite_draw(0, 0, 600 // 2, 424, 0, '',
                                       w, h, 800, 400)

    def update(self):
        pass

