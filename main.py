import random
import sys
from os import system

balance, plays, red_bet_amount, green_bet_amount, black_bet_amount, odd_bet_amount, even_bet_amount, number_bet_amount \
    = 0, 0, 0, 0, 0, 0, 0, 0
bet_red, bet_black, bet_green, bet_odd, bet_even = False, False, False, False, False
bet_number, money_on_number, last_numbers, last_colors = [], [], [], []
player_choice = ''
message = 'Lets Play Roulette'
max_bet = 500
total_bet = 0


def screen_clear():
    system('clear')
    return


def spins():
    global plays
    slots = {'00': 'green', '0': 'green', '1': 'red', '2': 'black', '3': 'red',
             '4': 'black', '5': 'red', '6': 'black', '7': 'red', '8': 'black',
             '9': 'red', '10': 'black', '11': 'red', '12': 'black', '13': 'red',
             '14': 'black', '15': 'red', '16': 'black', '17': 'red', '18': 'black',
             '19': 'red', '20': 'black', '21': 'red', '22': 'black', '23': 'red',
             '24': 'black', '25': 'red', '26': 'black', '27': 'red', '28': 'black',
             '29': 'red', '30': 'black', '31': 'red', '32': 'black', '33': 'red',
             '34': 'black', '35': 'red', '36': 'black'}

    winning_number = int(random.choice(list(slots.keys())))
    winning_color = slots[str(winning_number)]
    last_numbers.append(winning_number)
    last_colors.append(winning_color)
    if winning_number %2 == 0:
        winning_odd_even = 'even'
    else:
        winning_odd_even = 'odd'
    plays += 1
    return winning_number, winning_color, winning_odd_even


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
    return


def print_screen():
    print(f'''
    Your current balance is {balance}.
    Your current bet is {total_bet}.
    You have played {plays} time(s).
    Current Red: {bet_red} | Current Black: {bet_black} | Current Green: {bet_green}
    Current Odd: {bet_odd} | Current Even: {bet_even}
    Current Numbers: {bet_number}
    Last 10 Numbers: {last_numbers}
    Last 10 Colors: {last_colors}
    MESSAGE: {message}
    ''')
    return


