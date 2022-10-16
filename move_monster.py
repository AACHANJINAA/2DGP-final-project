from pico2d import *

class Monster:
    def __init__(self):
        self.x, self.y = 400, 100
        self.kx, self.ky = 70, 55
        self.dir_x = 1
        self.dir_y = 1
        self.frame = 0
        self.cnt = 0

        self.Run = load_image('basic_monster.png')

        self.run_appear = True

    def update(self):
        if self.run_appear:
            self.x += self.dir_x * 5
            self.frame = (self.frame + 1) % 4
            self.cnt = (self.cnt + 1) % 64
            delay(0.1)
            if self.cnt == 0:
                if self.dir_x == 1 and self.dir_y == 1:
                    self.dir_x = -1
                    self.dir_y = 0
                elif self.dir_x == -1 and self.dir_y == 0:
                    self.dir_x = 1
                    self.dir_y = 1

    def draw(self):
        if self.run_appear:
            self.Run.clip_draw(self.frame * self.kx, self.ky - self.dir_y * self.ky,
                               self.kx, self.ky, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            close_canvas()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            close_canvas()

open_canvas(800, 400)

monster = Monster()
running = True

while running:
    clear_canvas()
    handle_events()

    monster.update()

    monster.draw()

    update_canvas()

    delay(0.05)

close_canvas()