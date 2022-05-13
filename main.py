from lotto_game_simulator import Lotto
from time import sleep


class Main:
    print('''Welcome to Lotto!
Lotto is game of chance where you or a machine select numbers
and you win a prize if the numbers are picked in a random drawing.

Take your chances with a Lucky Dip to play randomly selected numbers
or click to enter your own 6 numbers.
''')
    draw = Lotto()

    def take_decision(self):
        print("Do you want to play randomly selected numbers? y/n? ")
        decision = input()

        if decision.lower() == "y":
            self.draw.lucky_dip()
            print(f"Your numbers: {self.draw.user_numbers}")

        else:
            self.draw.take_numbers_from_user()
            print(f"Your numbers: {self.draw.user_numbers}")

        sleep(3)
        print('''There are 49 sequentially placed balls in the cassette of the draw machine.
The drum of a drawing machine is empty...
the lock is released...
the drawing begins...
The drawn numbers are:''')

        sleep(6)
        self.draw.draw_numbers()
        self.draw.check_numbers()
        self.draw.win_rate_info()
        print(self.draw)


if __name__ == "__main__":
    main = Main()
    main.take_decision()
