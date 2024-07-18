from game_slow_functions import *
from game_characters import *
from game_outside_travels import move_to_town
from game_battles import *


def forest_start():

    slow_print("You arrive at the entrance to the nearby forest.\n"
               "Tales of monsters dens and hidden riches bid many\n"
               "adventurer to tackle it.\n")

    while True:
        slow_print("You are at the entrance to the forest.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Head deeper into the forest.")
        slow_print("2. Look around.")
        slow_print("3. Return to town.")
        slow_print("4. Check your Status.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4):
                raise Exception

        except Exception:
            print("Please enter only 1, 2, or 3.")
            slow_screen_clear()

        else:
            if choice == str(1):
                slow_print("You press through the trees and bushes.")
                slow_screen_clear()
                forest_room1a()
                return False

            elif choice == str(2):
                slow_print("The canopy of trees obscures much of the light "
                           "from the sun,\nallowing only a few dappled rays "
                           "to shine through. There is a\nsmall road leading "
                           "into the forest proper that you can follow\n"
                           "for a certain distance.")
                slow_screen_clear()

            elif choice == str(3):
                slow_print("You decide you are unprepared and return to town.")
                slow_screen_clear()
                move_to_town()
                return False

            elif choice == str(4):
                adventurer.check_status()


def forest_room1a():

    slow_print("A few animals dash into the bushes\n"
               "as you walk into a small clearing.")

    while True:
        slow_print("You are standing in a small "
                   "clearing with some small animals.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Go North.")
        slow_print("2. Go West")
        slow_print("3. Go South.")
        slow_print("4. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4):
                raise Exception

        except Exception:
            slow_print("Please enter only 1, 2, 3 or 4.")

        else:
            if choice == str(1):
                slow_print("You head north.")
                slow_screen_clear()
                forest_room2a()
                return False

            elif choice == str(2):
                slow_print("You head west.")
                slow_screen_clear()
                forest_room1b()
                return False

            elif choice == str(3):
                slow_print("You head south.")
                slow_screen_clear()
                forest_start()
                return False

            elif choice == str(4):
                slow_print("The bushes rustle as some critters scurry"
                           "around in the underbrush.")
                slow_screen_clear()


def forest_room1b():

    while True:
        slow_print("Some birds are chirping nearby as you \n"
                   "make your way through the dense foliage.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Go North.")
        slow_print("2. Go East")
        slow_print("3. Look around.")
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
                slow_print("You head north.")
                slow_screen_clear()
                forest_room2b()
                return False

            elif choice == str(2):
                slow_print("You head east.")
                slow_screen_clear()
                forest_room1a()
                return False

            elif choice == str(3):
                if adventurer.forest1b_gold_found is False:
                    slow_print("You notice something glittering "
                               "in the grass at your feet.")
                    slow_print("You found 5 gold coins!")
                    adventurer.gold += 5

                else:
                    slow_print("You find nothing else of interest.")
                    slow_screen_clear()


def forest_room1c():

    slow_print("The air suddenly feels lighter as you "
               "come across a \nsmall spring. The water "
               "seems to shimmer as you look at it.")

    while True:
        slow_print("You are standing by a small spring.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Go back the way you came.")
        slow_print("2. Drink from the spring.")
        slow_print("3. Look around.")
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
                slow_print("You turn around and leave the "
                           "small spring behind you.")
                slow_screen_clear()
                forest_room2c()
                return False

            elif choice == str(2):
                slow_print("You kneel by the edge of the water, "
                           "scooping a handful \nof it into your mouth."
                           "You feel invigorated as you drink it!")
                adventurer.recover_health(20)
                slow_screen_clear()

            elif choice == str(3):
                slow_print("The area seems to almost shine with "
                           "a mystical glow.")
                slow_screen_clear()


def forest_room2a():

    enemy = random_enemy("Forest")
    random_battle(enemy, 5)
    if enemy.name == "Slime":
        adventurer.slimes_defeated += 1

    slow_print("Your tunic tears on a sharp branch as "
               "you walk deeper into the forest.")

    while True:
        slow_print("You are standing amongst some sharp branches.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Go West.")
        slow_print("2. Go East")
        slow_print("3. Go South.")
        slow_print("4. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4):
                raise Exception

        except Exception:
            print("Please enter only 1, 2, 3, or 4.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                slow_print("You head West.")
                slow_screen_clear()
                forest_room2b()
                return False

            elif choice == str(2):
                slow_print("You head East.")
                slow_screen_clear()
                forest_room2c()
                return False

            elif choice == str(3):
                slow_print("You head South.")
                slow_screen_clear()
                forest_room1a()
                return False

            elif choice == str(4):
                slow_print("There are strange markings on some of the trees.\n"
                           "Perhaps territorial warning signs from some \n"
                           "bandits or monsters.")
                slow_screen_clear()
    # forest 1a, 2b, 2c


def forest_room2b():

    enemy = random_enemy("Forest")
    random_battle(enemy, 3)
    if enemy.name == "Slime":
        adventurer.slimes_defeated += 1

    slow_print("The trees are particularly dense in this part of the \n"
               "forest, making it difficult to move quickly.")

    while True:
        slow_print("You are standing where the trees are growing densely.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Go North.")
        slow_print("2. Go East")
        slow_print("3. Go South.")
        slow_print("4. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4):
                raise Exception

        except Exception:
            print("Please enter only 1, 2, 3, or 4.\n")
            slow_screen_clear()
        else:
            if choice == str(1):
                slow_print("You head North.")
                slow_screen_clear()
                forest_room3b()
                return False

            elif choice == str(2):
                slow_print("You head East.")
                slow_screen_clear()
                forest_room2a()
                return False

            elif choice == str(3):
                slow_print("You head South.")
                slow_screen_clear()
                forest_room1b()
                return False

            elif choice == str(4):
                slow_print("You notice more of those marking on the "
                           "trees as you move between them.")
                slow_screen_clear()


def forest_room2c():

    slow_print("The forest seems strangely quiet now... \n"
               "Perhaps there is a danger ahead?")

    while True:
        slow_print("You are at a quiet spot in the forest.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Go West")
        slow_print("2. Go South.")
        slow_print("3. Look around.")
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
                slow_print("You head West.")
                slow_screen_clear()
                forest_room2a()
                return False

            elif choice == str(2):
                slow_print("You head South.")
                slow_screen_clear()
                forest_room1c()
                return False

            elif choice == str(3):
                slow_print("You can't see anything out of the ordinary "
                           "\nunder the shade of the forest canopy.")
                slow_screen_clear()


def forest_room3a():
    if adventurer.forest3a_camp is False:
        forest_room3a_campfight()

    else:
        forest_room3a_campdefeat()


def forest_room3a_campfight():
    while True:
        adventurer.forest3c_camp_enemy = random_enemy("Forest")
        adventurer.forest3c_camp_enemy.name += " Group"
        slow_print("You press up against a tree as you hear "
                   "noises ahead.\nYou peer around the "
                   "trunk and notice some shadows moving \n"
                   "just up ahead. It may be a group "
                   "of monsters...")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Try to sneak past.")
        slow_print("2. Step into the open.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2):
                raise Exception

        except Exception:
            print("Please enter only 1 or 2.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                if adventurer.speed > random.randint(7, 13):
                    slow_print("You successfully skirt your "
                               "way past the group.")
                    slow_screen_clear()
                    forest_room3a_campdefeat()
                    return False

                else:
                    slow_print("A cry yells out followed by "
                               "a rush of movement!")
                    slow_print("You've been seen! "
                               "Prepare to fight!")
                    adventurer.forest3c_camp_enemy.health += 30
                    adventurer.forest3c_camp_enemy.attack += 15
                    random_battle(adventurer.forest3c_camp_enemy, -1)
                    adventurer.forest3a_camp = True
                    if forest3c_camp_enemy.name == "Slime":
                        adventurer.slimes_defeated += 3
                    slow_screen_clear()
                    forest_room3a_campdefeat()
                    return False

            elif choice == str(2):
                slow_print("You sneak closer and see a "
                           f"{adventurer.forest3c_camp_enemy.name} \n"
                           "gathered up ahead.\nYou manage to "
                           "take one out before the group notices.")
                slow_print("Prepare to fight!")
                adventurer.forest3c_camp_enemy.health += 20
                adventurer.forest3c_camp_enemy.attack += 10
                random_battle(adventurer.forest3c_camp_enemy, -1)
                adventurer.forest3a_camp = True
                if forest3c_camp_enemy.name == "Slime":
                    adventurer.slimes_defeated += 3
                slow_screen_clear()
                forest_room3a_campdefeat()
                return False


def forest_room3a_campdefeat():
    while True:
        if adventurer.forest3a_camp is True:
            slow_print("The bodies of the "
                       f"{adventurer.forest3c_camp_enemy.name}"
                       " lay on the ground where you defeated them.")
        else:
            slow_print("The noise from the nearby group "
                       "slowly fades as you sneak away.")

        slow_print("\nWhat will you do?\n")
        slow_print("1. Go East")
        slow_print("2. Go West.")
        slow_print("3. Look around.")
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
                slow_print("You head East.")
                slow_screen_clear()
                forest_room3c()
                return False

            elif choice == str(2):
                slow_print("You head West.")
                slow_screen_clear()
                forest_room3b()
                return False

            elif choice == str(3):
                slow_print("There is an array of scattered objects on "
                           "the ground, no doubt from that group.")
                slow_screen_clear()


def forest_room3b():

    enemy = random_enemy("Forest")
    random_battle(enemy, 6)
    if enemy.name == "Slime":
        adventurer.slimes_defeated += 1

    slow_print("A sweet scent reaches your nose as you push "
               "through some bushes. Perhaps there is a fresh flower "
               "blooming nearby.")

    while True:
        slow_print("You are standing by some flowering bushes.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Go North")
        slow_print("2. Go East.")
        slow_print("3. Go South.")
        slow_print("4. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4):
                raise Exception

        except Exception:
            print("Please enter only 1, 2, 3, or 4.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                slow_print("You head North.")
                slow_screen_clear()
                forest_room4b()
                return False

            elif choice == str(2):
                slow_print("You head East.")
                slow_screen_clear()
                forest_room3a()
                return False

            elif choice == str(3):
                slow_print("You head South.")
                slow_screen_clear()
                forest_room2b()
                return False

            elif choice == str(4):
                slow_print("You see a flowerbed blooming under "
                           "the shade of a fallen log.")
                slow_screen_clear()


def forest_room3c():

    enemy = random_enemy("Forest")
    random_battle(enemy, 3)
    if enemy.name == "Slime":
        adventurer.slimes_defeated += 1

    slow_print("The forest is getting denser the deeper you go. \n"
               "It looks like there's only one path forward.")

    while True:
        slow_print("You are standing in a cramped "
                   "path through the trees.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Go North")
        slow_print("2. Go West.")
        slow_print("3. Look around.")
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
                slow_print("You head North.")
                slow_screen_clear()
                forest_room4c()
                return False

            elif choice == str(2):
                slow_print("You head West.")
                slow_screen_clear()
                forest_room3a()
                return False

            elif choice == str(3):
                slow_print("You could almost swear there are... faces\n "
                           "in the bark of the trees. All of them looking\n "
                           "right at you as you walk through the forest.")
                slow_screen_clear()


def forest_room4b():

    slow_print("You come to a dead end in the path. The trees are\n "
               "too tightly packed to squeeze through.")

    while True:
        slow_print("You are at a dead end on this forest path.")
        os.system('clear')
        slow_print("\nWhat will you do?\n")
        slow_print("1. Back the way you came.")
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
                slow_print("You turn around and go back.")
                slow_screen_clear()
                forest_room3b()
                return False

            elif choice == str(2):
                if adventurer.room4bitem is False:
                    slow_print("You notice something just past "
                               "a gap in the trees.")
                    slow_print("You reach through and grab it.")
                    slow_print("You found a Steel Sword!")
                    adventurer.inventory.append("Steel Sword")
                    adventurer.room4bitem = True
                    slow_screen_clear()

                else:
                    slow_print("You aren't able to see much thanks "
                               "to how dark it is due to the trees.")
                    slow_screen_clear()


def forest_room4c():

    slow_print("The trees are growing much more closely together here, \n"
               "forcing you to squeeze through or turn around.")

    while True:
        slow_print("You are standing between densely packed trees.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Through the trees.")
        slow_print("2. Turn around.")
        slow_print("3. Look around.")
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
                slow_print("You squeeze yourself through "
                           "a gap in the trees.")
                slow_screen_clear()
                forest_room5c()
                return False

            elif choice == str(2):
                slow_print("You turn around and go back.")
                slow_screen_clear()
                forest_room3c()
                return False

            elif choice == str(3):
                if "Missing Necklace" in adventurer.quests and \
                 adventurer.necklace_found is False:
                    slow_print("You notice something shining in a hole "
                               "in one of the tree trunks. \nReaching "
                               "inside you grab hold of an old necklace.")
                    adventurer.necklace_found = True
                    slow_screen_clear()

                elif adventurer.necklace_found is True:
                    slow_print("You don't notice anything "
                               "else amoung the trees.")
                    slow_screen_clear()

                else:
                    slow_print("It's too difficult to take "
                               "notice of anything.")
                    slow_screen_clear()


def forest_room5a():

    slow_print("You step into an empty clearing.\n"
               "A breath of fresh air after the recent "
               "squeeze through\nthose tight trees.")

    while True:
        slow_print("You are standing in a small clearing.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Go North")
        slow_print("2. Go East.")
        slow_print("3. Go West.")
        slow_print("4. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4):
                raise Exception

        except Exception:
            print("Please enter only 1, 2, 3, or 4.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                slow_print("You head North.")
                slow_screen_clear()
                forest_room6a()
                return False

            elif choice == str(2):
                slow_print("You head East.")
                slow_screen_clear()
                forest_room5c()
                return False

            elif choice == str(3):
                slow_print("You head West.")
                slow_screen_clear()
                forest_room5b()
                return False

            elif choice == str(4):
                slow_print("You notice a small rabbit hopping "
                           "towards the western path.")
                slow_print("You hear a loud noise to the north.\n"
                           "Best to be prepared before you proceed.")
                slow_screen_clear()


def forest_room5b():
    slow_print("The air seems to glow as you step into a small clearing.\n"
               "It takes a moment but you realise that glow is actually\n"
               "dust sprinkling from a fairy's wings as it hovers above\n"
               "a small pool of water.")
    while True:
        slow_print("You are standing by a fairy's pool.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Go Back.")
        slow_print("2. Try to speak to the fairy.")
        slow_print("3. Try to catch the fairy.")
        slow_print("4. Drink from the pool.")
        slow_print("5. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4) \
             and choice != str(5):
                raise Exception

        except Exception:
            print("Please enter only 1, 2, 3, 4, or 5.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                slow_print("You turn around and leave the spring behind.")
                slow_screen_clear()
                forest_room5a()
                return False

            elif choice == str(2):
                slow_print("If she is capable of understanding you "
                           "or replying isn't clear.\n "
                           "Either way she gives no response.")
                slow_screen_clear()

            elif choice == str(3):
                slow_print("As you reach to try and grab the small fairy "
                           "a rush of dust suddenly\nflies into your face.\n"
                           "You wipe your eyes and when you can see again \n"
                           "you realise you are no "
                           "longer at the fairy's pool...")
                slow_screen_clear()
                forest_room3b()

            if choice == str(4):
                slow_print("The fairy regards you curiously "
                           "as you kneel down and\n"
                           "drink from the pool, but does nothing else.\n"
                           "The water instantly restores your vitality.")
                adventurer.recover_health(100)
                slow_print("The water has fully healed you!")
                slow_screen_clear()

            elif choice == str(5):
                slow_print("You look at the fairy. She is perhaps no\n"
                           "bigger than a hummingbird and is content to\n"
                           "simply watch you as you watch her.")
                slow_screen_clear()


def forest_room5c():

    enemy = random_enemy("Forest")
    random_battle(enemy, 3)
    if enemy.name == "Slime":
        adventurer.slimes_defeated += 1

    while True:
        slow_print("You step into a tiny clearing, \n"
                   "surrounded on all side by densely packed trees.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Go North")
        slow_print("2. Go West.")
        slow_print("3. Go South.")
        slow_print("4. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2) \
             and choice != str(3) and choice != str(4):
                raise Exception

        except Exception:
            print("Please enter only 1, 2, 3, or 4.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                slow_print("You head North.")
                slow_screen_clear()
                forest_room6c()
                return False

            elif choice == str(2):
                slow_print("You head West.")
                slow_screen_clear()
                forest_room5a()
                return False

            elif choice == str(3):
                slow_print("You head South.")
                slow_screen_clear()
                forest_room4c()
                return False

            elif choice == str(4):
                slow_print("You notice a path through "
                           "the trees to the north,\n "
                           "with some sounds of laughter echoing through.")
                slow_screen_clear()


def forest_room6a():
    slow_print("As you move through the trees you here an "
               "indescribable noise.\n Like something "
               "scracthing the very thoughts in your mind.")
    slow_print("A shadow bursts forth from between the trees!")
    spider = Enemy("Giant Spider", 50, 25, 10, 10, 150, 100)
    battle_event(adventurer, spider)

    slow_print("With the spider defeated you press onward"
               "past its twitching corpse.\n"
               "Delaying here would only be dangerous.\n"
               "A nest is likely nearby and you aren't "
               "equipped to deal with it.")
    slow_screen_clear()
    forest_room7()


def forest_room6c():
    if adventurer.forest_6c_camp is False:
        slow_print("You step out of the trees and into a clearing where\n"
                   "some bandits have set up a camp!")
        bandit_camp = Enemy("Bandits", 50, 25, 10, 10, 100, 50)
        battle_event(adventurer, bandit_camp)
        adventurer.forest_6c_camp = True
        if "Clear Bandit Camp" in adventurer.quests:
            slow_print("You have cleared the bandit camp!\n"
                       "Report your success in town!")
            adventurer.keyitems.append("Bandit Camp Cleared")

    else:
        slow_print("The camp is now silent, "
                   "save for the crackling of the dying fire.")

    while True:
        slow_print("You are standing at the center of the old bandit camp.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Go Back.")
        slow_print("2. Look around.")
        choice = int(input())
        try:
            if choice != 1 and choice != 2:
                raise Exception

        except Exception:
            print("Please enter only 1, or 2.\n")
            slow_screen_clear()

        else:
            if choice == 1:
                slow_print("You go back the way you came.")
                slow_screen_clear()
                forest_room5c()
                return False

            elif choice == 2:
                if "Missing Person" in adventurer.quests:
                    slow_print("As you look around you notice a "
                               "bundle of\nrags piled up with "
                               "some rope.\nTaking a closer look "
                               "you realise it is a person!\n"
                               "You cut them free, and give "
                               "them some supplies and "
                               "directions.\nThey are thankful "
                               "for the help and quickly run "
                               "from the forest back to town.")
                    adventurer.forest_kidnapped_person = True
                    slow_screen_clear()

                else:
                    slow_print("You notice some discarded rags.\n"
                               "You look through the bandit "
                               "supplies but find nothing of value.")
                    slow_screen_clear()


def forest_room7():
    while True:
        slow_print("You are sitting in a small "
                   "clearing at the end of the forest.")
        slow_print("\nWhat will you do?\n")
        slow_print("1. Leave")
        slow_print("3. Look around.")
        choice = input()
        try:
            if choice != str(1) and choice != str(2):
                raise Exception

        except Exception:
            print("Please enter only 1 or 2.\n")
            slow_screen_clear()

        else:
            if choice == str(1):
                slow_print("You depart from the forest,\n"
                           "heading toward the nearest town.")
                slow_screen_clear()
                move_to_town()
                return False

            elif choice == str(2):
                slow_print("The forest is eerily quiet here.\n"
                           "Perhaps the giant spiders had hunted\n"
                           "or scared all the other critters away.")
                slow_screen_clear()
