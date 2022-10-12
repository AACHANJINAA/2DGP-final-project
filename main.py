from pico2d import*
import game_framework
import map_state

state = map_state

def map_print():
    state.enter()
    state.basic_map()
    state.handle_events()

open_canvas(800, 399)

while state == map_state:
    map_print()

close_canvas()