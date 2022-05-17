from lotto_game_simulator import Lotto
from time import sleep


class Main:
    print('''Welcome to Lotto!
Lotto is game where you or a machine select numbers
and you have a chance to win a prize if your numbers are picked in a random drawing.

Take your chances with a Lucky Dip to play randomly selected numbers
or choose your own 6 numbers.
''')
    draw = Lotto()

    def play_the_lotto_game(self):
        print("Do you want to play randomly selected numbers? y/n? ")
        decision = input()

        if decision.lower() == "y":
            self.draw.get_lucky_dip()
            print(f"Your numbers are: {self.draw.user_numbers}")
        else:
            self.draw.take_numbers_from_user()
            print(f"Your numbers are: {self.draw.user_numbers}")

        print('''There are 49 sequentially placed balls in the cassette of the draw machine.
The drum of a drawing machine is empty...the lock is released...the drawing begins...
The drawn numbers are:''')

        sleep(4)
        self.draw.draw_numbers()
        for number in self.draw.winning_numbers:
            print(number)
            sleep(2)
        self.draw.check_numbers()
        self.draw.show_game_result_info()
        print(self.draw)


if __name__ == "__main__":
    main = Main()
    main.play_the_lotto_game()

