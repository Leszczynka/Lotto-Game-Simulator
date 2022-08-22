from random import sample
from time import sleep


def choice_game_option():
    game_options = ['own numbers', 'lucky dip']
    for index, option in enumerate(game_options):
        print(f'{index} - {option}')
    user_input = int(input('What option would you like to play? '))
    return user_input


def draw_numbers():
    lucky_numbers = sample(range(1, 50), 6)
    return lucky_numbers


def take_users_numbers():
    user_numbers = []
    while len(user_numbers) < 6:
        number = int(input("Enter a number from 1 to 49: "))
        if number < 1 or number > 49:
            print('Number must be an integer from 1 to 49')
            continue
        if number in user_numbers:
            print('You are already enter this number')
            continue
        user_numbers.append(number)
    return user_numbers


def check_result(user_numbers, lucky_numbers):
    user_lucky_numbers = 0
    for number in user_numbers:
        if number in lucky_numbers:
            user_lucky_numbers += 1
    return user_lucky_numbers


def calculate_winning_rate(user_lucky_numbers):
    print(f'{user_lucky_numbers} of your numbers was/were lucky.')
    if user_lucky_numbers < 3:
        return f'Unfortunately, no prize this time.'
    elif 3 <= user_lucky_numbers <= 5:
        return f'Congratulations, you win the {user_lucky_numbers} level prize'
    return f'CONGRATULATIONS!!! You win the grand prize!'


def play():
    print('Welcome to Lotto! '
          'Lotto is game where you or a machine select numbers and you have a chance to win a prize if your numbers are'
          'picked in a random drawing.\nTake your chances with a Lucky Dip to play randomly selected numbers '
          'or choose your own 6 numbers.')

    user_choice = choice_game_option()
    if user_choice == 0:
        user_numbers = take_users_numbers()
    else:
        user_numbers = draw_numbers()
    print(f'User numbers: {user_numbers}')
    sleep(3)
    print('There are 49 sequentially placed balls in the cassette of the draw machine.\n'
          'The drum of a drawing machine is empty...\n'
          'the lock is released...\n'
          'the drawing begins...\n'
          'The drawn numbers are:')
    lucky_numbers = draw_numbers()
    for number in lucky_numbers:
        sleep(1)
        print(number)

    print('We are checking result... Please wait...')
    sleep(3)
    result = check_result(user_numbers, lucky_numbers)
    winning_rate_info = calculate_winning_rate(result)
    print(f'\n---{winning_rate_info}---\n')


if __name__ == "__main__":
    play()
