import random

choice = ["Rock", "Paper", "Scissors"]

def get_computer_choice():
    computer_choice = choice[random.ranint(0,2)]
    return computer_choice

def get_user_choice():
    num = input("Choose 0 for 'Rock', 1 for 'Paper' and 2 for 'Scissors': ")
    user_choice = choice[num]
    return user_choice

