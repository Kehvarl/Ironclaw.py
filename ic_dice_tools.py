dice_progression = ["d4", "d6", "d8", "d10", "d12"]


def display_dice(val):
    """
    Converts a die-level into a more friendly dice-pool
    :param int val: The die-level to display
    :return str: pretty-printed dice value (eg: d4)
    """
    d = ""
    while val > 5:
        val -= 5
        d += "d12 "
    if val > 0:
        d += dice_progression[val - 1]
    return d
