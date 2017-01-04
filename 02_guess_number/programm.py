import random

print('-------------------------------------------------')
print('               GUESS THAT NUMBER GAME')
print('-------------------------------------------------')
print('')

the_number=random.randint(0,100)

guess_number=-1

while guess_number != the_number:

    guess_text=input("Guess a number between 0 and 100: ")
    guess_number=int(guess_text)

    if guess_number < the_number:
        print('Your guess of {} was to LOW'.format(guess_number))
    elif guess_number > the_number:
        print('Your guess of {} was to HIGH'.format(guess_number))
    else:
        print('You WIN, the number was {}'.format(guess_number))


