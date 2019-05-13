# PvP
# Not finished
from generation.py import *

SETTINGS_FILE = 'settings.txt'


a, b = pole_size_from_settings(SETTINGS_FILE)
pole = generation(a, b)

end_of_game = False
cur_player = 1
while not end_of_game:
    


