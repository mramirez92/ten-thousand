from random import randint
from collections import Counter


class GameLogic:
    def __init__(self, num_dice=6):
        self.num_dice = num_dice
        self.total_score = 0
        self.round_score = 0
        self.current_round = 1

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

    def initialized_game(self):
        print("""
    Welcome to Dice 100000
    (y)es to play or (n)o to decline
            """)
        user_response = input("> ").lower()

        if user_response == "y":
            self.play()
        else:
            print("OK. Maybe another time")

    def play(self, roller=None):

        roll = roller or self.roll_dice(self.num_dice)
        print("*** {} ***".format(" ".join(str(num) for num in roll)))

        valid_input = ['1', '2', '3', '4', '5', '6']
        keep_input = input("Enter dice to keep, or (q)uit:")
        if keep_input == "q":
            print(f"Thanks for playing. You earned {self.total_score} points.")
            return
        else:
            self.keeper(keep_input)

    def keeper(self, keep_input):

        dice_kept = []
        current_score = []
        if " " in keep_input:
            dice_kept = [int(num) for num in keep_input.replace(" ", "")]
        else:
            dice_kept = [int(keeper) for keeper in keep_input]

        # for keeper in keep_input:
        #     dice_kept.append(int(keeper))
        self.total_score = self.calculate_score(tuple(dice_kept))

        # Calculate the score for the round
        print("You have {} unbanked points and {} dice remaining".
              format(self.total_score, self.num_dice - len(dice_kept)))
        print("(r)oll again, (b)ank your points or (q)uit:")
        next_play = input("> ").lower()

        if next_play == "q":
            self.quit()

    def quit(self):
        print(f"Thanks for playing. You earned {self.total_score} points.")
        return


if __name__ == "__main__":
    play_game = GameLogic()
    play_game.initialized_game()
