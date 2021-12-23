import player
from player import Player
 
class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs
 
    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)



class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name='Move north', hotkey='n')
 
 
class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move south', hotkey='s')
 
 
class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move east', hotkey='e')
 
 
class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move west', hotkey='w')
 
 
class ViewInventory(Action):
    """Prints the player's inventory"""
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View inventory', hotkey='i')

class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey='a', enemy=enemy)

class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Flee", hotkey='f', tile=tile)

class Equip(Action):
    """prints the player's inventory and ask for weapons"""
    def __init__(self):
        super().__init__(method=Player.equip, name='Equip', hotkey='q')

class Heal(Action):
    """Heals the player"""
    def __init__(self):
        super().__init__(method=Player.heal, name="Heal", hotkey='h')

class Status(Action):
    """displays Player's level,health power,xp"""
    def __init__(self):
        super().__init__(method=Player.status, name="Status", hotkey='t')
