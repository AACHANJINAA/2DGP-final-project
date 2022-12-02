from pico2d import*
import game_framework
import game_world

from move_kirby import Kirby, SKILL
from Background import SWORD_BACK, SPARK_BACK, BOMBER_BACK
from Background import SWORD_BOSS_BACK, SPARK_BOSS_BACK, BOMBER_BOSS_BACK, LAST_BOSS_BACK
from move_boss import SWORD_BOSS, SPARK_BOSS, BOMBER_BOSS, LAST_BOSS
from move_monster import BASIC_MONSTER, SWORD_MONSTER, SPARK_MONSTER, BOMBER_MONSTER

kirby = None
stage1, stage2, stage3 = None, None, None
stage4, stage5, stage6, stage7 = None, None, None, None
monster = [None, None, None, None]
boss1, boss2, boss3, boss4 = None, None, None, None

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
            kirby.handle_event(event)
def enter():
    global kirby
    global stage1, stage2, stage3
    global stage4, stage5, stage6, stage7
    global boss1, boss2, boss3, boss4
    global monster

    kirby = Kirby()

    stage1 = SWORD_BACK(0)
    stage2 = SPARK_BACK(0)
    stage3 = BOMBER_BACK(0)

    stage4 = SWORD_BOSS_BACK(0)
    stage5 = SPARK_BOSS_BACK(0)
    stage6 = BOMBER_BOSS_BACK(0)
    stage7 = LAST_BOSS_BACK(0)

    for i in range(0, 4):
        monster = [BASIC_MONSTER(), SWORD_MONSTER(), SPARK_MONSTER(), BOMBER_MONSTER()]
    # 소드 스파크 봄버 디디디마왕순
    boss1, boss2, boss3, boss4 = SWORD_BOSS(), SPARK_BOSS(), BOMBER_BOSS(), LAST_BOSS()

    game_world.add_object(stage1, 0)
    game_world.add_object(monster[0], 1)
    game_world.add_object(monster[1], 1)
    #game_world.add_object(monster[2], 1)
    #game_world.add_object(monster[3], 1)
    game_world.add_object(kirby, 1)

    game_world.add_collision_group(kirby, monster[0], 'kirby:basic_monster')
    game_world.add_collision_group(kirby, monster[1], 'kirby:sword_monster')
    #game_world.add_collision_group(kirby, monster[2], 'kirby:spark_monster')
    #game_world.add_collision_group(kirby, monster[3], 'kirby:bomber_monster')

    game_world.add_collision_group(kirby, monster[0], 'kirby_skill:basic_monster')
    game_world.add_collision_group(kirby, monster[1], 'kirby_skill:sword_monster')
    #game_world.add_collision_group(kirby, monster[2], 'kirby_skill:spark_monster')
    #game_world.add_collision_group(kirby, monster[3], 'kirby_skill:bomber_monster')

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
