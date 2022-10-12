from pico2d import*
import game_framework
import map_state
import logo_state
import move_kirby

state = logo_state
def map_print():
    state.enter()
    state.draw()
    state.handle_events()

open_canvas(800, 400)

while state == logo_state or state == map_state:
    map_print()

state.exit()
close_canvas()