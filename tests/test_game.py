# tests/test_game.py
import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_empty_word(self):
        new_game = Game()
        self.assertIs(new_game.is_valid(''), False)

    def test_word_is_valid(self):
        new_game = Game()
        new_game.grid = list('TWEUTAKSZ')
        self.assertIs(new_game.is_valid('TEST'), True)
        self.assertEqual(new_game.grid, list('TWEUTAKSZ'))
