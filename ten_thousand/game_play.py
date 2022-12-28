from game_logic import *

print("Welcome to Ten Thousand")


def game_play(roll=GameLogic):
    while True:
        print("(y)es to play or (n)o to decline")
        answer = input("> ").lower()

        if answer == "n":
            print("bye")
            break
        else:
            roll = GameLogic()


game_play()
