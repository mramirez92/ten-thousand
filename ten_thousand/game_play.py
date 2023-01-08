from textwrap import dedent
import sys

from game_logic import GameLogic
import re


class Game:
    def __init__(self):
        self.current_roll = ()
        self.dice_kept = []
        self.dice_string = ""
        self.rounds = 1
        self.num_dice = 6
        self.round_score = 0
        self.total_score = 0

    def roll(self, roller=None):
        print(f"Rolling {self.num_dice} dice...")
        self.current_roll = roller or GameLogic.roll_dice(self.num_dice)
        self.dice_string = "*** {} ***".format(" ".join(str(num) for num in self.current_roll))
        print(self.dice_string)

    def zilch(self):
        print(dedent("""\
        ****************************************
        **       Zilch!!! Round over          **
        ****************************************
        """))
        self.round_reset()

    def dice_strigify(self, tupple):
        return "*** {} ***".format(" ".join(str(num) for num in tupple))

    def cheater(self):
        print("Cheater!!! Or possibly made a typo...")
        current_roll = self.dice_strigify(self.current_roll)
        print(current_roll)

    def initialized_game(self):
        print("Welcome to Dice 100000")
        print("(y)es to play or (n)o to decline")
        user_response = input("> ").lower()

        if user_response == "y":
            self.play_round()
        else:
            print("OK. Maybe another time")

    def round_reset(self):
        self.total_score += self.round_score
        print(f"You banked {self.round_score} in round {self.rounds}\nTotal score is {self.total_score} points")
        self.round_score = 0
        self.rounds += 1
        self.num_dice = 6

    def play_round(self):
        playing = True
        while playing:
            print(f"Starting Round {self.rounds}")
            same_round = True
            while same_round:
                self.roll()
                if GameLogic.calculate_score(tuple(self.current_roll)) == 0:
                    print(dedent("""\
                    ****************************************
                    **       Zilch!!! Round over          **
                    ****************************************
                    """))
                    self.round_score = 0
                    self.round_reset()
                    break

                # validation of kept dice, returns validated kept dice list
                self.keeper_input(self.current_roll)
                self.num_dice -= len(self.dice_kept)
                if self.num_dice == 0:
                    self.num_dice = 6
                current_score = GameLogic.calculate_score(tuple(self.current_roll))
                # self.round_score
                self.round_score += current_score
                print(f"You have {self.round_score} unbanked points and {self.num_dice} dice remaining")
                next_play = input("(r)oll again, (b)ank your points or (q)uit:\n>").lower()

                if next_play == "r":
                    continue
                elif next_play == "b":
                    self.round_reset()
                    break
                elif next_play == "q":
                    print(f"Thanks for playing. You earned {self.total_score} points.")
                    exit(0)

    def keeper_input(self, current_roll):
        while True:
            keep_input = input("Enter dice to keep, or (q)uit:\n >")
            if keep_input == "q":
                break
            self.dice_kept = [int(keeper) for keeper in re.sub(r'[^0-9]', '', keep_input)]

            if GameLogic.validate_keepers(self.current_roll, self.dice_kept):
                return self.dice_kept
            else:
                self.cheater()

        print(f"Thanks for playing. You earned {self.total_score} points.")
        exit(0)


if __name__ == "__main__":
    game = Game()
    game.initialized_game()