def place_bet():
    global bet_red, bet_black, bet_odd, bet_even, bet_green, message, red_bet_amount, balance, total_bet, \
        black_bet_amount, green_bet_amount, odd_bet_amount, even_bet_amount, number_bet_amount
    bet = ''
    while bet != 'q':
        screen_clear()
        print_screen()
        # TODO: Need to fix the display to add color
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
        # TODO: This Code below can be made DRY!
        elif int(bet) == 1:
            if bet_red:
                bet_red = False
                balance = int(balance) + int(red_bet_amount)
                total_bet = total_bet - int(red_bet_amount)
                red_bet_amount = 0
            else:
                red_bet_amount = input('Please enter an amount to bet on RED: ')
                if int(red_bet_amount) > int(balance):
                    message = 'BET NOT PLACED! Balance to low.'
                elif (int(red_bet_amount) + int(total_bet)) > max_bet:
                    message = 'BET NOT PLACED! Exceeded Max bet'
                else:
                    total_bet += int(red_bet_amount)
                    balance = int(balance) - int(red_bet_amount)
                    bet_red = True
                    message = 'Bet placed on RED'
        elif int(bet) == 2:
            if bet_black:
                bet_black = False
                balance = int(balance) + int(black_bet_amount)
                total_bet = total_bet - int(black_bet_amount)
                black_bet_amount = 0
            else:
                black_bet_amount = input('Please enter an amount to bet on BLACK: ')
                if int(black_bet_amount) > int(balance):
                    message = 'BET NOT PLACED! Balance to low.'
                elif (int(black_bet_amount) + int(total_bet)) > max_bet:
                    message = 'BET NOT PLACED! Exceeded Max bet'
                else:
                    total_bet += int(black_bet_amount)
                    balance = int(balance) - int(black_bet_amount)
                    bet_black = True
                    message = 'Bet placed on BLACK'
        elif int(bet) == 3:
            if bet_green:
                bet_green = False
                balance = int(balance) + int(green_bet_amount)
                total_bet = total_bet - int(green_bet_amount)
                green_bet_amount = 0
            else:
                green_bet_amount = input('Please enter an amount to bet on GREEN: ')
                if int(green_bet_amount) > int(balance):
                    message = 'BET NOT PLACED! Balance to low.'
                elif (int(green_bet_amount) + int(total_bet)) > max_bet:
                    message = 'BET NOT PLACED! Exceeded Max bet'
                else:
                    total_bet += int(green_bet_amount)
                    balance = int(balance) - int(green_bet_amount)
                    bet_black = True
                    message = 'Bet placed on GREEN'
        elif int(bet) == 4:
            if bet_odd:
                bet_odd = False
                balance = int(balance) + int(odd_bet_amount)
                total_bet = total_bet - int(odd_bet_amount)
                odd_bet_amount = 0
            else:
                odd_bet_amount = input('Please enter an amount to bet on ODD: ')
                if int(odd_bet_amount) > int(balance):
                    message = 'BET NOT PLACED! Balance to low.'
                elif (int(odd_bet_amount) + int(total_bet)) > max_bet:
                    message = 'BET NOT PLACED! Exceeded Max bet'
                else:
                    total_bet += int(odd_bet_amount)
                    balance = int(balance) - int(odd_bet_amount)
                    bet_odd = True
                    message = 'Bet placed on ODD'
        elif int(bet) == 5:
            if bet_even:
                bet_even = False
                balance = int(balance) + int(even_bet_amount)
                total_bet = total_bet - int(even_bet_amount)
                even_bet_amount = 0
            else:
                even_bet_amount = input('Please enter an amount to bet on EVEN: ')
                if int(even_bet_amount) > int(balance):
                    message = 'BET NOT PLACED! Balance to low.'
                elif (int(even_bet_amount) + int(total_bet)) > max_bet:
                    message = 'BET NOT PLACED! Exceeded Max bet'
                else:
                    total_bet += int(even_bet_amount)
                    balance = int(balance) - int(even_bet_amount)
                    bet_even = True
                    message = 'Bet placed on EVEN'
        elif int(bet) == 6:
            number_to_add = int(input('Enter a number 1-36: '))
            while 1 > number_to_add > 36:
                number_to_add = input(int('Enter a number 1-36: '))
            if number_to_add in bet_number:
                bet_number.remove(number_to_add)
            else:
                number_bet_amount = input(f'Please enter an amount to bet on {number_to_add}: ')
                if int(number_bet_amount) > int(balance):
                    message = 'BET NOT PLACED! Balance to low.'
                elif (int(number_bet_amount) + int(total_bet)) > max_bet:
                    message = 'BET NOT PLACED! Exceeded Max bet'
                else:
                    total_bet += int(number_bet_amount)
                    balance = int(balance) - int(number_bet_amount)
                    message = f'Bet placed on {number_to_add}!'
        elif int(bet) == 7:
            message = 'Group betting not yet implemented!'
        else:
            message = 'Something is Wrong!'
    return


def play_game():
    global last_colors, balance, red_bet_amount, total_bet, bet_red, bet_black, bet_green, bet_odd, \
        bet_even, black_bet_amount, odd_bet_amount, even_bet_amount, message
    message = ''
    winning_return = spins()
    win_number, win_color, odd_even = winning_return[0], winning_return[1], winning_return[2]
    print('Win Color is: ' + win_color)
    # TODO: May need to do a check on the bet and then drill down
    # TODO: This function is doing to much.  Make a function for changing balances.
    if win_color is 'red' and bet_red:
        balance = int(balance) + (int(red_bet_amount) * 2)
        message = 'You won on RED '
    if win_color is 'black' and bet_black:
        balance = int(balance) + (int(black_bet_amount) * 2)
        message += 'You won on BLACK'
    if odd_even is 'even' and bet_even:
        balance = int(balance) + (int(even_bet_amount) * 2)
        message += 'You won on EVEN'
    if odd_even is 'odd' and bet_odd:
        balance = int(balance) + (int(odd_bet_amount) * 2)
        message += 'You won on ODD'
    if win_number in bet_number:
        balance = int(balance) + (int(number_bet_amount) * 35)
    # TODO: Add these individually to each win condition.
    red_bet_amount, black_bet_amount, odd_bet_amount, even_bet_amount, total_bet = 0, 0, 0, 0, 0
    bet_red, bet_black, bet_green, bet_odd, bet_even = False, False, False, False, False
    return


if __name__ == '__main__':
    screen_clear()
    # TODO: This can be cleaned up a little!
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
