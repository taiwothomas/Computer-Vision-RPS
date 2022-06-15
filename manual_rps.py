from curses import KEY_MARK
import random

choice = ["Rock", "Paper", "Scissors"]

def get_computer_choice():
    computer_choice = choice[random.ranint(0,2)]
    return computer_choice

def get_user_choice():
    num = input("Choose 0 for 'Rock', 1 for 'Paper' and 2 for 'Scissors': ")
    user_choice = choice[num]
    return user_choice

def get_winner(player_1, player_2):
    global choice
    first = choice.index(player_1)
    second = choice.index(player_2)
    result = first - second
    if result == 0:
        print("It's a draw")
    elif result == -1 or 2:
        print("You lose.")
    else:
        print("You win!")

def play():
    get_winner(get_user_choice(), get_computer_choice())

play()
