from pico2d import*
import game_framework

image = None

def enter():
    global image
    image = load_image('map.png')
    clear_canvas()

def exit():
    global image
    del image

def update():
    # 포탈 위치 들어갔을 때
    pass

def draw():
    global image
    image.draw(800 // 2, 400 // 2)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            close_canvas()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
            close_canvas()
