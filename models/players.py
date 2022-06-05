from models.player import Player
# from player import Player
import random



player1LAN = Player("Alice", "", False)
player2LAN = Player("Bob", "", False)
results_list = []

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

def play_game_URL_input(player1, player2):
    if player1.choice == player2.choice:
        return "It's a draw, you chose the same thing."
    elif player1.choice == "rock":
        if player2.choice == "scissors":
            return "Player one wins! Rock crushes scissors."
        else: 
            return "Player two wins! Paper wraps rock."
    elif player1.choice == "scissors":
        if player2.choice == "paper":
            return "Player one wins! Scissors wrap paper."
        else:
            return "Player two wins! Rock crushes scissors."
    elif player1.choice == "paper":
        if player2.choice == "rock":
            return "Player one wins! Paper wraps rock."
        else:
            return "Player two wins! Scissors cut paper."

def play_game_LAN_input(player1LAN, player2LAN):
    if player1LAN.choice == player2LAN.choice:
        return "It's a draw, you chose the same thing."
    elif player1LAN.choice == "rock":
        if player2LAN.choice == "scissors":
            return "Player one wins! Rock crushes scissors."
        else: 
            return "Player two wins! Paper wraps rock."
    elif player1LAN.choice == "scissors":
        if player2LAN.choice == "paper":
            return "Player one wins! Scissors wrap paper."
        else:
            return "Player two wins! Rock crushes scissors."
    elif player1LAN.choice == "paper":
        if player2LAN.choice == "rock":
            return "Player one wins! Paper wraps rock."
        else:
            return "Player two wins! Scissors cut paper."

def play_game_select_input(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a draw, you chose the same thing."
    elif player1_choice == "rock":
        if player2_choice == "scissors":
            return "Player one wins! Rock crushes scissors."
        elif player2_choice == "paper": 
            return "Player two wins! Paper wraps rock."
        else:
            return "something went wrong1. You shouldn't see this string"       
    elif player1_choice == "scissors":
        if player2_choice == "paper":
            return "Player one wins! Scissors wrap paper."
        elif player2_choice == "rock":
            return "Player two wins! Rock crushes scissors."
        else:
            return "something went wrong2. You shouldn't see this string"
    elif player1_choice == "paper":
        if player2_choice == "rock":
            return "Player one wins! Paper wraps rock."
        elif player2_choice == "scissors":
            return "Player two wins! Scissors cut paper."
        else:
            return "something went wrong3. You shouldn't see this string"