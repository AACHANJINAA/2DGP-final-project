from pico2d import*
import game_framework
import game_world

from move_kirby import Kirby

image = None
kirby = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            kirby.handle_event(event)

def enter():
    global kirby
    kirby = Kirby()
    game_world.add_object(kirby, 0)

def exit():
    game_world.clear()
    # global image, kirby
    # del image
    # del kirby

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.01)
    # global kirby
    # delay(0.05)
    # kirby.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()
    # global image, kirby
    # image.draw(800 // 2, 400 // 2)
    # kirby.draw()
    # update_canvas()

def pause():
    pass

def resume():
    pass
def test_self():
    import map_state

    pico2d.open_canvas()
    game_framework.run(map_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
