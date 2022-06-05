class Player():
    def __init__(self, name, choice, has_played):
        self.name = name
        self.choice = choice
        self.has_played = has_played
    

    # def play_RPS(self, player1_choice, player2_choice):
    #     option_list = ["rock", "paper", "scissors"]
    #     if player1_choice == player2_choice:
    #         return "draw"