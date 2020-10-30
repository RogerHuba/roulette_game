import random
import sys
from os import system

balance = 0
plays = 0
player_choice = ''


def spins():
    global plays
    slots = {'00': 'green', '0': 'green', '1': 'red', '2': 'black',
             '3': 'red', '4': 'black', '5': 'red', '6': 'black', '7': 'red',
             '8': 'black', '9': 'red', '10': 'black', '11': 'red',
             '12': 'black', '13': 'red', '14': 'black', '15': 'red',
             '16': 'black', '17': 'red', '18': 'black', '19': 'red',
             '20': 'black', '21': 'red', '22': 'black', '23': 'red',
             '24': 'black', '25': 'red', '26': 'black', '27': 'red',
             '28': 'black', '29': 'red', '30': 'black', '31': 'red',
             '32': 'black', '33': 'red', '34': 'black', '35': 'red',
             '36': 'black'}

    winning_number = int(random.choice(list(slots.keys())))
    winning_color = slots[str(winning_number)]

    plays += 1
    return winning_number, winning_color


def menu():
    print(f'''
    Your current balance is {balance}.
    You have played {plays} time(s).
    
    1) Enter Account Balance
    2) Place a bet
    3) Play
    q) Quit
    ''')
    menu_choice = input('What would you like to do? ')
    return menu_choice


if __name__ == '__main__':
    system('clear')
    while not player_choice:
        player_choice = menu()
        if not player_choice:
            player_choice = menu()
        elif player_choice == 'q':
            print('Thank you for playing!')
            sys.exit()
        elif int(player_choice) is 1:
            balance = input('Please Enter your starting balance: ')
            player_choice = ''
        elif int(player_choice) is 2:
            pass
            player_choice = ''
        elif int(player_choice) is 3:
            winning_return = spins()
            win_number = winning_return[0]
            win_color = winning_return[1]
            print(f'The winning number is {win_number} and the winning color is {win_color} in {plays} tries.')
            player_choice = ''


