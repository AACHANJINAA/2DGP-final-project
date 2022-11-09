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
# def handle_events():
#     global kirby
#     events = get_events()
#     for event in events:
#         #keydown
#         if kirby.run_appear and not kirby.jump_appear and not kirby.absorb_appear:
#             if event.type == SDL_QUIT:
#                 game_framework.quit()
#             elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#                 game_framework.quit()
#             elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
#                 kirby.R_move = True
#             elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
#                 kirby.L_move = True
#             elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
#                 kirby.frame = 0
#                 kirby.run_appear = False
#                 kirby.jump_appear = True
#                 kirby.jump_move = True
#             elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
#                 kirby.frame = 0
#                 kirby.run_appear = False
#                 kirby.absorb_appear = True
#                 kirby.absorb_move = True
#         #keyup
#         if event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
#             kirby.R_move = False
#             kirby.frame = 7
#         elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
#             kirby.L_move = False
#             kirby.frame = 7
