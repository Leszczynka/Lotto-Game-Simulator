from random import randint


class Lotto:
    def __init__(self, user_numbers: list):
        self.winning_numbers = []
        self.user_numbers = user_numbers

    def draw_numbers(self):
        while len(self.winning_numbers) < 6:
            number = randint(1, 49)
            if number not in self.winning_numbers:
                self.winning_numbers.append(number)

    def check_numbers(self):
        if len(set(self.winning_numbers) & set(self.user_numbers)) == len(self.winning_numbers):
            print("YOU WON!!!")
        else:
            print("Not this time")

    def __str__(self):
        return str(f"Your numbers: {self.user_numbers}\nLucky numbers: {self.winning_numbers}")


if __name__ == "__main__":
    my_numbers = [11, 22, 4, 6, 2, 14]

    l1 = Lotto(my_numbers)
    l1.draw_numbers()
    l1.check_numbers()
    print(l1)
