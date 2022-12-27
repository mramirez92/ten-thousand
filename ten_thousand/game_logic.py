from random import randint


class GameLogic:

    # kind of its own thing, static method has input and has outputs, just needs a place to live
    # returns tuple of random integers, between 1 and 6
    @staticmethod
    def roll_dice(num_dice):
        return tuple(randint(1, 6) for _ in range(0, num_dice))
