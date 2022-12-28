from random import randint
from collections import Counter


class GameLogic:

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
                score += n_of_kind[dice_num]*2
            else:
                score += 0

        return score
