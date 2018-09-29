from enum import Enum

class Positions(Enum):
    MOUTH_OPEN_LEFT = 0
    MOUTH_OPEN_RIGHT = 1
    MOUTH_OPEN_CENTRE = 2
    MOUTH_CLOSED_LEFT = 3
    MOUTH_CLOSED_RIGHT = 4
    MOUTH_CLOSED_CENTRE = 5

class Character:
    def __init__(self, filename, player_name=""):
        """ filename    - character file
            player_name - player assigned character name
        """
        self.character_name = filenname.split('.')[0]
        self.player_name = player_name
        with open(filename, 'r') as f:
            all_animations = f.read()
            self.animations_list = f.split('*******')

    def get_position(position):
        return self.animations_list[position]
