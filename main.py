from pico2d import*
import game_framework
import map_state
import logo_state

states = [logo_state, map_state]
def state_print(a):
    a.enter()
    a.draw()
    a.update()
    a.handle_events()


open_canvas(800, 400)

for state in states:
    while state == logo_state or state == map_state:
        state_print(state)

state.exit()
close_canvas()