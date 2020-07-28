import time
import random


def print_pause(messages):
    print(messages)
    time.sleep(2)


def introduction(item, barrier):
    print_pause('Welcome to your adventure game!')
    print_pause('You find yourself standing in a crossroads.')
    print_pause("You don't know where you are"
                " and it is getting dangerous here.")
    print_pause('Your goal is to find a way to go home safely.')


def left(item, barrier):
    print_pause('\nThe road comes to dead end')
    if 'gun' in item:
        print_pause('There is nothing here!')
    else:
        print_pause('But... You have found a gun here.')
        print_pause('What would you do now?')
        while True:
            choice2 = \
                input('Enter 1 to put the gun in your bag'
                      ' and enter 2 to ignore it: ')
            if choice2 == '1':
                item.append('gun')
                print_pause('\nThe gun becomes your defense weapon now.')
                break
            elif choice2 == '2':
                print_pause("\nIt is a dangerous weapon, you don't like it.")
                break
    print_pause('\nNow we have to go back the crossroads.')
    print_pause('One again...')
    crossroads(item, barrier)


def right(item, barrier):
    print_pause("\nYou've been here before, this is the way to go home.")
    print_pause('Suddenly, ' + barrier + ' appears.')
    while True:
        choice2 = \
            input('Enter 1 if you want to fight'
                  ' and enter 2 if you want to run away: ')
        if choice2 == '1':
            if 'gun' in item:
                print_pause('\nYou quickly shot ' + barrier
                            + ' with your gun.')
                print_pause('He is injured and runs away!')
                print_pause('You are safe now.')
                print_pause('Congratulatons!')
            else:
                print_pause('\nYou are so brave,'
                            ' but it should be a the wrong option this time.')
                print_pause('Game over!!!')
            play_again()
            break
        if choice2 == '2':
            print_pause('\nYou now in the crossroads.')
            print_pause('One again...')
            crossroads(item, barrier)
            break


def crossroads(item, barrier):
    print_pause('\nYou need to make a choice: ')
    while True:
        choice = \
            input('Please enter 1 to turn right'
                  ' and enter 2 to turn left: ')
        if choice == '1':
            right(item, barrier)
            break
        elif choice == '2':
            left(item, barrier)
            break
        else:
            print_pause('Please input again: ')
    return choice


def play_again():
    again = input('\nDo you want to play again?'
                  ' Enter yes or no. ').lower()
    if again == 'yes':
        print_pause("Let's play again.\n")
        main()
    elif again == 'no':
        print_pause('Thank you, Bye!')
    else:
        play_again()


def main():
    item = []
    barrier = random.choice(['a monster', 'a dragon', 'a thief'])
    introduction(item, barrier)
    crossroads(item, barrier)


if __name__ == "__main__":
    main()
