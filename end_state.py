from pico2d import*
import game_framework
import play_state
import server

image = None
bgm = None

def enter():
    global image, bgm
    bgm = load_music('bgm/kill_last_boss.mp3')
    bgm.set_volume(32)
    bgm.repeat_play()
    image = load_image('map/end.png')
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
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()

