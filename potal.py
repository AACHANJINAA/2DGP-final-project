from pico2d import*
import server


class POTAL:
    def __init__(self, pn):
        self.frame = 0
        self.potal = [load_image('map/potal_blue.png'),
                      load_image('map/potal_blue.png'),
                      load_image('map/potal_blue.png'),
                      load_image('map/potal_purple.png')]

        self.potal_num = pn


    def draw(self):
        for i in range(0, self.potal_num):
            self.potal[i].clip_composite_draw(int(self.frame) * 134, 0, 134, 129,
                                              0.0, 'h', 250 * (i + 1), 120, 100, 90)

    def update(self):
        self.frame = (self.frame + 0.2) % 3

    def handle_event(self, event):
        pass


