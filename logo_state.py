from pico2d import*
import game_framework
import play_state

image = None
stop = False
logo_time = 0.0

def enter():

    global image
    image = load_image('map/logo.png')
    clear_canvas()

def exit():
    global image
    del image

def update():
    global logo_time, stop
    delay(0.05)
    if not stop:
        logo_time += 0.05
    if logo_time > 3.0:
        game_framework.change_state(play_state)

def draw():
    global image
    image.draw(1200 // 2, 500 // 2)
    update_canvas()

def handle_events():
    global stop
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(play_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()

