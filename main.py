import os
import time
import random
from character import Character, Positions
from screen import Screen

def get_character_list():
    character_files = os.listdir('./characters')
    character_names = [name.split('.')[0] for name in character_files]
    character_files = ['characters/' + name for name in character_files]
    return character_names, character_files

def random_walk(character, screen, prev_x):
    movements = [0]
    if prev_x + character.width + 2 < screen.width - 1:
        movements.append(2)
    if prev_x >= 2:
        movements.append(-2)

    move = random.choice(movements)
    animation = character.get_animation_by_direction(move)

    new_x = prev_x + move

    screen.place(animation, new_x, 0)

    return new_x

if __name__ == "__main__":
    character_names, character_files = get_character_list()
    print("Which character would you like to play with?")
    print("\n".join(character_names))

    name = ""
    while name not in character_names:
        name = input("> ")

    idx = character_names.index(name)
    character = Character(character_files[idx])

    s = Screen()

    x = s.width // 2

    while True:
        x = random_walk(character, s, x)
        s.draw()
        time.sleep(1)
