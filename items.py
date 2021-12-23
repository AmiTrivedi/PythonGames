

# Base class for all items
class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description # attribute of the Item class and any subclasses
        self.value = value # attribute of the Item class and any subclasses
    
    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Extend the Items class



class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Potion(Item):
    def __init__(self, name, description, value, amt, health):
        self.amt = amt
        self.health = health
        super().__init__(name, description, value)
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nHealth: {}".format(self.name, self.description, self.value, self.health)


class Potion1(Potion):
    def __init__(self):
        super().__init__(name="Small Potion",
                         description="A small potion.",
                         value=5,
                         amt=2,
                         health=10)
class Potion2(Potion):
    def __init__(self):
        super().__init__(name="Booster Potion",
                         description="A Booster potion.",
                         value=5,
                         amt=2,
                         health=15)

class Potion3(Potion):
    def __init__(self):
        super().__init__(name="Power Potion",
                         description="A Powerpack potion.",
                         value=5,
                         amt=1,
                         health=25)



 
class MagicWand(Weapon):
    def __init__(self):
        super().__init__(name="MagicWand",
                         description="A Magic Wand is here... Use Magic power.....",
                         value=10,
                         damage=15)



class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="A Sword is very sharp than Knife.",
                         value=2,
                         damage=3)





class Blessing(Weapon):
    def __init__(self):
        super().__init__(name="Blessing",
                         description="Blessing will create a Magic.",
                         value=3,
                         damage=10)


class Keeper(Weapon):
    def __init__(self):
        super().__init__(name="Keeper",
                         description="Use keeper against players.",
                         value=4,
                         damage=5)

class Seeker(Weapon):
    def __init__(self):
        super().__init__(name="Seeker",
                         description="Use seeker against players.",
                         value=2,
                         damage=5)

class Beaters(Weapon):
    def __init__(self):
        super().__init__(name="Beaters",
                         description="Use Beaters against players.",
                         value=2,
                         damage=12)

class Broomstick(Weapon):
    def __init__(self):
        super().__init__(name="Broomstick",
                         description="Broomstick can be used as a weapon.",
                         value=7,
                         damage=11)

class Ridikulus(Weapon):
    def __init__(self):
        super().__init__(name="Ridikulus",
                         description="This boggart-banishing spell takes something scary and turns it into something silly.",
                         value=10,
                         damage=13)

class Alohomora(Weapon):
    def __init__(self):
        super().__init__(name="Alohomora",
                         description="Forgot your keys? Sneaking into a place you don't belong? "
                         "Managing mischief? This unlocking charm means you'll never need a locksmith again..",
                         value=11,
                         damage=9)

class PetrificusTotalus(Weapon):
    def __init__(self):
        super().__init__(name="PetrificusTotalus",
                         description="A pretty basic spell for a young "
                         "wizard or witch, this is a full-body-bind curse."
                         "You can easily paralyze your opponent with this little spell,.",
                         value=12,
                         damage=8)

class WingardiumLeviosa(Weapon):
    def __init__(self):
        super().__init__(name="WingardiumLeviosa",
                         description="One of the first spells taught to underclassmen at Hogwarts, "
                         "this levitation charm can make objects like feathers fly or levitate.",
                         value=10,
                         damage=7)

class Expelliarmus(Weapon):
    def __init__(self):
        super().__init__(name="Expelliarmus",
                         description="Go on the defensive with this disarming"
                         "incantation that knocks things, like your opponent's wand, out of hand..",
                         value=13,
                         damage=15)

class ExpectoPatronum(Weapon):
    def __init__(self):
        super().__init__(name="ExpectoPatronum",
                         description="This is undoubtedly the most popular spell in the film series. "
                         "This powerful defensive incantation"
                         " uses a happy memory to conjure something positive, "
                         "like a silvery-white animal that can chase off Dementors.",
                         value=2,
                         damage=20)