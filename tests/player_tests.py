import unittest

from models.player import Player
from models.players import *

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Alice", "")
        self.player2 = Player("Bob", "")

#draw condition tests
    def test_p1R_p1R(self):
        self.player1.choice = "rock"
        self.player2.choice = "rock"
        winner = self.player1.play_RPS(self.player1, self.player2)
        self.assertEqual("draw", winner)

    def test_p1P_p1P(self):
        self.player1.choice = "paper"
        self.player2.choice = "paper"
        winner = self.player1.play_RPS(self.player1, self.player2)
        self.assertEqual("draw", winner)

    def test_p1S_p1RS(self):
        self.player1.choice = "scissors"
        self.player2.choice = "scissors"
        winner = self.player1.play_RPS(self.player1, self.player2)
        self.assertEqual("draw", winner)

#player 1 win condition tests
    def test_p1R_p1S(self):
        self.player1.choice = "rock"
        self.player2.choice = "scissors"
        winner = self.player1.play_RPS(self.player1, self.player2)
        self.assertEqual(self.player1, winner)

    def test_p1S_p1P(self):
        self.player1.choice = "scissors"
        self.player2.choice = "paper"
        winner = self.player1.play_RPS(self.player1, self.player2)
        self.assertEqual(self.player1, winner)

    def test_p1P_p1R(self):
        self.player1.choice = "paper"
        self.player2.choice = "rock"
        winner = self.player1.play_RPS(self.player1, self.player2)
        self.assertEqual(self.player1, winner)

#player 2 win condition tests
    def test_p1R_p1P(self):
        self.player1.choice = "rock"
        self.player2.choice = "paper"
        winner = self.player1.play_RPS(self.player1, self.player2)
        self.assertEqual(self.player2, winner)

    def test_p1S_p1R(self):
        self.player1.choice = "scissors"
        self.player2.choice = "rock"
        winner = self.player1.play_RPS(self.player1, self.player2)
        self.assertEqual(self.player2, winner)

    def test_p1P_p1S(self):
        self.player1.choice = "paper"
        self.player2.choice = "scissors"
        winner = self.player1.play_RPS(self.player1, self.player2)
        self.assertEqual(self.player2, winner)


