from slow_functions import *

class Character:
    """
    Creates an Instance of a Character Class.
    """

    def __init__(self, name, health, attack, defence, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        self.speed = speed

    def attack_other(self, other_char):
        """
        A function allowing one character to reduce another characters health
        """
        damage_taken = self.attack - (other_char.defence / 2.5)
        other_char.health -= damage_taken
        slow_print(f"{other_char.name} took {damage_taken} damage!")
        if other_char.health > 0:
            slow_print(f"{other_char.name} has {other_char.health} "
                       "health remaining!")
        elif other_char.health <= 0:
            other_char.health = 0
            slow_print(f"{other_char.name} has no health remaining!")

    def check_life(self):
        """
        A simple function to check if the character still has health.
        If the health is equal to or below 0 it returns True for checks.
        """
        if self.health <= 0:
            self.health = 0
            return True

    def recover_health(self, amount):
        """
        A simple function to restore health to a character
        and prevent it from going above 100.
        """
        self.health += amount
        if self.health > 100:
            self.health = 100
            slow_print("You are fully healed!")
        else:
            slow_print(f"You recovered {amount} health!")

    def use_potion(self, amount):
        """
        A simple function using the above recover_health() function to
        restore health and print out the results.
        """
        self.recover_health(amount)
        slow_print(f"You now have {player.health}.")
        sleep(1.5)


class Player(Character):
    """
    Creates an Instance of a Player Character Class.
    """

    def __init__(self, name, health, attack, defence,
                 speed, gold, inventory, quests):
        super().__init__(name, health, attack, defence, speed)
        self.gold = gold
        self.inventory = inventory
        self.quests = quests
        self.keyitems = []
        # variables used for checks through dungeons
        # will be reset to default on return to town
        # road variables
        self.found_gold_road_1 = False
        # road_3 variables
        self.road3_side_road_seen = False
        self.road3_tracks_found = False
        self.road3_enemy_fought = False
        self.road3_camp_fought = False
        # road_4 variables
        self.road_4_struggle_seen = False
        self.road_4_fight = False
        self.road_4_group = False

        # forest variables
        self.forest1b_gold_found = False
        self.forest3a_camp = False
        self.forest3c_camp_enemy = 0
        self.room4bitem = False
        self.necklace_found = False
        self.forest_6c_camp = False

    def block_attack(self, other_char):
        slow_print("You block the enemy attack!")
        self.defence *= 2
        other_char.attack_other(self)
        self.defence /= 2

    def reset_flags(self):
        self.road3_side_road_seen = False
        self.road3_tracks_found = False
        self.road3_enemy_fought = False
        self.road3_camp_fought = False
        self.road_4_struggle_seen = False
        self.road_4_fight = False
        self.road_4_group = False
        self.forest1b_gold_found = False
        self.forest3a_camp = False
        self.forest3c_camp_enemy = 0
        self.room4bitem = False
        self.necklace_found = False
        self.forest_6c_camp = False
        self.forest_rescue = False


class Enemy(Character):
    """
    Creates an Instance of an Enemy Character Class.
    """

    def __init__(self, name, health, attack, defence, speed, loot):
        super().__init__(name, health, attack, defence, speed)
        self.loot = loot

    def drop_loot(self, player, loot):
        player.gold += self.loot
        slow_print(f"The {self.name} dropped {self.loot} gold!")