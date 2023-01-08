# breaking down code 
`Welcome to Ten Thousand
(y)es to play or (n)o to decline
> y` 

- Takes in no arguments
- invite to play() -> y or n, or True/False
  - if n then decline_game() "okay, maybe another time"
  - else start_game()

def start_game():
- total_score = 0
- loop for round_num in given num of rounds
  - round_score = do_round(round_num, func_to_roll)
  - if round_score was a a quit = 1, end game
      - return
  - complete_round( round_num, total_round, round_score) show round stats
    - "You banked 500 points in round 1, Total score is 500 points"
- end_game(total_score), exits loop 
What must we do in the begginning and end, and in betwwen?
`Starting round 1` 
    - start_round(round_num, function_to_roll_dice) -> return round_score or quit

Rolling 6 dice...
*** 2 3 1 3 4 2 ***
Enter dice to keep, or (q)uit:
> 1
You have 100 unbanked points and 5 dice remaining
(r)oll again, (b)ank your points or (q)uit:
> r
Rolling 5 dice...
*** 4 2 4 4 6 ***
Enter dice to keep, or (q)uit:
> 444
You have 500 unbanked points and 2 dice remaining
(r)oll again, (b)ank your points or (q)uit:
> b
You banked 500 points in round 1
Total score is 500 points
Starting round 2
Rolling 6 dice...
*** 3 2 3 2 1 4 ***
Enter dice to keep, or (q)uit:
> q
Thanks for playing. You earned 500 points
> 

```python
accepted = invte_to_play()
if not accepted:
    decline_game()
else:
    start_game(rounds, roll_dice)
    
def decline_game():
    print("bye")
    
def invite_to_play(num_rounds):
    print("Welcome to Ten Thousand
    (y)es to play or (n)o to decline")
    choice =input(">")
    return choice =="y"

def start_game(rounds, roll_dice):
  total_score = 0
  for num_round in range(1,rounds+1):
    round_score = do_round(round_num,roll_dice)
      
      if round_score == -1:
        break
        
        total_score += round_score
        
        complete_round(round_num, total_score, round_score)
          
    end_game(total_score)
        

def do_round(round_num, roll_dice):
  """
  rouond num: int
  rolldice: function
  returns: num of points in round or -1 to quit
  - loop for round_num in given num of rounds
  """
  print(f"staring round {round_num}")
  round_score =0
  num_dice = 6
  
  while True:
    print(f"rolling {num_dice} dice..")
      roll = roll_dice(num_dice)
      display_formated_roll()
      if Gamelogic.calculate_score(roll):
        zilch()
        return 0
      else:
        keepers = validate_keepers(roll)
        #roll again, b or q
          
def end_game(score):
  print(f"Thanks for playing. You earned {500} points")
  
def complete_round( round_num, total_score, round_score):
  print( f"You banked {round_score} points in round {round_num}, Total score is {total_score} points")
  
    
```