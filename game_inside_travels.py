# This script was necessary to avoid cyclical
# imports between the road/forest and town
# when trying to and from either area.
from game_road import road_start
from game_forest import forest_start


def move_to_road():
    """
    This function is simply a helper function to travel
    to the road from the town.
    """
    road_start()


def move_to_forest():
    """
    This function is simply a helper function to travel
    to the forest from the town.
    """
    forest_start()
