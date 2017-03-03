import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_defensive_roll(self):
        dice_roll = random.randint(1, 12)
        return dice_roll * self.level

    def __repr__(self):
        return 'A Creature of type {} with level {}'.format(self.name, self.level)


class Wizard(Creature):
    def attack(self, creature):
        our_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()
        print('You roll {}. Your opponent rolls {}'.format(our_roll, creature_roll))
        return our_roll > creature_roll
