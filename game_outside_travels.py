# This script was necessary to avoid cyclical
# imports between the road/forest and town
# when trying to and from either area.
import game_hubworld


def move_to_town():
    """
    This function is simply a helper function to travel
    to the town from either the road or forest.
    """
    game_hubworld.town()
