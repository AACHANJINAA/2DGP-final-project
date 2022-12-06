kirby = None
monster = [None, None, None, None]
boss = [None, None, None, None]
background = [None, None, None, None,
              None, None, None,
              None, None, None, None]
skill = None
stage_number = 0
potal_number = 0
stage_replay = None
stage_restart = None
mode = 0
other_boss_die = None
last_boss_die = None

def server_reset():
    global monster, boss, background, skill, stage_number, potal_number, stage_replay
    global mode, other_boss_die, last_boss_die
    monster = [None, None, None, None]
    boss = [None, None, None, None]
    background = [None, None, None, None,
                  None, None, None,
                  None, None, None, None]
    skill = None
    stage_number = 0
    potal_number = 0
    stage_replay = None
    mode = 0
    other_boss_die = None
    last_boss_die = None