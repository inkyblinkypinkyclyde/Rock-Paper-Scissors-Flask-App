from models.player import Player
# from player import Player
import random

player1 = Player("John", "Rock")
player2 = Player("Jarrod", "Paper")
player3 = Player("Stan", "scissors")

player_list = [player1, player2, player3]

possible_actions = ["rock", "paper", "scissors"]

def play_game_pve(choice):
    computer_choice = random.choice(possible_actions)
    if computer_choice == choice:
        return f"It's a draw, computer also chose {choice}"
    elif choice == "rock":
        if computer_choice == "scissors":
            return "Rock crushes scissors. You win"
        else: 
            return "Paper wraps rock. You Lose"
    elif choice == "scissors":
        if computer_choice == "paper":
            return "Scissors wrap paper. You win"
        else:
            return "Rock crushes scissors. You Lose"
    elif choice == "paper":
        if computer_choice == "rock":
            return "Paper wraps rock. You win"
        else:
            return "Scissors cut paper. You lose"
    