import random

class Positions:
    MOUTH_OPEN_LEFT = 0
    MOUTH_OPEN_RIGHT = 1
    MOUTH_OPEN_CENTRE = 2
    MOUTH_CLOSED_LEFT = 3
    MOUTH_CLOSED_RIGHT = 4
    MOUTH_CLOSED_CENTRE = 5

    LEFT   = [MOUTH_OPEN_LEFT, MOUTH_CLOSED_LEFT]
    CENTRE = [MOUTH_OPEN_CENTRE, MOUTH_CLOSED_CENTRE]
    RIGHT  = [MOUTH_OPEN_RIGHT, MOUTH_CLOSED_RIGHT]

class Character:
    def __init__(self, filename, player_name=""):
        """ filename    - character file
            player_name - player assigned character name
        """
        self.character_name = filename.split('.')[0]
        self.player_name = player_name
        with open(filename, 'r') as f:
            all_animations = f.read()
            self.animations_list = all_animations.split('********')
            self.width = max([len(line) for line in all_animations.split('\n')])
            self.height = max([len(animation.split('\n')) for animation in self.animations_list])

    def get_animation(self, position):
        return self.animations_list[position]

    def get_animation_by_direction(self, direction=0):
        """ Gets a random animation for the character facing a direction.
            direction - integer, if positive then right, negative left and 0 centre
        """
        if direction < 0:
            return self.animations_list[random.choice(Positions.LEFT)]
        if direction == 0:
            return self.animations_list[random.choice(Positions.CENTRE)]
        if direction > 0:
            return self.animations_list[random.choice(Positions.RIGHT)]
        raise ValueError("Incorrect direction argument")
