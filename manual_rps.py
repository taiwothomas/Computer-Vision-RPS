#from curses import KEY_MARK
import random
from camera_rps import get_prediction


choice = ["Rock", "Paper", "Scissors"]
computer_wins = 0
user_wins = 0
rounds_played = 0

def get_computer_choice():
    global choice
    computer_choice = choice[random.randint(0,2)]
    return computer_choice

def get_user_choice():
    global choice
    num = get_prediction()
    user_choice = choice[num]
    return user_choice

def get_winner(player_1, player_2):
    global choice, computer_wins, user_wins, rounds_played
    first = choice.index(player_1)
    second = choice.index(player_2)
    result = first - second
    if result == 0:
        print("It's a draw")
    elif result == -1 or 2:
        print("You lose.")
        computer_wins += 1
    else:
        print("You win!")
        user_wins += 1
    rounds_played += 1
    return computer_wins, user_wins

def play():
    get_winner(get_user_choice(), get_computer_choice())

while rounds_played < 5:
    play()
    
if computer_wins > user_wins:
    print("You have lost the war.")
elif user_wins > computer_wins:
    print("You have won the war.")
else:
    print("Stalemate. Impasse. Deadlock. Unanimous draw.")