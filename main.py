import random


plays = 1
balance = input('Please Enter your starting balance: ')


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
    print(f'The winning number is {winning_number} and the winning color is {winning_color} in {plays} tries.')

    plays += 1
    return winning_number, winning_color


if __name__ == '__main__':
    winning_numbers = spins()
