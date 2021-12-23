import player
from player import Player

_world = {}
starting_position = (0, 0)


#Player.level = 1
def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    print("""            Welcome to the wizard's world..""")
    print("""            If you are a fan of Hogwarts and Harry Potter...""")
    print("""            then this game is for you ... There are 3 levels of this game...""")
    print("""            They will take you to the wizarding world... GO and PLAY..""")
    print("""            Enter the levels for the game:""")
    level_input = int(input('level: '))
    print(level_input)
    if level_input == 1:
        Player.level = level_input
        print("you have entered level 1..")
    elif level_input == 2:
        print("you have entered level 2.....")
        Player.level = level_input
    else:
        print("you have entered level 3.....")
    if level_input == 2:
        with open('map2.txt', 'r') as f:
            rows = f.readlines()
        x_max = len(rows[0].split('|'))  # Assumes all rows contain the same number of tabs
        for y in range(len(rows)):
            cols = rows[y].split('|')
            for x in range(x_max):
                tile_name = cols[x].replace('\n', '')  # Windows users may need to replace '\r\n'
                if tile_name == 'QuiddichGame':
                    global starting_position
                    starting_position = (x, y)
                _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)
    elif level_input == 1:
        with open('map.txt', 'r') as f:
            rows = f.readlines()
        x_max = len(rows[0].split('|'))  # Assumes all rows contain the same number of tabs
        for y in range(len(rows)):
            cols = rows[y].split('|')
            for x in range(x_max):
                tile_name = cols[x].replace('\n', '')  # Windows users may need to replace '\r\n'
                if tile_name == 'Hogwarts':
                    starting_position = (x, y)
                _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)

    else:
        with open('map3.txt', 'r') as f:
            rows = f.readlines()
        x_max = len(rows[0].split('|'))  # Assumes all rows contain the same number of tabs
        for y in range(len(rows)):
            cols = rows[y].split('|')
            for x in range(x_max):
                tile_name = cols[x].replace('\n', '')  # Windows users may need to replace '\r\n'
                if tile_name == 'ClassRoom':
                    starting_position = (x, y)
                _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)
def tile_exists(x, y):
    return _world.get((x, y))
