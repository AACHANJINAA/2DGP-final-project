from pico2d import*
import game_framework
import play_state

image = None
bgm = None



def enter():
    global image, bgm
    bgm = load_music('bgm/kirby_logo_music.mp3')
    bgm.set_volume(32)
    bgm.repeat_play()
    image = load_image('map/logo.png')
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
    global stop
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(play_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()

