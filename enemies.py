class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2)
 
class GiantSnake(Enemy):
    def __init__(self):
        super().__init__(name="GiantSnake", hp=11, damage=3)

class ThreeHeadedDog(Enemy):
    def __init__(self):
        super().__init__(name="ThreeHeadedDog", hp=12, damage=5)

class Deatheaters(Enemy):
    def __init__(self):
        super().__init__(name="Deatheaters", hp=13, damage=7)

class dementors(Enemy):
    def __init__(self):
        super().__init__(name="dementors", hp=14, damage=6)

class Voldemort(Enemy):
    def __init__(self):
        super().__init__(name="Voldemort", hp=15, damage=8)

class MinistryOfMagic(Enemy):
    def __init__(self):
        super().__init__(name="MinistryOfMagic", hp=16, damage=9)

class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Dragon", hp=17, damage=11)


class HarryPotter(Enemy):
    def __init__(self):
        super().__init__(name="HarryPotter", hp=18, damage=12)

class Cedric(Enemy):
    def __init__(self):
        super().__init__(name="Cedric", hp=19, damage=10)

class Lunalovegood(Enemy):
    def __init__(self):
        super().__init__(name="Lunalovegood", hp=20, damage=11)

class DarkArts(Enemy):
    def __init__(self):
        super().__init__(name="DarkArts", hp=21, damage=13)

class MagicalCreatures(Enemy):
    def __init__(self):
        super().__init__(name="MagicalCreatures", hp=22, damage=11)

class Potion(Enemy):
    def __init__(self):
        super().__init__(name="Potion", hp=23, damage=14)

class LifeLession(Enemy):
    def __init__(self):
        super().__init__(name="LifeLession", hp=24, damage=8)

class Herbology(Enemy):
    def __init__(self):
        super().__init__(name="LifeLession", hp=25, damage=13)

class Divination(Enemy):
    def __init__(self):
        super().__init__(name="Divination", hp=26, damage=12)

class Transfiguration(Enemy):
    def __init__(self):
        super().__init__(name="Transfiguration", hp=27, damage=15)


class DracoMalfoy(Enemy):
    def __init__(self):
        super().__init__(name="DracoMalfoy", hp=10, damage=16)



