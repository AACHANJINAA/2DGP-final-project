from pico2d import*
import game_framework
import game_world
import server
#from Background import FixedBackground as Background

from move_kirby import Kirby, SKILL
from Background import BACK
from move_monster import BASIC_MONSTER, SWORD_MONSTER, SPARK_MONSTER, BOMBER_MONSTER

server.kirby = None
server.background = None
server.monster = [None, None, None, None]

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            server.kirby.handle_event(event)
def enter():

    server.kirby = Kirby()
    server.monster = [BASIC_MONSTER(), SWORD_MONSTER(), SPARK_MONSTER(), BOMBER_MONSTER()]
    server.background = BACK(0)

    game_world.add_object(server.background, 0)
    #game_world.add_object(server.monster[0], 1)
    #game_world.add_object(server.monster[1], 1)
    game_world.add_object(server.monster[2], 1)
    #game_world.add_object(server.monster[3], 1)
    game_world.add_object(server.kirby, 1)

    #game_world.add_collision_group(server.kirby, server.monster[0], 'kirby:basic_monster')
    #game_world.add_collision_group(server.kirby, server.monster[1], 'kirby:sword_monster')
    game_world.add_collision_group(server.kirby, server.monster[2], 'kirby:spark_monster')
    #game_world.add_collision_group(server.kirby, server.monster[3], 'kirby:bomber_monster')

    #game_world.add_collision_group(server.kirby, server.monster[0], 'kirby_skill:basic_monster')
    #game_world.add_collision_group(server.kirby, server.monster[1], 'kirby_skill:sword_monster')
    game_world.add_collision_group(server.kirby, server.monster[2], 'kirby_skill:spark_monster')
    #game_world.add_collision_group(server.kirby, server.monster[3], 'kirby_skill:bomber_monster')

def exit():
    game_world.clear()
def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('collision by group', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()
def draw():
    clear_canvas()
    draw_world()
    update_canvas()
def pause():
    pass
def resume():
    pass
def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
