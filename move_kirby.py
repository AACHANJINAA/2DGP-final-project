from pico2d import*

class Kirby:
    def __init__(self):
        self.x, self.y = 30, 100
        self.kx, self.ky = 70, 55
        self.dir_x = 1
        self.dir_y = 1
        self.jump_y = 1
        self.frame = 7

        self.Run = load_image('kirby_move.png')
        self.Jump = load_image('kirby_jump.png')
        self.absorb = load_image('kirby_absorb.png')

        self.run_appear = True
        self.jump_appear = False
        self.absorb_appear = False

        self.L_move = False
        self.R_move = False
        self.jump_move = False
        self.absorb_move = False

    def update(self):
        if self.run_appear:
            if self.R_move:
                self.dir_x = +1
                self.dir_y = 1
                self.x += self.dir_x * 10
                self.frame = (self.frame - 1) % 7

            elif self.L_move:
                self.dir_x = -1
                self.dir_y = 0
                self.x += self.dir_x * 10
                self.frame = (self.frame - 1) % 7
        if self.jump_appear:
            if self.jump_move:
                self.y += self.jump_y * 25
                self.frame = (self.frame + 1) % 8
                delay(0.01)
                if self.frame > 3:
                    self.jump_y = -1
                else:
                    self.jump_y = +1
                if self.frame == 0:
                    self.jump_move = False
                    self.jump_appear = False
                    self.run_appear = True
                    self.frame = 7
        if self.absorb_appear:
            if self.absorb_move:
                self.frame = (self.frame + 1) % 8
                delay(0.05)
                if self.frame == 0:
                    self.absorb_move = False
                    self.absorb_appear = False
                    self.run_appear = True
                    self.frame = 7

    def draw(self):
        if self.run_appear:
            if self.y != 100 and not self.jump_appear:
                self.y = 100
            self.Run.clip_draw(self.frame * self.kx, self.ky - self.dir_y * self.ky,
                               self.kx, self.ky, self.x, self.y)
        elif self.jump_appear:
            self.Jump.clip_draw(self.frame * self.kx, self.ky - self.dir_y * self.ky,
                                self.kx, self.ky, self.x, self.y)
        elif self.absorb_appear:
            self.absorb.clip_draw(self.frame * self.kx + 3, self.ky - self.dir_y * self.ky,
                                  self.kx, self.ky, self.x, self.y)

def handle_events():
    global running, kirby
    events = get_events()
    for event in events:
        #keydown
        if kirby.run_appear and not kirby.jump_appear and not kirby.absorb_appear:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
                kirby.R_move = True
            elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
                kirby.L_move = True
            elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
                kirby.frame = 0
                kirby.run_appear = False
                kirby.jump_appear = True
                kirby.jump_move = True
            elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
                kirby.frame = 0
                kirby.run_appear = False
                kirby.absorb_appear = True
                kirby.absorb_move = True
        #keyup
        if event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            kirby.R_move = False
            kirby.frame = 7
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            kirby.L_move = False
            kirby.frame = 7

open_canvas(800, 400)

kirby = Kirby()
running = True

while running:
    clear_canvas()
    handle_events()

    kirby.update()

    kirby.draw()

    update_canvas()

    delay(0.05)

close_canvas()