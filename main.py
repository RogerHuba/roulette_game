import random
import sys
from os import system

balance, plays = 0, 0
bet_red, bet_black, bet_green, bet_odd, bet_even = False, False, False, False, False
bet_number, last_numbers, last_colors = [], [], []
player_choice = ''
message = 'Lets Play Roulette'
max_bet = 500


def screen_clear():
    system('clear')


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
    screen_clear()
    print_screen()
    print(f'''
    
    1) Enter Account Balance
    2) Place a bet
    3) Play
    q) Quit
    ''')
    menu_choice = input('What would you like to do? ')
    return menu_choice


def quit_game():
    print('Thank you for playing!')
    sys.exit()


def adjust_balance():
    global balance
    balance = input('Please Enter your starting balance: ')


def print_screen():
    print(f'''
    Your current balance is {balance}.
    You have played {plays} time(s).
    Current Red: {bet_red} | Current Black: {bet_black} | Current Green: {bet_green}
    Current Odd: {bet_odd} | Current Even: {bet_even}
    Current Numbers: {bet_number}
    Last 10 Numbers: {last_numbers}
    MESSAGE: {message}
    ''')
    return


def place_bet():

    global bet_red, bet_black, bet_odd, bet_even, bet_green, message
    bet = ''
    while bet != 'q':
        screen_clear()
        print_screen()
        print(f'''
        1) Red  2) Black  3) Green
        4) Odd  5) Even
        6) Specific Number
        7) Number Groups Not Implemented
        q) Done Betting!
        ''')
        bet = input('Place your bet, 1-5: ')
        if bet == 'q':
            return
        elif int(bet) == 1:
            if bet_red:
                bet_red = False
            else:
                bet_red = True
        elif int(bet) == 2:
            pass
        elif int(bet) == 3:
            pass
        elif int(bet) == 4:
            pass
        elif int(bet) == 5:
            pass
        elif int(bet) == 6:
            pass
        elif int(bet) == 7:
            message = 'Group betting not yet implemented!'


def play_game():
    global last_colors, last_numbers
    winning_return = spins()
    win_number = winning_return[0]
    win_color = winning_return[1]
    print(f'The winning number is {win_number} and the winning color is {win_color} in {plays} tries.')


if __name__ == '__main__':
    screen_clear()
    while not player_choice:
        player_choice = menu()
        if not player_choice:
            player_choice = menu()
        elif player_choice == 'q':
            quit_game()
        elif int(player_choice) == 1:
            adjust_balance()
            player_choice = ''
        elif int(player_choice) == 2:
            place_bet()
            player_choice = ''
        elif int(player_choice) == 3:
            play_game()
            player_choice = ''


