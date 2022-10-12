from pico2d import*
import game_framework
import map_state
import logo_state
import move_kirby


def state_print():
    state.enter()
    state.draw()
    state.handle_events()

states = [logo_state, map_state]
for state in states:
    while state == logo_state or state == map_state:
        state_print()


open_canvas(800, 400)



state.exit()
close_canvas()