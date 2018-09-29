import time
import shutil

class Screen:
    def __init__(self):
        self.screen_height, self.width = shutil.get_terminal_size()
        self.height = 10
        self.clear()

    def clear(self):
        self.grid = [[' ']*self.width for row in range(self.height)]

    def place(self, sprite, x, y):
        """ 0, 0 is in top edge and increases going right and down
            NB. places sprites over each other. Last to be placed is on top
            sprite - the string to place
            x      - the horizontal co-ord
            y      - the vertical co-ord
        """
        x_start = x
        for line in sprite.split('\n'):
            for char in line:
                self.grid[y][x] = char
                x += 1
            x = x_start
            y += 1

    def draw(self):
        for line in range(self.screen_height-self.height):
            print()
        for line in self.grid:
            print(''.join(line))
        print("-----------------------------------------")
        self.clear()
