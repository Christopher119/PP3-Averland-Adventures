import random
from game_slow_functions import *

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
        if damage_taken <= 0:
            slow_print("You completely blocked the attack and took no damage!")
        else:
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


class Player(Character):
    """
    Creates an Instance of a Player Character Class.
    """

    def __init__(self, name, health, attack, defence,
                 speed, gold, inventory, quests, sword, shield):
        super().__init__(name, health, attack, defence, speed)
        self.max_health = 100
        self.level = 1
        self.exp = 0
        self.gold = gold
        self.inventory = inventory
        self.quests = quests
        self.sword = sword
        self.shield = shield
        self.keyitems = []

        # quest variables
        self.slimes_defeated = 0
        self.caravan_saved = False
        self.forest_6c_camp = False
        self.necklace_found = False
        self.missing_person_found = False
        self.forest_kidnapped_person = False

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


    def update_values(self, new_value):
        self.name = new_value.name
        self.health = new_value.health
        self.attack = new_value.attack
        self.defence = new_value.defence
        self.speed = new_value.speed
        self.gold = new_value.gold
        self.inventory = new_value.inventory
        self.quests = new_value.quests


    def check_status(self):
        slow_screen_clear()
        slow_print(f"Your name: {self.name}. Your level: {self.level}. Your gold: {self.gold}")
        slow_print(f"Your experience: {self.exp}/100. Your health: {self.health}/{self.max_health}")
        slow_print(f"Your attack: {self.attack}. Your defence: {self.defence}. Your speed: {self.speed}")
        slow_print(f"Your sword: {self.sword}. Your shield: {self.shield}")
        slow_print(f"Your inventory:")
        for number, items_owned in enumerate(self.inventory):
                print(number+1, items_owned)
        slow_print(f"Your quests:")
        for number, quests_owned in enumerate(self.quests):
                print(number+1, quests_owned)
        slow_print(f"Your key items:")
        for number, keys_owned in enumerate(self.keyitems):
                print(number+1, keys_owned)

        while True:
            slow_print("\nWould you like to change your equipment?")
            slow_print("1. Yes.")
            slow_print("2. No.")
            choice = input()
            try:
                if choice != str(1) and choice != str(2):
                    raise Exception

            except Exception:
                print("Please enter only 1 or 2.\n")
                slow_screen_clear()

            else:
                if choice == str(1):
                    slow_screen_clear()
                    self.equipment_display()

                else:
                    slow_print("Returning to game.")
                    slow_screen_clear()
                    return False


    def equipment_display(self):
        while True:
            available_items = 0
            for number, items_owned in enumerate(self.inventory):
                print(number+1, items_owned)
                available_items += 1
            slow_print("\nWhat would you like to equip?\n"
                       "Press 0 to return to the previous menu.")
            choice = input()
            try:
                if choice > str(available_items) and choice.alpha() is True:
                    raise Exception

            except Exception:
                slow_print("Please only enter the numbers on screen, "
                           "or 0 to return to the previous menu.")
            else:
                if choice == str(0):
                    return False

                elif choice <= str(available_items) and choice > str(0):
                    if "Sword" in adventurer.inventory[int(choice)-1]:
                        self.equip_shield(adventurer.inventory[int(choice)-1])
                        adventurer.inventory.pop(int(choice)-1)

                    elif "Shield" in adventurer.inventory[int(choice)-1]:
                        self.equip_shield(adventurer.inventory[int(choice)-1])
                        adventurer.inventory.pop(int(choice)-1)

                    else:
                        slow_print("You cannot equip that.")


    def level_up(self, xp_amount):
        self.exp += xp_amount
        slow_print(f"You earned {xp_amount} experience from your victory!")

        if self.exp >= 100:
            slow_print("You leveled up!")
            hp_up = random.randint(2, 10)
            atk_up = random.randint(1, 5)
            def_up = random.randint(1, 5)
            spd_up = random.randint(1, 5)
            self.exp = 0
            self.max_health += hp_up
            self.attack += atk_up
            self.defence += def_up
            self.speed += spd_up
            slow_print(f"Health has increased by {hp_up} points!")
            slow_print(f"Attack has increased by {atk_up} points!")
            slow_print(f"Defence has increased by {def_up} points!")
            slow_print(f"Speed has increased by {spd_up} points!")


    def equip_sword(self, sword):
        if not sword:
            self.sword = sword

        else:
            adventurer.inventory.append(self.sword)
            self.sword = sword

        slow_print(f"You have equipped a {self.sword}")
        if "Iron" in self.sword:
            self.attack += 2
        elif "Steel" in self.sword:
            self.attack += 4
        elif "Silver" in self.sword:
            self.attack += 6

        slow_screen_clear()


    def equip_shield(self, shield):
        if not self.shield:
            self.shield = shield

        else:
            adventurer.inventory.append(self.shield)
            self.shield = shield

        slow_print(f"You have equipped a {self.shield}")
        if "Iron" in self.shield:
            self.attack += 2
        elif "Steel" in self.shield:
            self.attack += 4
        elif "Silver" in self.shield:
            self.attack += 6
        slow_screen_clear()


    def block_attack(self, other_char):
        slow_print("You block the enemy attack!")
        self.defence *= 2
        other_char.attack_other(self)
        self.defence /= 2


    def recover_health(self, amount):
        """
        A simple function to restore health to a character
        and prevent it from going above 100.
        """
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
            slow_print("You are fully healed!")

        else:
            slow_print(f"You recovered {amount} health!")

        slow_print(f"You now have {self.health}.")


    def use_potion(self, amount):
        """
        A simple function using the above recover_health() function to
        restore health and print out the results.
        """
        self.recover_health(amount)
        sleep(1.5)


    def reset_flags(self):
        self.found_gold_road_1 = False
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


class Enemy(Character):
    """
    Creates an Instance of an Enemy Character Class.
    """

    def __init__(self, name, health, attack, defence, speed, loot, experience):
        super().__init__(name, health, attack, defence, speed)
        self.loot = loot
        self.experience = experience


    def drop_loot(self, player, loot):
        player.gold += self.loot
        slow_print(f"The {self.name} dropped {self.loot} gold!")


adventurer = Player("Adventurer Boy", 100, 1000, 10, 12, 1000,
                    ["Old Sword", "New Sword",  "Potion", "Silver Sword", "Silver Armor"], [], "", "")