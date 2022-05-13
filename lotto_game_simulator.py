from random import randint
from time import sleep


class Lotto:
    def __init__(self):
        self.winning_numbers = []
        self.user_numbers = []
        self.user_lucky_numbers = 0
        self.win_rate = {6: "I", 5: "II", 4: "III", 3: "IV"}

    def lucky_dip(self):
        while len(self.user_numbers) < 6:
            number = randint(1, 49)
            if number not in self.user_numbers:
                self.user_numbers.append(number)

    def take_numbers_from_user(self):
        while len(self.user_numbers) < 6:
            number = int(input("Type a number from 1 to 49: "))
            if number not in self.user_numbers:
                self.user_numbers.append(number)
        print(f"Your numbers are: {self.user_numbers}")

    def draw_numbers(self):
        while len(self.winning_numbers) < 6:
            number = randint(1, 49)
            if number not in self.winning_numbers:
                self.winning_numbers.append(number)

        for number in self.winning_numbers:
            sleep(2)
            print(number)

    def check_numbers(self):
        for number in self.user_numbers:
            if number in self.winning_numbers:
                self.user_lucky_numbers += 1
        if self.user_lucky_numbers == 0:
            print("No match this time")
        elif self.user_lucky_numbers == 6:
            print("Congratulations. The main award is yours!")
        else:
            print(f"You have successfully drawn only {self.user_lucky_numbers} numbers.")
            return self.user_lucky_numbers

    def win_rate_info(self):
        if self.user_lucky_numbers >= 3:
            print(f"Win rate is: {self.win_rate[self.user_lucky_numbers]}.")
        else:
            print("No award this time.")

    def __str__(self):
        return str(f"Your numbers: {self.user_numbers}\nLucky numbers: {self.winning_numbers}")

