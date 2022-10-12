from pico2d import*
import game_framework
import map_state

image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('logo.png')
    clear_canvas()

def exit():
    global image
    del image

def update():
    global logo_time
    delay(0.05)
    logo_time += 0.05
    if logo_time > 1.0:
        game_framework.change_state(map_state)
    pass

def draw():
    global image
    image.draw(800 // 2, 400 // 2)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(map_state)

