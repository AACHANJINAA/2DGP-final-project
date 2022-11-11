from pico2d import*
import game_framework

class SWORD_BACK:
    def __init__(self, x=0):
        self.image = load_image('basic_stage/sword_basic_stage.png')
        self.x = x

    def draw(self):
        self.image.clip_composite_draw(0, 0, 400, 200, 0, '',
                                       800 // 2, 600 // 2, 800, 600)

    def update(self):
        pass

class SPARK_BACK:
    def __init__(self, x=0):
        self.image = load_image('basic_stage/spark_basic_stage.png')
        self.x = x

    def draw(self):
        self.image.clip_composite_draw(0, 0, 640, 360, 0, '',
                                       800 // 2, 600 // 2, 800, 600)

    def update(self):
        pass

class BOMBER_BACK:
    def __init__(self, x=0):
        self.image = load_image('basic_stage/bomber_basic_stage.png')
        self.x = x

    def draw(self):
        self.image.clip_composite_draw(0, 0, 400, 200, 0, '',
                                       800 // 2, 600 // 2, 800, 600)

    def update(self):
        pass