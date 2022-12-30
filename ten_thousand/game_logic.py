from random import randint
from collections import Counter
import re


class GameLogic:
    def __init__(self, num_dice=6):
        self.current_roll = ()
        self.round = 1
        self.num_dice = num_dice
        self.current_play_score = 0
        self.round_score = 0
        self.total_score = 0
        self.dice_kept = []

    # kind of its own thing, static method has input and has outputs, just needs a place to live
    # returns tuple of random integers, between 1 and 6

    @staticmethod
    def roll_dice(num_dice):
        return tuple(randint(1, 6) for _ in range(0, num_dice))

    @staticmethod
    def calculate_score(roll):

        n_of_kind = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}

        score = 0

        # counter returns value pair ex ({5: 1})

        counter_dice = Counter(roll)

        for dice_num, counts in counter_dice.items():
            if dice_num == 5 and counts <= 2:
                score += 50 * counts
            elif dice_num == 1 and counts <= 2:
                score += 100 * counts
            elif counts == 3:
                score += n_of_kind[dice_num]
            elif counts == 4:
                score += n_of_kind[dice_num] * 2
            else:
                score += 0

        return score

    def round_start_msg(self):
        print(f"Starting Round {self.round}")
        print("Rolling 6 dice...")

    def initialized_game(self):
        print("Welcome to Dice 100000")
        print("(y)es to play or (n)o to decline")
        user_response = input("> ").lower()

        if user_response == "y":
            self.round_start_msg()
            self.roll()
        else:
            print("OK. Maybe another time")

    def roll(self, roller=None):
        self.current_roll = roller or self.roll_dice(self.num_dice)
        print("*** {} ***".format(" ".join(str(num) for num in self.current_roll)))

        keep_input = input("Enter dice to keep, or (q)uit:")
        if keep_input == "q":
            self.quit()

        self.dice_kept = [int(keeper) for keeper in re.sub(r'[^0-9]', '', keep_input)]

        while True:
            if all(nums in self.current_roll for nums in self.dice_kept):
                break
            else:
                print("Cheater!!!")
                print("Or possibly made a typo...")
                print("*** {} ***".format(" ".join(str(num) for num in self.current_roll)))
                keep_input = input("Enter dice to keep, or (q)uit:")

        self.keeper(keep_input)

    # def validate_input(self, roll, keepers):
    #             roll_count = Counter(self.current_roll)
    #             dice_count = Counter(self.dice_kept)
    #
    #             for number, count in dice_count.items():
    #                 if number not in roll_count:
    #                     return False
    #                 elif count > roll_count[number]:
    #                  return False
    #             return True

    def keeper(self, keep_input):

        self.dice_kept = [int(keeper) for keeper in re.sub(r'[^0-9]', '', keep_input)]

        # Calculate the score for the round
        self.current_play_score = self.calculate_score(tuple(self.dice_kept))
        self.round_score += self.current_play_score

        if self.current_play_score == 0:
            self.zilch()
        else:
            print("You have {} unbanked points and {} dice remaining".
                  format(self.round_score, self.num_dice - len(self.dice_kept)))
            print("(r)oll again, (b)ank your points or (q)uit:")
            next_play = input("> ").lower()
            self.valid_next_move(next_play)

    def zilch(self):
        print("You zilched!")
        self.round += 1
        print(f"Your total score is {self.total_score} points.")
        self.round_start_msg()
        self.roll()

    def bank(self):
        # add total round score to total score
        self.total_score += self.round_score
        print(f"You banked {self.round_score} in round {self.round}")
        self.round += 1
        self.round_score = 0
        print(f"Total score is {self.total_score} points")
        self.round_start_msg()
        self.roll()

    def quit(self):
        print(f"Thanks for playing. You earned {self.total_score} points.")
        return

    def valid_next_move(self, next_play):

        while next_play not in ["r", "b", "q"]:
            print("invalid input")
            print("(r)oll again, (b)ank your points or (q)uit:")
            next_play = input("> ").lower()

        if next_play == "q":
            self.quit()
        elif next_play == "b":
            self.bank()
        elif next_play == "r":
            self.roll()


if __name__ == "__main__":
    play_game = GameLogic()
    play_game.initialized_game()
