from pico2d import*
import game_framework
import logo_state

image = None

def enter():
    global image
    image = load_image('map/exit.png')
    clear_canvas()

def exit():
    global image
    del image

def update():
    pass

def draw():
    global image
    image.draw(1200 // 2, 500 // 2)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(logo_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()

