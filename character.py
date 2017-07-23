from random import shuffle

from ic_dice_tools import display_dice


class Character:
    def __init__(self):
        self.name = ""
        self.race = ""
        self.body = 0
        self.speed = 0
        self.mind = 0
        self.will = 0
        self.careers = {}
        self.skills = {}
        self.gifts = {}
        self.flaws = {}

    def __repr__(self):
        trait = '{0}: {1:<5}'
        traits = '{0} -- {1} -- {2} -- {3}'.format(
            trait.format("Body", display_dice(self.body)),
            trait.format("Speed", display_dice(self.speed)),
            trait.format("Mind", display_dice(self.mind)),
            trait.format("Will", display_dice(self.will)))
        return '{0.name:<10}  {0.race:<10} [{1}]'.format(self, traits)

    @staticmethod
    def generate_character(race_list, dice_list):
        shuffle(dice_list)
        shuffle(race_list)
        d = iter(dice_list)
        character = Character()
        character.body = next(d)
        character.speed = next(d)
        character.mind = next(d)
        character.will = next(d)
        character.race = race_list[0]
        return character
