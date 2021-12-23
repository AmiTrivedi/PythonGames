import winsound
from playsound import playsound
import items, enemies, actions, world


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.Equip())
        moves.append(actions.Status())
        moves.append(actions.Heal())

        return moves


class Hogwarts(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        you are At LEVEL  -  3
        Welcome to Hogwarts....
        There are several war rooms....
        Each rooms have enemies and you have weapons ....
        You can make out four paths, each equally as dark and foreboding.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class QuiddichGame(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        You are At LEVEL - 2
        Welcome to Hogwarts famous Quiddich Game
        To win you have to play against four houses, each equally as powerful.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class ClassRoom(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        You are At LEVEL - 3
        Back to School...Here you have different classes of Famous 
        Hogwarts professors....They teach you Magics....
        And To win you have to pass their exams....
        By the way exams comes in terms of Enemies ....!
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy

        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Opponent does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
       Use your maps carefully... 
       Staircases are changing daily in Hogwarts...
        You must forge onwards.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class PhilosophersStone(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.ThreeHeadedDog())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound1.wav', winsound.SND_ASYNC)
            return """
            You have to Grab a stone...A ThreeHeadedDog jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead  ThreeHeadedDog  on the ground.
            """


class PrisonerOfAzkaban(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.dementors())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound2.wav', winsound.SND_ASYNC)
            return """
             A Prisoner is escaped from Azkaban..Dementors jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead dementors is on the ground.
             """


class ChamberOfSecrets(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSnake())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound3.wav', winsound.SND_ASYNC)
            return """
             You are in the Chamber of Secrets...A GiantSnake jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead snake is on the ground.
             """


class GobletOfFire(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Dragon())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound4.wav', winsound.SND_ASYNC)
            return """
             You have participated in Goblet of Fire..A Dragon jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead Dragon is on the ground.
             """


class HalfBloodPrince(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.MinistryOfMagic())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound5.wav', winsound.SND_ASYNC)
            return """
             Want to know who is Half Blood Prince? ...People of Ministry are behind you!
             """
        else:
            return """
             You have killed every one....
             """


class DeathlyHallows(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound6.wav', winsound.SND_ASYNC)
            return """
             You have to find Horcruxes.. A GiantSpider jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead GiantSpider is on the ground.
             """


class FinalWarRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Voldemort())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/war.wav', winsound.SND_ASYNC)
            return """
             Finally Voldemort is here....Fight with him....
             """
        else:
            return """
             you killed Voldemort Hurray... .
             """


class OrderOfPhoenix(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Deatheaters())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound11.wav', winsound.SND_ASYNC)
            return """
             Death Eaters are here....Death eaters jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead Death eaters is on the ground.
             """


class GryffindorHouse(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.HarryPotter())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound6.wav', winsound.SND_ASYNC)

            return """
            You might belong in Gryffindor,
            Where dwell the brave at heart,
            Their daring, nerve and chivalry
            Set Gryffindors apart."""
        else:
            return """
             You won....!
             """


class RavenclawHouse(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Lunalovegood())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound6.wav', winsound.SND_ASYNC)
            return """
             Or yet in wise old Ravenclaw
            If you’ve a ready mind
            Where those of wit and learning
            Will always find their kind."""

        else:
            return """
             You won....!
             """


class HufflepuffHouse(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Cedric())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound6.wav', winsound.SND_ASYNC)

            return """
            You might belong in Hufflepuff
            Where they are just and loyal
            Those patient Hufflepuffs are true
            And unafraid of toil."""

        else:
            return """
             You won....!
             """


class SlytherinHouse(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.DracoMalfoy())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound6.wav', winsound.SND_ASYNC)
            return """
             Or perhaps in Slytherin
            You’ll make your real friends
            Those cunning folk use any means
            To achieve their ends"""

        else:
            return """
             You won....!
             """


class FinalMatch(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.dementors())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound("sound6.wav", winsound.SND_ASYNC)
            return """
             Hurry!! you are in the final ..your match is against dementors  ..
             They are very powerful..
             ...All the best....
             """
        else:
            return """
             You won....!
             """


class DumbledoreRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.MagicWand())

    def intro_text(self):
        return """
        Your notice something shiny in the898 corner.
        It's a Magic Wand! You pick it up.
        """


class BroomstickRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Broomstick())

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a Nimbus 2001! You pick it up.
        """


class UmbridgeClass(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.MinistryOfMagic())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound7.wav', winsound.SND_ASYNC)
            return """
            The Teacher that Everyone 
            Love to hate......
            She is teaching Defence Against
            Dark Arts....
             """

        else:
            return """
            You have passed the Exam....!
             """


class LupinClass(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.dementors())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound8.wav', winsound.SND_ASYNC)
            return """
            Professor Lupin may be the most adept Defense Against the Dark Arts instructor
            Hogwarts students learn about more dangerous creatures from him.
            Best mentor ever....
            He is teaching Defence Against
            Dark Arts....
             """

        else:
            return """
            You have passed the Exam....!
             """


class HagridClass(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.MagicalCreatures())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound9.wav', winsound.SND_ASYNC)
            return """
            Well, that and his penchant for 
            assigning his students to look after magic creatures
            whose utility as educational subjects is dubious 
            at best, deadly at worst.
            He is teaching care of 
            Magical Creatures...
             """

        else:
            return """
            You have passed the Exam....!
             """


class LockhartClass(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.DarkArts())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound10.wav', winsound.SND_ASYNC)
            return """
            A famous author that used Memory Charms to 
            modify people's memories, taking credit for
             their work
            He is teaching Defence Against
            Dark Arts....
             """

        else:
            return """
            You have passed the Exam....!
             """


class SnapeClass(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Potion())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound11.wav', winsound.SND_ASYNC)
            return """
            Most hated but most loveable and skilled....
            After All This Time...Always...
            Go to page No.394......
            He is teaching Defence Against
            Dark Arts and Most Importantly
            Potions.....!
             """

        else:
            return """
            You have passed the Exam....!
             """


class DumbledoreClass(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Blessing())

    def intro_text(self):
        return """
        Exams are cancelled....You have blessing of Professor
        """


class SproutClass(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Herbology())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound12.wav', winsound.SND_ASYNC)
            return """
            Professor Sprout has got to be one of 
            the most patient educators at Hogwarts..
            Head of Hufflepuff House, Sprout is also 
            handy whenever the school's troubles call for
            the cultivation of some sort of magical herb or fungi.
            She is teaching Herbology...
             """

        else:
            return """
            You have passed the Exam....!
             """


class TrelawneyClass(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Divination())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound13.wav', winsound.SND_ASYNC)
            return """
            Conceived the prophecy of the Chosen One;
            predicted the death of a student at the
            beginning of every school year.
            She is teaching Divination...
             """

        else:
            return """
            You have passed the Exam....!
             """


class McGonagallClass(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Transfiguration())

    def intro_text(self):
        if self.enemy.is_alive():
            winsound.PlaySound('./sound/sound14.wav', winsound.SND_ASYNC)
            return """
            McGonagall may be strict, but there's no denying 
            that she cares more about her students than 
            the average Hogwarts professor.Even though she has a 
            reputation for being tough, McGonagall is the best sort
            of law enforcement — the kind who knows when it's 
            time to break the rules
            
            She is teaching Transfiguration
             """

        else:
            return """
            You have passed the Exam....!
             """


class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        Happiness can be found, even in the darkest of times, 
        if one only remembers to turn on the light
 
 
        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True


class LeaveField(MapTile):
    def intro_text(self):
        return """
        you have won the quiddich game....
        Quiddich Cup is Waiting for you...
        Join one of the House and play next matches...!!

        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True


class ResultRoom(MapTile):
    def intro_text(self):
        return """
        Hurry....! Exams are over....!!
        Now , you know the power of magic....
        But remember one thing...
        You are not Allowed to use magic
        outside the Hogwarts....!!!


        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True
