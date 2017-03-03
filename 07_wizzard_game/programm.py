import random

import time

from actors import Creature, Wizard


def main():
    actors = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 5),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandulf', 75)

    while True:

        actor = random.choice(actors)
        print('There appears {}'.format(actor))
        cmd = input('You can [a]ttack, [r]un away or [l]ook around:').lower()

        if cmd == 'a':
            if hero.attack(actor):
                actors.remove(actor)
                print('The Wizard slays {} and celebrates his victory'.format(actor.name))
            else:
                print('The {} of level {} defeats the hero, who must rest now'.format(actor.name, actor.level))
                time.sleep(5)
                print('The Wizard reappears revitalised')
        elif cmd == 'r':
            print('The Wizard runs away')
        elif cmd == 'l':
            print('The Wizard looks around and sees:')
            for a in actors:
                print('{}'.format(a))

        else:
            print('Sorry we do not understand {}'.format(cmd))
            break


if __name__ == '__main__':
    main()
