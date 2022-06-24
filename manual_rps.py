import numpy
from RPS_solution import vision
import random


class Rps:

    def __init__(self):
        self.choice = ['Rock', 'Paper', 'Scissors']
        self.user_wins = 0
        self.computer_wins = 0
        self.rounds_played = 0
        self.computer_choice = ""
        self.user_choice = ""

    def get_computer_choice(self):
        self.computer_choice = self.choice[random.randint(0,2)]
        print(f"Computer chose {self.computer_choice}")
        return self.computer_choice
    
    def get_user_choice(self):
        self.user_choice = self.choice[self.get_prediction()]
        print(f"You chose {self.user_choice}")
        return self.user_choice
    
    def get_prediction(self):
        number = numpy.argmax(vision()) - 1
        return number
    
    def get_winner(self, player_1, player_2):
        first  = self.choice.index(player_1)
        second = self.choice.index(player_2)
        result = first - second
        print(result)

        if result == 0:
            print("It's a draw.")
        elif result == -1 or result == 2:
            print("You lose.")
            self.computer_wins += 1
        else:
            print("You win.")
            self.user_wins += 1
        self.rounds_played += 1
    
    def play(self):
        while self.rounds_played < 5:
            self.get_winner(self.get_user_choice(), self.get_computer_choice())
        print(f"Computer scored {self.computer_wins}.\nYou scored {self.user_wins}.")
        if self.computer_wins > self.user_wins:
            print("You have lost the war.")
        elif self.user_wins > self.computer_wins:
            print("You have won the war.")
        else:
            print("Stalemate. Impasse. Deadlock. Unanimous draw.")


game = Rps()
game.play()

