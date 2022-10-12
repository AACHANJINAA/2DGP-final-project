from pico2d import*

class Kirby:
    def __init__(self):
        self.x, self.y = 0, 100
        self.dir = 1
        self.frame = 0
        self.image = load_image('kirby_walk.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 10

    def draw(self):
        self.image.clip_draw(self.frame * 60, 50 - self.dir * 50, 60, 48, self.x, self.y)

def handle_events():
    global running, kirby
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

kirby = Kirby()
running = True

open_canvas(800, 400)

while running:
    handle_events()

    kirby.update()

    clear_canvas()
    kirby.draw()

    update_canvas()

    delay(0.05)

close_canvas()