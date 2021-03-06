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

    while True:
        s.place(character.get_position(random.choice(range(6))), 30, 0)
        s.draw()
        time.sleep(1)

