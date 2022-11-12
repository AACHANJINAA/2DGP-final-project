from pico2d import*
import game_framework
import game_world

from move_kirby import Kirby
from move_sword import Sword_Kirby
from move_spark import Spark_Kirby
from move_bomber import Bomber_Kirby
from Background import SWORD_BACK, SPARK_BACK, BOMBER_BACK
from Background import SWORD_BOSS, SPARK_BOSS, BOMBER_BOSS, LAST_BOSS
from boss import BOSS1, BOSS2, BOSS3, BOSS4
from move_monster import BASIC_MONSTER, SWORD_MONSTER, SPARK_MONSTER, BOMBER_MONSTER

kirby, sword_kirby, spark_kirby, bomber_kirby = None, None, None, None
stage1, stage2, stage3 = None, None, None
stage4, stage5, stage6, stage7 = None, None, None, None
monster1, monster2, monster3, monster4 = None, None, None, None
boss1, boss2, boss3, boss4 = None, None, None, None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            kirby.handle_event(event)
            sword_kirby.handle_event(event)
            spark_kirby.handle_event(event)
            bomber_kirby.handle_event(event)

def enter():
    global kirby, sword_kirby, spark_kirby, bomber_kirby
    global stage1, stage2, stage3
    global stage4, stage5, stage6, stage7
    global boss1, boss2, boss3, boss4
    global monster1, monster2, monster3, monster4
    
    a, b, c = None, None, None

    kirby = Kirby()
    sword_kirby = Sword_Kirby()
    spark_kirby = Spark_Kirby()
    bomber_kirby = Bomber_Kirby()

    stage1 = SWORD_BACK(0)
    stage2 = SPARK_BACK(0)
    stage3 = BOMBER_BACK(0)

    stage4 = SWORD_BOSS(0)
    stage5 = SPARK_BOSS(0)
    stage6 = BOMBER_BOSS(0)
    stage7 = LAST_BOSS(0)

    monster1 = BASIC_MONSTER()
    monster2 = SWORD_MONSTER()
    monster3 = SPARK_MONSTER()
    monster4 = BOMBER_MONSTER()

    # 봄버 스파크 칼 디디디마왕순
    boss1 = BOSS1()
    boss2 = BOSS2()
    boss3 = BOSS3()
    boss4 = BOSS4()

    name = 'bomber'

    if name == 'sword':
        c = monster2
        b = sword_kirby
        a = stage1
    elif name == 'spark':
        c = monster3
        b = spark_kirby
        a = stage2
    elif name == 'bomber':
        c = monster4
        b = bomber_kirby
        a = stage5
    elif name == 'sword_boss':
        c = boss3
        b = sword_kirby
        a = stage4
    elif name == 'spark_boss':
        c = boss2
        b = spark_kirby
        a = stage5
    elif name == 'bomber_boss':
        c = boss1
        b = bomber_kirby
        a = stage6
    elif name == 'last':
        c = boss4
        b = kirby
        a = stage7
    
    game_world.add_object(a, 0)
    game_world.add_object(c, 1)
    game_world.add_object(b, 2)

def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.01)

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
