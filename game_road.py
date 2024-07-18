from game_slow_functions import *
from game_characters import *
from game_outside_travels import move_to_town
from game_battles import *


def road_start():
    """
    This function is for the beginning of the road 'dungeon'.
    It is the start of the road leading from town, and the only way
    to return to town unless the player is at the end of the road.
    """
    while True:
        slow_print("The wall of the town is at your back as\n"
                   "you begin travelling the Merchant's Road.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Return to town.")
        slow_print("4. Check your Status.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4):
                raise Exception

        except Exception:
            print("Please enter only 1, 2, or 3.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                slow_print("You continue down the road.")
                slow_screen_clear()
                road_1()
                return False

            elif choice == str(2):
                print("It is a peaceful and pleasant day, perfect for a "
                      "leisurely walk.\nThough something tells you that "
                      "you won't have a relaxing journey.")
                slow_screen_clear()

            elif choice == str(3):
                print("You decide you are unprepared and return to town.")
                adventurer.health = adventurer.max_health
                slow_screen_clear()
                move_to_town()
                return False

            elif choice == str(4):
                adventurer.check_status()


def road_1():
    """
    This function is another 'room' in the road 'dungeon'.
    It simply contains options to continue, turn back, or
    look around.
    """
    while True:
        slow_print("You walk at a brisk pace, enjoying the refreshing air.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception
        except Exception:
            print("Please enter only 1, 2, or 3.\n")
        else:
            if choice == str(1):
                slow_print("You continue down the road.")
                slow_screen_clear()
                road_2()
                return False

            elif choice == str(2):
                if adventurer.found_gold_road_1 is not True:
                    slow_print("Your eyes scan over the road when you notice "
                               "\na small bag discarded on the roadside. You "
                               "crouch down to examine it,\nfinding it mostly "
                               "empty, save for a few coins.\n"
                               "You found 10 gold!")
                    adventurer.gold += 10
                    adventurer.found_gold_road_1 = True
                    slow_screen_clear()

                else:
                    slow_print("You see nothing else of interest.")
                    slow_screen_clear()

            elif choice == str(3):
                slow_print("You make your way back the way you came.")
                slow_screen_clear()
                road_start()
                return False


def road_2():
    """
    This function is another 'room' in the road 'dungeon'.
    It simply contains options to continue, turn back, or
    look around.
    It also has a possible random encounter versus an enemy.
    """
    enemy = random_enemy("Road")
    random_battle(enemy, 7)
    if enemy.name == "Slime":
        adventurer.slimes_defeated += 1

    while True:
        slow_print("You stay wary the further you get from a town.\n"
                   "Though merchant roads are well travelled, they "
                   "\nare also often targeted by many thieves and "
                   "monsters for that same reason.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
              and choice != str(3):
                raise Exception

        except Exception:
            print("Please enter only 1, 2, or 3.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                slow_print("You continue down the road.")
                slow_screen_clear()
                road_3()
                return False

            elif choice == str(2):
                slow_print("You wave to some passing merchants "
                           "as they head toward town.")
                slow_screen_clear()

            elif choice == str(3):
                slow_print("You make your way back the way you came.")
                slow_screen_clear()
                road_1()
                return False


def road_3():
    """
    This function is another 'room' in the road 'dungeon'.
    It simply contains options to continue, turn back, or
    look around.
    Looking will reveal a path to a side road the player
    can then choose to travel.
    """
    while True:
        slow_print("You keep your hand on the hilt of your "
                   "weapon, wary for any potential threats.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception

        except Exception:
            print("Please enter only 1, 2, or 3.\n")

        else:
            if choice == str(1):
                slow_print("You continue down the road.")
                slow_screen_clear()
                road_4()
                return False

            elif choice == str(2):
                if adventurer.road3_side_road_seen is False:
                    adventurer.road3_side_road_seen = True
                    slow_print("You notice there is a path "
                               "leading through some bushes.")

                elif adventurer.road3_side_road_seen is True:
                    slow_print("You consider the path you "
                               "noticed earlier.")

                slow_print("\nWould you like to investigate "
                           "this side road?")
                slow_print("1. Yes.")
                slow_print("2. No.")
                choice = input()
                try:
                    if choice != str(1) and choice != str(2):
                        raise Exception

                except Exception:
                    print("Please enter only 1, or 2.\n")
                    slow_screen_clear()

                else:
                    if choice == str(1):
                        slow_print("You decide to travel the side road.")
                        slow_screen_clear()
                        road_3a()
                        return False

                    elif choice == str(2):
                        slow_print("You decide it safer to stick "
                                   "to the path more trodden.")
                        slow_screen_clear()

            elif choice == str(3):
                slow_print("You make your way back the way you came.")
                slow_screen_clear()
                road_2()
                return False


def road_3a():
    """
    This function is a 'sub-room' in the road 'dungeon'
    for road_3().
    It simply contains options to turn back, or
    look around.
    Looking will reveal a path to the player
    which they can then choose to travel.
    """
    while True:
        slow_print("You move through some bushes warily.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Go back.")
        slow_print("2. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2):
                raise Exception

        except Exception:
            print("Please enter only 1, or 2.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                slow_print("You go back to the main road.")
                slow_screen_clear()
                road_3()
                return False

            elif choice == str(2):
                if adventurer.road3_tracks_found is False:
                    adventurer.road3_tracks_found = True
                    slow_print("You find some tracks in the "
                               "dirt at your feet.")

                elif adventurer.road3_tracks_found is True:
                    slow_print("You consider the tracks "
                               "you found earlier.")

                slow_print("\nWould you like to "
                           "follow them?")
                slow_print("1. Yes.")
                slow_print("2. No.")
                choice = input()
                try:
                    if choice != str(1) and choice != str(2):
                        raise Exception
                except Exception:
                    print("Please enter only 1, or 2.\n")
                    slow_screen_clear()

                else:
                    if choice == str(1):
                        slow_print("You decide to follow the tracks "
                                   "further off the road.")
                        slow_screen_clear()
                        road_3b()
                        return False

                    elif choice == str(2):
                        slow_print("You aren't sure what may be at "
                                   "the end of these tracks,\n so you "
                                   "err on the side of caution.")
                        slow_screen_clear()


def road_3b():
    """
    This function is a 'sub-room' in the road 'dungeon'
    for road_3().
    It simply contains options to turn back, or
    continue.
    It has a forced battle versus a randomised enemy.
    This enemy is stored in a variable within the character
    class to be reused in the following sub-room for a
    boss encounter.
    """
    slow_print("You follow the tracks through the bushes.")

    # generating a random enemy and assigning it to a variable
    # within the Player class to be stored for consistent encounters
    if adventurer.road3_enemy_fought is False:
        adventurer.road3_enemies = random_enemy("Road")
        battle_event(adventurer, adventurer.road3_enemies)
        adventurer.road3_enemy_fought = True
        if road3_enemies.name == "Slime":
            adventurer.slimes_defeated += 1
        slow_print("After the battle you realise that there must "
                   "be a group up ahead. It would be dangerous "
                   "to proceed...")

    else:
        slow_print(f"The body of the {adventurer.road3_enemies.name} "
                   "you defeated is still here.")

    while True:
        slow_print("\nWhat will you do?\n")
        slow_print("1. Go back.")
        slow_print(f"2. Enter the {adventurer.road3_enemies.name}'s "
                   "territory.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2):
                raise Exception

        except Exception:
            print("Please enter only 1, or 2.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                print("You go back through the bushes.")
                slow_screen_clear()
                road_3a()
                return False

            elif choice == str(2):
                if adventurer.road3_camp_fought is False:
                    slow_print("You steel yourself for the battle ahead.")

                else:
                    slow_print("You walk towards the clearing.")

                slow_screen_clear()
                road_3c()
                return False


def road_3c():
    """
    This function is a 'sub-room' in the road 'dungeon'
    for road_3().
    It has a forced battle versus the randomised enemy
    type from the previous sub-room.
    This enemy's health, attack, and name are modified
    to be more difficult in combat.
    """
    if adventurer.road3_camp_fought is False:
        slow_print("As you thought there are multiple "
                   f"{adventurer.road3_enemies.name}s here.")
        sleep(1.5)
        adventurer.road3_enemies.health += 30
        adventurer.road3_enemies.attack += 10
        adventurer.road3_enemies.name += " Group"
        battle_event(adventurer, adventurer.road3_enemies)
        adventurer.road3_camp_fought = True
        if road3_enemies.name == "Slime":
            adventurer.slimes_defeated += 3

        slow_print("After the battle you search around the area.")
        if "Missing Person" in adventurer.quests:
            slow_print("You find the missing person hiding nearby.\n")
            slow_print("You promise to help them back to the road safely.\n")
            adventurer.missing_person_found = True
        slow_print("With nothing else of value to find you return "
                   "to the main road, triumphant.")

    else:
        slow_print("The area is silent now that you have "
                   "defeated all the enemies here.")
        slow_print("You turn around and walk back towards "
                   "the main road.")
    slow_screen_clear()
    road_3()


def road_4():
    """
    This function is a 'room' in the road 'dungeon'.
    It simply contains the options to continue, turn back,
    or look around.
    It has a random encounter chance.
    Looking can reveal another path for the player to
    travel.
    """
    enemy = random_enemy("Road")
    random_battle(enemy, 5)
    if enemy.name == "Slime":
        adventurer.slimes_defeated += 1

    while True:
        slow_print("You check your map as you walk,\n"
                   "estimating you are about halfway\n"
                   "to the next town.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception

        except Exception:
            print("Please enter only 1, 2, or 3.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                slow_print("You continue down the road.")
                slow_screen_clear()
                road_5()
                return False

            elif choice == str(2):
                if adventurer.road_4_struggle_seen is False:
                    adventurer.road_4_struggle_seen = True
                    slow_print("You notice signs of a "
                               "battle leading off the road.")

                elif adventurer.road_4_struggle_seen is True:
                    slow_print("You consider the signs of "
                               "a struggle you saw earlier.")

                slow_print("\nWould you like to investigate?")
                slow_print("1. Yes.")
                slow_print("2. No.")
                choice = input()
                try:
                    if choice != str(1) and choice != str(2):
                        raise Exception

                except Exception:
                    print("Please enter only 1, or 2.\n")
                    slow_screen_clear()

                else:
                    if choice == str(1):
                        slow_print("You decide to follow the damage.")
                        slow_screen_clear()
                        road_4a()
                        return False

                    elif choice == str(2):
                        slow_print("It could be a trap.\n You decide"
                                   "to stay on the main road.")
                        slow_screen_clear()

            elif choice == str(3):
                slow_print("You make your way back the way you came.")
                slow_screen_clear()
                road_3()
                return False


def road_4a():
    """
    This function is a 'sub-room' in the road 'dungeon'
    for road_4().
    It has a forced battle versus a randomised enemy
    that is saved to the player class.
    The player can turn back or continue further from here.
    """
    slow_print("You follow the evidence of a struggle further off the road.")
    sleep(1.5)

    if adventurer.road_4_fight is False:
        adventurer.road4_enemies = random_enemy("Road")
        battle_event(adventurer, adventurer.road4_enemies)
        adventurer.road4_enemy_fought = True
        enemy = random_enemy("Road")
        if road4_enemies.name == "Slime":
            adventurer.slimes_defeated += 1
        slow_print("You take a moment to relax after the battle.\n"
                   "You have no doubt there is a group of "
                   f"{adventurer.road4_enemies.name}s ahead.")

    else:
        slow_print(f"The body of the {adventurer.road4_enemies.name} "
                   "you defeated is still here.")

    while True:
        slow_print("\nWhat will you do?\n")
        slow_print("1. Go back.")
        slow_print(f"2. Go further.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2):
                raise Exception

        except Exception:
            print("Please enter only 1, or 2.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                print("You go back to the main road.")
                slow_screen_clear()
                road_4()
                return False

            elif choice == str(2):
                if adventurer.road_4_group is False:
                    slow_print("You steel yourself for the battle ahead.")

                else:
                    slow_print("You walk towards the clearing.")

                slow_screen_clear()
                road_4b()
                return False


def road_4b():
    """
    This function is a 'sub-room' in the road 'dungeon'
    for road_3().
    It has a forced battle versus the randomised enemy
    type from the previous sub-room.
    This enemy's health, attack, and name are modified
    to be more difficult in combat.
    """
    if adventurer.road_4_group is False:
        slow_print("As you thought there are multiple "
                   f"{adventurer.road4_enemies.name}s here.\n"
                   "They have surrounded a caravan they forced\n"
                   "off the road.")
        sleep(1.5)
        adventurer.road4_enemies.health += 30
        adventurer.road4_enemies.attack += 10
        adventurer.road4_enemies.name += " Group"
        battle_event(adventurer, adventurer.road4_enemies)
        if enemy.name == "Slime":
            adventurer.slimes_defeated += 3
        adventurer.road_4_group = True

        slow_print("After the battle you search around the area.")
        slow_print("The merchants are truly thankful for your rescue\n"
                   "promising to report your deeds to the adventurer's guild.")
        adventurer.caravan_saved = True
        slow_print("With nothing else of value to find you return "
                   "to the main road, triumphant.")

    else:
        slow_print("The area is silent now that you have "
                   "defeated all the enemies here.")
        slow_print("You turn around and walk back towards "
                   "the main road.")
    slow_screen_clear()
    road_4()


def road_5():
    """
    This function is a 'room' in the road 'dungeon'.
    It simply contains the options to continue, turn back,
    or look around.
    It has a random encounter chance.
    """
    enemy = random_enemy("Road")
    random_battle(enemy, 3)
    if enemy.name == "Slime":
        adventurer.slimes_defeated += 1

    while True:
        slow_print("You pause for a moment of rest on the side of the road,\n"
                   "keeping a careful watch for any threats.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception

        except Exception:
            print("Please enter only 1, 2, or 3.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                print("You continue down the road.")
                slow_screen_clear()
                road_6()
                return False

            elif choice == str(2):
                print("Nothing catches your eye.")
                slow_screen_clear()

            elif choice == str(3):
                slow_print("You make your way back the way you came.")
                slow_screen_clear()
                road_4()
                return False


def road_6():
    """
    This function is a 'room' in the road 'dungeon'.
    It simply contains the options to continue, turn back,
    or look around.
    It has a random encounter chance.
    """
    enemy = random_enemy("Road")
    random_battle(enemy, 2)
    if enemy.name == "Slime":
        adventurer.slimes_defeated += 1

    while True:
        slow_print("The road is getting a little busier, more merchants,\n"
                   "but also more possible threats lying in wait ahead.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Continue down the road.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception

        except Exception:
            print("Please enter only 1, 2, or 3.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                slow_print("You continue down the road.")
                slow_screen_clear()
                road_7()
                return False

            elif choice == str(2):
                slow_print("There is nothing of interest.")
                slow_screen_clear()

            elif choice == str(3):
                slow_print("You make your way back the way you came.")
                slow_screen_clear()
                road_5()
                return False


def road_7():
    """
    This function is a 'room' in the road 'dungeon'.
    It simply contains the options to continue, turn back,
    or look around.
    """
    while True:
        slow_print("As you walk the road you see the "
                   "next town not far from you.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Continue towards town.")
        slow_print("2. Look around.")
        slow_print("3. Go back up the road.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3):
                raise Exception

        except Exception:
            print("Please enter only 1, 2, or 3.\n")

        else:
            if choice == str(1):
                slow_print("You continue and arrive at the next town.")
                adventurer.health = adventurer.max_health
                slow_screen_clear()
                move_to_town()
                return False

            elif choice == str(2):
                slow_print("There is nothing of interest.")
                slow_screen_clear()

            elif choice == str(3):
                slow_print("You make your way back the way you came.")
                slow_screen_clear()
                road_6()
                return False
