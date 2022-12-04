import random

from pico2d import*
import game_framework
import game_world
import server

from move_kirby import Kirby
from Background import BACK
from move_monster import BASIC_MONSTER, SWORD_MONSTER, SPARK_MONSTER, BOMBER_MONSTER
from move_boss import SWORD_BOSS, SPARK_BOSS, BOMBER_BOSS,LAST_BOSS

server.kirby = None
server.background = [None, None, None, None,
                     None, None, None,
                     None, None, None, None]
server.monster = [None, None, None, None]
stage = []
server.stage_number = 6

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
    server.boss = [SWORD_BOSS(), SPARK_BOSS(), BOMBER_BOSS(), LAST_BOSS()]
    b = [BACK(0, 4), BACK(0, 3), BACK(0, 2), BACK(0, 1),
         BACK(1, 4), BACK(2, 4), BACK(3, 4),
         BACK(4, 4), BACK(5, 4), BACK(6, 4), BACK(7, 4)]
    # map 0 1 2 3
    # basic_stage 4 5 6
    # boss_stage 7 8 9 10

    match server.stage_number:
        case 0: #map(potal_num is 4)
            server.background = b[0]
            game_world.add_object(server.background, 0)
            game_world.add_object(server.kirby, 1)
        case 1: #basic_stage_1
            server.background = b[4]
            game_world.add_object(server.background, 0)
            game_world.add_object(server.kirby, 1)
            game_world.add_object(server.monster[0], 1)
            game_world.add_collision_group(server.kirby, server.monster[0], 'kirby:basic_monster')
            game_world.add_collision_group(server.kirby, server.monster[0], 'kirby_skill:basic_monster')
            game_world.add_object(server.monster[1], 1)
            game_world.add_collision_group(server.kirby, server.monster[1], 'kirby:sword_monster')
            game_world.add_collision_group(server.kirby, server.monster[1], 'kirby_skill:sword_monster')
        case 2:  #boss_stage_1
            server.background = b[7]
            game_world.add_object(server.background, 0)
            server.mode = 1
            game_world.add_object(server.kirby, 1)
            game_world.add_object(server.boss[0], 1)
            game_world.add_collision_group(server.kirby, server.boss[0], 'kirby:sword_boss')
            game_world.add_collision_group(server.kirby, server.boss[0], 'kirby_skill:sword_boss')
        case 3:  # basic_stage_2
            server.background = b[5]
            game_world.add_object(server.background, 0)
            game_world.add_object(server.kirby, 1)
            game_world.add_object(server.monster[0], 1)
            game_world.add_collision_group(server.kirby, server.monster[0], 'kirby:basic_monster')
            game_world.add_collision_group(server.kirby, server.monster[0], 'kirby_skill:basic_monster')
            game_world.add_object(server.monster[2], 1)
            game_world.add_collision_group(server.kirby, server.monster[2], 'kirby:spark_monster')
            game_world.add_collision_group(server.kirby, server.monster[2], 'kirby_skill:spark_monster')
        case 4:  # boss_stage_2
            server.background = b[8]
            game_world.add_object(server.background, 0)
            server.mode = 2
            game_world.add_object(server.kirby, 1)
            game_world.add_object(server.boss[1], 1)
            game_world.add_collision_group(server.kirby, server.boss[1], 'kirby:spark_boss')
            game_world.add_collision_group(server.kirby, server.boss[1], 'kirby_skill:spark_boss')
        case 5:  # basic_stage_3
            server.background = b[6]
            game_world.add_object(server.background, 0)
            game_world.add_object(server.kirby, 1)
            game_world.add_object(server.monster[0], 1)
            game_world.add_collision_group(server.kirby, server.monster[0], 'kirby:basic_monster')
            game_world.add_collision_group(server.kirby, server.monster[0], 'kirby_skill:basic_monster')
            game_world.add_object(server.monster[3], 1)
            game_world.add_collision_group(server.kirby, server.monster[3], 'kirby:bomber_monster')
            game_world.add_collision_group(server.kirby, server.monster[3], 'kirby_skill:bomber_monster')
        case 6:  # boss_stage_3
            server.background = b[9]
            game_world.add_object(server.background, 0)
            server.mode = 3
            game_world.add_object(server.kirby, 1)
            game_world.add_object(server.boss[2], 1)
            game_world.add_collision_group(server.kirby, server.boss[2], 'kirby:bomber_boss')
            game_world.add_collision_group(server.kirby, server.boss[2], 'kirby_skill:bomber_boss')
        case 7:  # boss_stage_final
            server.background = b[10]
            game_world.add_object(server.background, 0)
            server.mode = 1
            game_world.add_object(server.kirby, 1)
            game_world.add_object(server.boss[3], 1)
            game_world.add_collision_group(server.kirby, server.boss[3], 'kirby:last_boss')
            game_world.add_collision_group(server.kirby, server.boss[3], 'kirby_skill:last_boss')



    #game_world.add_object(server.background, 0)
    #game_world.add_object(server.monster[0], 1)
    #game_world.add_object(server.monster[1], 1)
    #game_world.add_object(server.monster[2], 1)
    #game_world.add_object(server.monster[3], 1)
    #game_world.add_object(server.kirby, 1)

    #game_world.add_object(server.boss[0], 1)
    #game_world.add_object(server.boss[1], 1)
    #game_world.add_object(server.boss[2], 1)
    #game_world.add_object(server.boss[3], 1)

    #game_world.add_collision_group(server.kirby, server.monster[0], 'kirby:basic_monster')
    #game_world.add_collision_group(server.kirby, server.monster[0], 'kirby_skill:basic_monster')
    #game_world.add_collision_group(server.kirby, server.monster[1], 'kirby:sword_monster')
    #game_world.add_collision_group(server.kirby, server.monster[1], 'kirby_skill:sword_monster')
    #game_world.add_collision_group(server.kirby, server.monster[2], 'kirby:spark_monster')
    #game_world.add_collision_group(server.kirby, server.monster[2], 'kirby_skill:spark_monster')
    #game_world.add_collision_group(server.kirby, server.monster[3], 'kirby:bomber_monster')
    # game_world.add_collision_group(server.kirby, server.monster[3], 'kirby_skill:bomber_monster')

    # game_world.add_collision_group(server.kirby, server.boss[0], 'kirby:sword_boss')
    # game_world.add_collision_group(server.kirby, server.boss[0], 'kirby_skill:sword_boss')
    # game_world.add_collision_group(server.kirby, server.boss[1], 'kirby:spark_boss')
    # game_world.add_collision_group(server.kirby, server.boss[1], 'kirby_skill:spark_boss')
    # game_world.add_collision_group(server.kirby, server.boss[2], 'kirby:bomber_boss')
    # game_world.add_collision_group(server.kirby, server.boss[2], 'kirby_skill:bomber_boss')
    # game_world.add_collision_group(server.kirby, server.boss[3], 'kirby:last_boss')
    # game_world.add_collision_group(server.kirby, server.boss[3], 'kirby_skill:last_boss')


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
