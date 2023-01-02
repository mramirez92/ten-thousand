from random import randint
from collections import Counter
import re


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
        # {1:1, 2:1, 3:1, 4:1, 5:1, 6:1} len == 6 -> straight -> returns 1500

        counter_dice = Counter(roll)

        # straight
        if len(counter_dice) == 6:
            return 1500

        # triple double

        if len(counter_dice) == 3 and all(value == 2 for value in counter_dice.values()):
            return 1500

        for dice_num, counts in counter_dice.items():
            if dice_num == 5 and counts <= 2:
                score += 50 * counts
            elif dice_num == 1 and counts <= 2:
                score += 100 * counts
            elif counts == 3:
                score += n_of_kind[dice_num]
            elif counts == 4:
                score += n_of_kind[dice_num] * 2
            elif counts == 5:
                score += n_of_kind[dice_num] * 3
            elif counts == 6:
                score += n_of_kind[dice_num] * 4


        return score

    @staticmethod
    def validate_keepers(dice_roll, dice_kept):
        dice_roll_validation = Counter(dice_roll)
        dice_kept_validation = Counter(dice_kept)

        if len(dice_kept_validation) <= len(dice_roll_validation):
            if all(dice_kept_validation[key] <= dice_roll_validation[key] for key in dice_kept_validation.keys()):
                return True
            return False
        else:
            return False


