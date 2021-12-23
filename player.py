import random
from importlib import util

import items, world

class Player():
    level = None

    def __init__(self):
        self.inventory = [items.ExpectoPatronum(), items.Sword(), items.Alohomora(),
                          items.Seeker(), items.PetrificusTotalus(), items.Keeper()] #Inventory on startup
        self.hp = 200 # Health Points
        self.location_x, self.location_y = world.starting_position  #(0, 0)
        self.victory = False #no victory on start up
        self.maxHp = 200
        self.experience = 0
        self.level = 1
        self.money = 30
        self.attackPower = 100

        self.chosenWpn = False
        self.armor = False
        self.currentWpn = self.inventory[1]

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])



    # is_alive method
    def is_alive(self):
        return self.hp > 0   #Greater than zero value then you are still alive
 
    def equip(self):
        print("\nThese are the Weapons you currently possess.\n")
        print("\n You will need all of them for 3 levels....\n")
        print("\n Use your weapons wisely....Don't break the rules....\n")
        print("\n You can also use potions to heal yourself....")
        print("\n Attention: Potions are limited....")

        weapon_list = []


        for item in self.inventory:
            if isinstance(item, items.Weapon): #if item is weapon..
                weapon_list.append(item)  #Add it to weapon list
        i = 1

        for weapon in weapon_list:
            print(i,". ",weapon.name, sep='')
            i+=1
        #input validation to get int from  user in  proper range
        while True:
            itemChoice = int(input("""\nSelect the weapon you want to equip:""")) - 1
            print(itemChoice)
            if itemChoice not in range(0,len(weapon_list)):
                print("\n Invalid weapon choice")
                continue
            break
        print('\n')
        print(weapon_list[itemChoice].name, "equipped.\n")
        self.currentWpn = weapon_list[itemChoice]
        self.chosenWpn = True
#        print(self.currentWpn)
 #       print(self.currentWpn.name)
#        weapon = self.currentWpn

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())
 
    def move_north(self):
        self.move(dx=0, dy=-1)
 
    def move_south(self):
        self.move(dx=0, dy=1)
 
    def move_east(self):
        self.move(dx=1, dy=0)
 
    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):

        if self.chosenWpn == True:
            best_weapon = self.currentWpn
        else:
            best_weapon = None
            max_dmg = 0
            for i in self.inventory:
                if isinstance(i, items.Weapon):
                    if i.damage > max_dmg:
                        max_dmg = i.damage
                        best_weapon = i

        print("You use {} against {}!".format(best_weapon.name, enemy.name))
      #  self.currentWpn = best_weapon.name
        self.currentWpn.name = best_weapon.name
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You won against {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def status(self):

        print(" * current HP: {} /".format(self.hp), "{}\n".format(self.maxHp))
        print(" * Attack Power: {}\n".format(self.attackPower))
        print(" * you are at level: {}\n".format(Player.level))
        print(" * You have currently used this weapon: {}\n".format(self.currentWpn.name))

    def heal(self):
        print("\n These are the potions you currently possess.\n")
        potion_list = []

        for potion in self.inventory:
                if isinstance(potion, items.Potion): #If item is this class..
                    if potion.amt <= 0:
                        self.inventory.remove(potion)
                        continue #skips this potion which you have none of
                    else:
                        potion_list.append(potion) #Add it to item_list
        i=1
        for potion in potion_list:
            print(i,". ", potion.name, sep='')
            i+=1
        while True:
            if len(potion_list) == 0:
                print("You have no potions...")
                return None #No potions, get out of method

            itemChoice = int(input("""\n Select a potion:""")) - 1

            if itemChoice not in range(0,len(potion_list)):
                print("\n Invalid choice")
                continue
            break
        self.healToPlayer(itemChoice, potion_list)

    def healToPlayer(self, itemChoice, potionList): # logic for healing player
        chosenPotion = potionList[itemChoice]
        print("\n Your are healed for {} ".format(chosenPotion.health))
        print("hp. \n")
        self.hp = self.hp + chosenPotion.health
        chosenPotion.amt = chosenPotion.amt - 1
        if chosenPotion.amt == 0:
            self.inventory.remove(chosenPotion)

       # if self.maxHp < self.hp:
        #    self.hp = self.maxHp

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
                action_method(**kwargs)