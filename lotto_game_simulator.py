from random import randint


class Lotto:
    def __init__(self):
        self.winning_numbers = []
        self.user_numbers = []
        self.user_lucky_numbers = 0
        self.winning_rate = {6: "I", 5: "II", 4: "III", 3: "IV"}

    def get_lucky_dip(self):
        while len(self.user_numbers) < 6:
            number = randint(1, 49)
            if number not in self.user_numbers:
                self.user_numbers.append(number)

    def take_numbers_from_user(self):
        while len(self.user_numbers) < 6:
            number = int(input("Type a number from 1 to 49: "))
            if number == 0 or number > 49:
                print("You can't select this number.")
            if number not in self.user_numbers and 1 <= number <= 49:
                self.user_numbers.append(number)

    def draw_numbers(self):
        while len(self.winning_numbers) < 6:
            number = randint(1, 49)
            if number not in self.winning_numbers:
                self.winning_numbers.append(number)

    def check_numbers(self):
        for number in self.user_numbers:
            if number in self.winning_numbers:
                self.user_lucky_numbers += 1

    def show_game_result_info(self):
        if self.user_lucky_numbers == 0:
            print("None of your numbers were lucky.")
        elif self.user_lucky_numbers in [1, 2]:
            print(f"{self.user_lucky_numbers} of your numbers were lucky!")
        if self.user_lucky_numbers >= 3:
            print(f"{self.user_lucky_numbers} of your numbers were lucky! Wining rate is: {self.winning_rate[self.user_lucky_numbers]}.")

    def __str__(self):
        return str(f"Your numbers: {self.user_numbers}\nLucky numbers: {self.winning_numbers}")
